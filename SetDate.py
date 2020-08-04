import xlrd;
import pandas as pd
import numpy as np
from datetime import date

from openpyxl import load_workbook

book = xlrd.open_workbook('C:/Users/Saleem/Desktop/University/ML/Project/MachineLearning.xlsx')
sheet = book.sheet_by_name('Sheet1')

def emptySlot():
    for i in range(sheet.ncols):         
        print(i)
    return i
        
col = emptySlot()


today = date.today()

# dd/mm/YY
date = today.strftime("%d/%m/%Y")

fn = r'C:/Users/Saleem/Desktop/University/ML/Project/MachineLearning.xlsx'

df = pd.read_excel(fn, header=None)
df2 = pd.DataFrame({'Data': [date]})

writer = pd.ExcelWriter(fn, engine='openpyxl')
book = load_workbook(fn)

writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df.to_excel(writer, sheet_name='Sheet1', header=None, index=False)
df2.to_excel(writer, sheet_name='Sheet1', header=None, index=False,
             startcol=col+1,startrow=0)

writer.save()