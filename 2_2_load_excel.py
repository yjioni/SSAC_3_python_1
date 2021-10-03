import pandas as pd

sample_1 = pd.read_excel('C:/Users/oing9/Desktop/Yulia/SSAC_3/web_crawling/datasalon-master/02_개정판/2_Data_Analysis_Basic/files/sample_1.xlsx',
                         header=1, skipfooter=2,
                         usecols='A:C')
print(sample_1.info())
print()
print(sample_1)
print()
print(sample_1.head(3))
print()
print(sample_1.tail(3))

