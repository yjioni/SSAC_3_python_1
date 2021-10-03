import pandas as pd

from tkinter import *
from tkinter import filedialog

# read sample1
filename = filedialog.askopenfilename(title='sample_1.xlsx',
                                      initialdir='C:/Users',
                                      filetypes=(('excel files', '*.xlsx'),
                                                 ('all files', '*.*'))
                                      )
sample = pd.read_excel(filename, header=1, skipfooter=2,
              usecols='A:C')
print('sample1:\n', sample)

# read sample2
filename2 = filedialog.askopenfilename(title='sample_codemaster.xlsx',
                                       initialdir='C:/Users',
                                       filetypes=(('excel files', '*.xlsx'),
                                                  ('all files', '*.*'))
                                       )
sample2 = pd.read_excel(filename2,
                        usecols='A:B')
print('sample2:\n', sample2)

# join
# pd.merge(left=, right=, how='left', left_on=, right_on=)
# 좌측 data table 기준, 매칭 값이 없을 경우 NaN 출력
sample_left_merge = pd.merge(left=sample, 
                        right=sample2,
                        how='left',
                        left_on='국적코드',
                        right_on='국적코드')

print(sample_left_merge)

# inner join
# pd.merge(left=, right=, how='inner', left_on=, right_on=)
# 두개 테이블이 매칭 가능한 값만 출력 (NaN 제외)
sample_inner_merge = pd.merge(left=sample,
                          right=sample2,
                          how='inner',
                          left_on='국적코드',
                          right_on='국적코드')
print(sample_inner_merge)
