import pandas as pd

df = pd.read_excel('C:\\Curso01\\Secao08\\myexcel.xlsx')

variable = 0
#iterating over an excel file

for row in range(len(df)):
    # print(df['name'][row])
    #Age is une column at the database
    #Row is a "counter"
    #LOC == select in one data base
    #ILOC => only integers
    # print(df.loc[row, 'age'])
    variable = int(df.loc[row, 'age'])
    if variable > 1:
        print('age is greater than 9')
