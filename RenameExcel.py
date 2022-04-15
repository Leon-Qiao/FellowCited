import pandas as pd
import os

dirs = os.listdir('PapersExcel')
for item in range(len(dirs)):
    target = pd.read_excel('PapersExcel/' + dirs[item], header = None)
    newName = target.iloc[0][0][5:-1]
    newName = newName.replace(',','')
    newName = newName.replace(':','')
    if newName+'.xls' not in dirs:
        os.rename('PapersExcel/' + dirs[item], 'PapersExcel/' + newName + '.xls')
    print(newName)