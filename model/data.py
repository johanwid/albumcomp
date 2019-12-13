import glob
import pandas as pd

dataLocation = "../data/albums/*.xlsx"


class Data:

    def __init__(self):
        self.df = pd.DataFrame()

    def getData(self):
        data = list()
        for myfile in glob.glob(dataLocation):
            data.append(myfile)
        return data

    def convertTableToDb(self):

        data = self.getData()
        for myfile in data:
            excel = pd.read_excel(myfile, "Master")
            self.df = self.df.append(excel)

    def randomizeTable(self):
        self.df = self.df.sample(frac=1).reset_index(drop=True)


if __name__ == "__main__":
    d = Data()
    d.convertTableToDb()
    d.randomizeTable()
