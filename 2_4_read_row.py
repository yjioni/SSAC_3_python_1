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

# 가독성을 높이기 위해 줄변경해서 작성하기 `\` 사용
#  성별이 '남성' 이면서, 입국객수가 10만 이상인 것 출력
condition2 = (sample['성별'] == '남성') \
             & (sample['입국객수'] >= 100000)
print(sample[condition2])
print()

# | == or조건, 여러 조건 중 한가지만 만족하면 출력력
# # 국적코드가 A01 or A18인 것 출력
condition3 = (sample['국적코드'] == 'A01') \
             | (sample['국적코드'] == 'A18')
print(sample[condition3])
print()

# | == or == isin['조건1', '조건2']
condition4 = (sample['국적코드'].isin(['A01', 'A18']))
print(sample[condition4])
print()

# 조건에 해당하지 않는 것 출력
condition5 = (sample['국적코드'].isin(['A01', 'A18']))
print(sample[condition5 == False])