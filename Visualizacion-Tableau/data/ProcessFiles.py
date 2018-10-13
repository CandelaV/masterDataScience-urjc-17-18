import pandas as pd
import os


def process_file(folder):

    filenames = os.listdir(folder)

    if not filenames[0].startswith("QL "):

        df = pd.read_csv("./"+ folder + "/" + filenames[0], delimiter = ",", decimal= ".")
        df = df[["Region", "Country Code", "Country", "Year", "Sex", "Value"]]
        df = df.rename(columns={'Value': filenames[0].strip("_data.csv")})
        print(df.columns)

    for file in filenames[1:]:

        print(file)

        if not file.startswith("QL "):

            df_1 = pd.read_csv("./" + folder + "/" + file, ",")
            df_1 = df_1[["Region", "Country Code", "Country", "Year", "Sex", "Value"]]
            df_1 = df_1.rename(columns={'Value': file.strip("_data.csv")})

            if len(df_1) > 1:

                df = df.merge(df_1,
                         on=["Region", "Country Code", "Country", "Year", "Sex"],
                         how="outer")
                print(len(df))
                print(df.columns)

    #df.loc[:, '24a - Gender parity index of the gross enrolment ratio in primary education'] *= 100
    #df.loc[:, '24b - Gender parity index of the gross enrolment ratio in secondary education'] *= 100
    #df.loc[:, '24c - Gender parity index of the gross enrolment ratio in tertiary education'] *= 100

    df.loc[df.Sex == 'not applicable', 'Sex'] = 'Parity Index'

    df.to_csv("./"+ "salidas" + "/" + "genderStats.csv", sep = ";", decimal=",")
    #df.to_csv("./" + "salidas" + "/" + "genderStats_6.csv", sep=",", decimal=".")


if __name__ == "__main__":

    folder_in = "./Datasets_genderstats_new/"
    process_file(folder_in)
