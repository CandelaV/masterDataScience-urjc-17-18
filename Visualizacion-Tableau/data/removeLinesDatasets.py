import os


def remove_2_lines(folder):

    filenames = os.listdir(folder)
    for file in filenames:

        if file.endswith('.csv'):

            file_in = open("./"+ folder + "/" + file, 'rb')

            lines = file_in.readlines()

            file_in.close()

            if not os.path.isdir(folder_out):
                os.mkdir(folder_out)

            file_out = open(folder_out + file, "w")

            for line in lines[2:]:

                file_out.write(line.decode())

            file_out.close()


if __name__ == "__main__":

    folder_in = "Datasets_genderstats"
    folder_out = "./Datasets_genderstats_new/"
    remove_2_lines(folder_in)

