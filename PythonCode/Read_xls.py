# This program reads an number file(xlxs in MAC) and print the cell output
import pandas as pd
from numbers_parser import Document

def read_number():


if __name__ == '__main__':

    doc = Document("heridity.numbers")
    sheets = doc.sheets
    tables = sheets[0].tables
    data = tables[0].rows(values_only=True)
    print(pd.DataFrame(data[1:]))

    #df = pd.DataFrame(data[1:], columns=data[1:])
    #print(df)