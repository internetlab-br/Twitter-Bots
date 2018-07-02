import tweepy
import pymysql
from operator import itemgetter

def conecta_banco():
    db = pymysql.connect("", "", "", "")
    return db

def create_lista ():
    db = conecta_banco()
    cursor = db.cursor()

    sql = """SELECT * FROM politicos where buscar = 1"""

    cursor.execute(sql)

    lista = cursor.fetchall()
    db.close()

    return lista

def update_politico(id, seguidores, handle, nome):
    db = conecta_banco()
    cursor = db.cursor()

    sql = "UPDATE `bot_followers`.`politicos` SET `nome`='"+nome+"', `handle`='"+handle+"', `seguidores`='"+str(seguidores)+"' " \
          "WHERE `id`='"+str(id)+"';"

    cursor.execute(sql)
    db.commit()
    db.close()

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('',
                      '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                 retry_errors=set([503]))


lista = create_lista()

print(lista)

for target in lista:
    user = api.get_user(target[0])
    print(target[1], user.followers_count)
    update_politico(target[0], user.followers_count, user.name,user.screen_name)

lista = sorted(lista, key=itemgetter(3))

print(lista)

for pessoa in lista:
    db = conecta_banco()
    cursor = db.cursor()
    users = []
    page_count = 0
    start = pessoa[3]

    try:
        for user in tweepy.Cursor(api.followers_ids, id=pessoa[0], count=5000).pages():
            page_count += 1
            print('Getting page {} for followers of '.format(page_count) + str(pessoa[2]))
            users.extend(user)
            for user in users:
                sql = "REPLACE INTO `bot_followers`.`seguidores` " \
                      "(`id`)" \
                      "VALUES ('%d');" % user
                cursor.execute(sql)

                sql = "INSERT INTO `bot_followers`.`politicos_seguidores` " \
                      "(`id_politico`, `id_seguidor`, `pos_seguidor`) " \
                      "VALUES ('%d', '%d', '%d');" % (pessoa[0], user, start)
                cursor.execute(sql)


                start -= 1

            db.commit()
            users.clear()



    except Exception as e:
        print("Deu ruim no " + pessoa[2] + ", próximo nome....")
        print(e)

    finally:
        db.close()
