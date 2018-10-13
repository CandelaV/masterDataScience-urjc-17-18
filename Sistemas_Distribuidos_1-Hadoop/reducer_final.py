#!/usr/bin/env python

from __future__ import division
import sys

def main():

    ## se inicializan variables auxiliares

    region_prev = None
    score_prev = 0
    count = 0

    ## para cada linea de cada twitt que sale del map y entra ordenada en el reduce

    for line in sys.stdin:

        ## se eliminan espacios en blanco delante y detras

        line = line.strip()

        ## se separa por el tabulador la informacion obtenida con el map

        region, score = line.split('\t')

        ## se convierte la puntuacion de cada twitt de texto a numero

        try:
            score = float(score)
        except ValueError:
            continue

        ## si el twitt actual proviene del mismo estado que el anteriormente leido,
        ## como al reduce entran ordenados, se suma la puntuacion en la variable
        ## auxiliar score_prev y se aniade uno mas al contador de twitts count

        if region_prev == region:
            score_prev += score
            count += 1
        else:
            if region_prev:

                ## se muestran los resultados por la salida standard
                ## el estado de EEUU, su puntuacion normalizada y el numero de twitts

                print '%s\t%s\t%s' % (region_prev, score_prev/count, count)

            ## se inicializan nuevamente las variables para la siguiente nueva region

            count = 1
            score_prev = score
            region_prev = region


    ## contabilizar el ultimo twitt leido que proviene del map

    if region_prev == region:
        print '%s\t%s\t%s' % (region_prev, score_prev/count, count)

if __name__ == '__main__':
    main()