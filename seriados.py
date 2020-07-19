#!/usr/bin/python3

from pymongo import MongoClient

# conecta ao banco de dados 
client = MongoClient('mongodb://localhost:27017/')

print("== Collections do database test")

with client:
    
    # lista as collections 
    db = client.test
    print(db.list_collection_names())

    # remove o registro se existir
    db.seriados.delete_one({ "_id":"10"})

    # lista os seriados
    seriados = db.seriados.find()
 
    print("=== Seriados ===")
    for seriado in seriados:
        print('Seriado: {0} - personagens: {1}'.
           format(seriado['nome'], 
            seriado['personagens']))

    # total de seriados
    total_de_seriados = db.seriados.count_documents({})

    print("=== Total de seriados: {}".format(total_de_seriados))

    # adiciona um seriado
    seriado3porCentro = { "_id" : "10",
                          "nome" : "3%",
                          "personagens" : ["Michele","Joana","Rafael","Marco","Ezequiel","Fernando"]}

    print("=== novo seriado: "+str(seriado3porCentro))

    db.seriados.insert_one(seriado3porCentro)     

    query_3porcento = { "_id": "10" }
    novos_valores = { "$set": { "nome": "3% - 3 por cento" } }

    # atualiza o nome do seriado
    db.seriados.update_one(query_3porcento, novos_valores)

    seriados = db.seriados.find()
 
    print("=== Seriados ===")
    for seriado in seriados:
        print('Seriado: {0} - personagens: {1}'.
           format(seriado['nome'], 
            seriado['personagens']))

    total_de_seriados = db.seriados.count_documents({})

    print("===Total de seriados: {}".format(total_de_seriados))	