meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "RACINGUEADA" : "Pechear en un partido de futbol",
            "FACHA" : "Una persona que esta bien vestida",
            "QUILOMBO" : "Hay desorden en un lugar", 
            "LABURAR" : "Trabajar",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("Significado:", meme_dict[word])
else:
    print("No se encuentra esa palabra en el diccionario")
