import pymysql, samplesize
import numpy
import scipy.stats
from operator import itemgetter



def conecta_banco():
    db = pymysql.connect("", "", "", "")
    return db

def create_lista_pol ():
    db = conecta_banco()
    cursor = db.cursor()

    sql = """SELECT * FROM politicos where grafo = 1"""

    cursor.execute(sql)

    lista = cursor.fetchall()
    db.close()

    return lista

def create_lista_seg (id):
    db = conecta_banco()
    cursor = db.cursor()

    sql = "SELECT * FROM politicos_seguidores " \
            "INNER JOIN seguidores ON politicos_seguidores.id_seguidor = seguidores.id " \
            "WHERE probabilidade is not null " \
            "AND probabilidade != -1 " \
            "AND id_politico = %d" % (id)

    cursor.execute(sql)

    lista = cursor.fetchall()
    db.close()

    return lista


lista_pol = create_lista_pol()
lista_pol = sorted(lista_pol, key=itemgetter(0))

print("% Seguidores que são bots:\n")

for pol in lista_pol:
    lista_seg = create_lista_seg(pol[0])
    print (pol[2] + "\t\t\t#seguidores: " + str(pol[3]), end=" ")
    print ("\t#amostra: " + str(len(lista_seg)), end=" ")
    ideal = samplesize.sampleSize(pol[3], 0.01, 0.95, 0.5)
    print("\t#amostra para margem de 1%: "+ str(int(ideal)+1), end="\t\t")
    print(int(ideal)+1 < len(lista_seg))
    if (len(lista_seg) > 1):
        a = 1.0*(numpy.array(lista_seg)[:,5])
        n = len(a)
        m, se = numpy.mean(a), scipy.stats.sem(a)
        h = se * scipy.stats.t._ppf((1 + 0.99) / 2., n - 1)

        print("Média:\n"+str(100*m) +"% +/- " + str(100*(h)) + "%")
        print("IC: " + str( (m-h)*pol[3] ) + ", " + str( (m+h)*pol[3] ))
    print("")
