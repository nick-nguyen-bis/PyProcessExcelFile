import pandas as pd
print('Hello World')
excelPath = 'D:\Chirality Files\DEV\Python\PyProcessExcelFile\Book1.xlsx' 
print('excelPath=['+ excelPath + ']') 
df = pd.read_excel(excelPath)
print(df)
print('Program ends here !')



