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

url = 'https://music.bugs.co.kr/chart'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

bucks_data = []
songs = soup.select('table.list > tbody > tr')

for rank, song in enumerate(songs):
    title = song.select('th > p > a')[0].text
    singer = song.select('p.artist > a')[0].text
    bucks_data.append(['Bucks', rank+1, title, singer])

columns = ['서비스', '순위', '제목', '가수']
df_bucks = pd.DataFrame(bucks_data, columns=columns)

save_name = filedialog.asksaveasfilename(title='save as',
                                         initialdir='C:/Users/',
                                         )
df_bucks.to_excel(save_name, index=False)