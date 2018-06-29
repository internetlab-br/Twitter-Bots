import random

import botometer
import pymysql
import tweepy


def conecta_banco():
    db = pymysql.connect("", "", "", "")
    return db

def create_lista ():
    db = conecta_banco()
    cursor = db.cursor()

    sql = """SELECT * FROM seguidores where probabilidade is null"""
    cursor.execute(sql)

    lista = cursor.fetchall()
    db.close()

    return list(lista)

def update_pessoa(id, prob):
    db = conecta_banco()
    cursor = db.cursor()

    sql = "UPDATE `bot_followers`.`seguidores` SET `probabilidade`='"+str(prob)+"'WHERE `id`='"+str(id)+"';"

    cursor.execute(sql)
    db.commit()
    db.close()

mashape_key = ""
twitter_app_auth = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)


auth = tweepy.OAuthHandler('', '')
auth.set_access_token('',
                      '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                 retry_errors=set([503]))


lista = create_lista()
random.shuffle(lista)
count = 0

for seguidor in lista:
    try:
        result = bom.check_account(seguidor[0])
        count += 1
        print (str(count) + ":\t" + result['user']['screen_name'] + "  " + str(result['cap']['universal']))
        update_pessoa(seguidor[0], result['cap']['universal'])
    except Exception as inst:
        # print (str(seguidor[0]) + "\t\tsem score")
        print (seguidor[0])
        update_pessoa(seguidor[0], -1)
        print (inst)

    print()
