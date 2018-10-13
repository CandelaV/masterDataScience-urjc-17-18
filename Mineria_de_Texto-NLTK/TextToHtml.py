from bs4 import BeautifulSoup
import os


def text_to_html(folder):

    filenames = os.listdir(folder)
    for file in filenames:

        if file.endswith('.html'):

            file_in = open("./"+folder+ "/" + file, 'rb')

            # Pasamos el contenido HTML a un objeto BeautifulSoup
            html = BeautifulSoup(file_in)
            file_in.close()

            # Obtenemos todos los párrafos para capturar el texto.
            parrafos = html.find_all('p')

            # Generamos el texto a procesar uniendo los párrafos detectados.
            text = ""
            for parrafo in parrafos:
                text = text + parrafo.getText() + "\n"

            if not os.path.isdir('./CorpusNoticiasPractica1718/'):
                os.mkdir('./CorpusNoticiasPractica1718/')

            # Generamos el fichero de CorpusNoticiasPractica1718
            file_out = open("./CorpusNoticiasPractica1718/" + file.strip(".html") + ".txt", "w")
            file_out.write(text)
            file_out.close()


if __name__ == "__main__":

    folder_input = "Corpus"
    text_to_html(folder_input)