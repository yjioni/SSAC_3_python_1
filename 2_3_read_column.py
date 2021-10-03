import pandas as pd

from tkinter import *
from tkinter import filedialog

filename = filedialog.askopenfilename(title='choose a file to read',
                                      initialdir='C:/Users',
                                      filetypes=(('excel files', ('*.xlsx')),
                                                 ('all files', '*.*')
                                                )
                                      )

sample = pd.read_excel(filename, header=1, skipfooter=2,
              usecols='A:C')

print(sample.info())
print()

print(sample)
print()

print('국적코드 column:\n', sample['국적코드'])
print()

print('국적코드&입국객수:\n', sample[['국적코드','입국객수']])
print()

sample['기준연월'] = '2019-11'
print(sample)