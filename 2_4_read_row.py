import pandas as pd

from tkinter import *
from tkinter import filedialog

filename = filedialog.askopenfilename(title='choose file',
                                      initialdir=('C:/Users/'),
                                      filetypes=(('excel files', '*.xlsx'),
                                                 ('all files', '*.*'))
                                     )

sample = pd.read_excel(filename, header=1, 
                       skipfooter=2, usecols='A:C')

print(sample)
print()

condition = (sample['성별'] == '남성')
print(condition)
print()

print(sample[condition])
print()

condition1 = (sample['입국객수'] > 100000)
print(condition1)
print()

print(sample[condition1])
print()

condition2 = (sample['성별'] == '남성') & (sample['입국객수'] >= 100000)
print(sample[condition2])
print()

condition3 = (sample['국적코드'] == 'A01')|(sample['국적코드'] == 'A18')
print(sample[condition3])
print()

condition4 = (sample['국적코드'].isin(['A01', 'A18']))
print(sample[condition4])
