import pandas as pd

from tkinter import *
from tkinter import filedialog

root = Tk()
file_name = filedialog.askopenfilename(title='choose an excel file',
                                initialdir='C:/Users',
                                filetypes=(('excel files', '*.xlsx'),
                                            ('all files', '*.*')
                                           )
                                        )
sample_1 = pd.read_excel(file_name,
                         header=1, skipfooter=2,
                         usecols='A:C')
print(sample_1.info())
print()
print(sample_1)
print()
print(sample_1.head(3))
print()
print(sample_1.tail(3))

