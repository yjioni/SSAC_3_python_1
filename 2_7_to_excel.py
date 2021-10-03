import pandas as pd
from tkinter import filedialog

# file1
file_name = filedialog.askopenfilename(title='sample_1.xlsx',
                                       initialdir='C:/Users',
                                       filetypes=(('excel files', '*.xlsx'),
                                                  ('all files', '*.*'))
                                       )
sample = pd.read_excel(file_name, header=1, skipfooter=2,
                       usecols='A:C')
sample['기준년월'] = '2019-11'

# sub_file
file_name1= filedialog.askopenfilename(title='sample_codemaster.xlsx')
sample_codemaster = pd.read_excel(file_name1)

# merge1 = file1 + sub_file
sample_merge = pd.merge(left=sample, right=sample_codemaster,
                        how='left', 
                        left_on='국적코드',
                        right_on='국적코드')

# file2
file_name2 = filedialog.askopenfilename(title='sample_2.xlsx',
                                        initialdir='C:/Users',
                                        filetypes=(('excel files', '*.xlsx'),
                                                   ('all files', '*.*'))
                                        )

sample2 = pd.read_excel(file_name2, header=1, skipfooter=2,
                        usecols='A:C')
sample2['기준년월'] = '2019-12'

# merge2 = file2 + sub_file
sample_merge1 = pd.merge(left=sample2, right=sample_codemaster,
                         how='left',
                         left_on='국적코드',
                         right_on='국적코드')

# append tables
sample_append = sample_merge.append(sample_merge1, 
                                    ignore_index=True)

print(sample_append)

# 저장
save_name = filedialog.asksaveasfilename(title='save as...',
                                         initialdir='./',
                                         filetypes=(('excel files', '*.xlsx'),
                                                    ('all files', '*.*'))
                                        )
sample_append.to_excel(save_name, index=False)