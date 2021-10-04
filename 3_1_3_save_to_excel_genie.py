from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from tkinter import filedialog, Tk

root = Tk()
root.filename = filedialog.askopenfilename(title='chrome_driver',
                                           initialdir='C:/Users/',
                                           filetypes=(('exe files', '*.exe'),
                                                      ('all files', '*.*'))
                                           )
driver = webdriver.Chrome(root.filename)

url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

genie_data = []

songs = soup.select('tbody > tr')

for rank, song in enumerate(songs):
    title = song.select('td.info > a.title')[0].text.strip()
    singer = song.select('td.info > a.artist')[0].text
    genie_data.append(['Genie', rank+1, title, singer])

columns = ['서비스', '순위', '제목', '가수']
df_genie = pd.DataFrame(genie_data, columns=columns)

save_name = filedialog.asksaveasfilename(title='save as',
                                         initialdir='C:/Users/',
                                         )
df_genie.to_excel(save_name, index=False)