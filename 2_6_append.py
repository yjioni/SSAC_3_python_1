import pandas as pd

from tkinter import filedialog

# read sample1
# sample1.xlsx 사용
filename = filedialog.askopenfilename(title='sample_1.xlsx',
                                      initialdir='C:/Users',
                                      filetypes=(('excel files', '*.xlsx'),
                                                 ('all files', '*.*'))
                                      )
sample = pd.read_excel(filename, header=1, skipfooter=2,
                       usecols='A:C')
sample['기준연월'] = '2019-11'

# sub_sample
# sample_codemaster.xlsx 사용
filename1 = filedialog.askopenfilename(title='sample_codemaster.xlsx',
                                      initialdir='C:/Users',
                                      filetypes=(('excel files', '*.xlsx'),
                                                 ('all files', '*.*'))
                                      )
sample1 = pd.read_excel(filename1)

# left_join >>> sample1 + sub_sample
sample_merge1 = pd.merge(left=sample, right=sample1, how='left',
                         left_on='국적코드', right_on='국적코드')
print(sample_merge1)
print()

# read sample2
filename2 = filedialog.askopenfilename(title='sample_2.xlsx',
                                       initialdir='C:/Users',
                                       filetypes=(('excel files', '*.xlsx'),
                                                  ('all files', '*.*'))
                                        )
sample2 = pd.read_excel(filename2, header=1, skipfooter=2, 
                        usecols='A:C')
sample2['기준연월'] = '2019-12'

# left_join >>> sample2 + sub_sample
sample_merge2 = pd.merge(left=sample2, right=sample1,
                         how='left', 
                         left_on ='국적코드',
                         right_on='국적코드')
print(sample_merge2)
print()

# 데이터를 위아래로 통합
# table1.append(table2, ignore_index=True)
sample_append = sample_merge1.append(sample_merge2, 
                                     ignore_index=True)
print(sample_append)


