#!/usr/bin/env python


import json, string, sys



## iniciamos diccionarios vacios

scores = {}
states = {}

## ficheros cuyo contenido se carga en los diccionarios

file_scores = "AFINN-111.txt"
file_states = "State.tsv"


## funcion para cargar contenido de ficheros en los diccionarios

sys.path.append('.')

def load_dictionary(file,dict):

    file_content = open(file)

    for line in file_content:
        key, value = line.split("\t")
        dict[key] = value

def main():

    ## se carga el contenido en ambos diccionarios vacios

    load_dictionary(file_scores,scores)
    load_dictionary(file_states,states)

    ## se lee el archivo de twitts a analizar linea a linea (twitt a twitt)

    for line in sys.stdin:

        line = line.strip()

        ## guardamos el twitt en la variable data con formato json

        data = ''
        try:
            data = json.loads(line)
        except ValueError as detail:
            sys.stderr.write(detail.__str__() + "\n")
            continue

        ## aplicamos filtros : exista texto, 'place' no sea nulo y el pais sea EEUU

        if 'text' in data and data['place'] is not None and data['place']['country_code'] == "US":

            ## pasamos el texto a minusculas
            text = data['text'].lower()

            ## encode a UTF-8 para eliminar errores de Unicode

            text = text.encode('utf-8')
            text = text.translate(string.maketrans(string.punctuation, ' ' * len(string.punctuation)))

            ## se divide el texto en palabras y se suma su puntuacion

            sentiment_score = 0
            for w in text.split(None):
                if len(w) > 0:
                    if w in scores:
                        sentiment_score += int(scores[w])

            ## se obtiene el estado de EEUU del usuario que ha escrito el twitt

            region = data['place']['full_name']

            ## por ser el campo 'full_name' introducido por el usuario,
            ## se intenta unificar utilizando un diccionario auxiliar
            ## con equivalencias entre el nombre del estado y sus siglas

            if "," in region:

                region1,region2 = region.split(",")

                if region2.strip() == "USA":

                    if region1 in states:

                        state = states[region1].strip()

                    else:
                        state = region1.strip()

                else:
                    state = region2.strip()
            else:
                state = region.strip()

            ## se saca por print el resultado del map para cada twitt leido que
            ## cumple con las caracteristicas del filtro impuesto

            print "\t".join([state, str(sentiment_score)]).encode('utf-8')


if __name__ == '__main__':
    main()