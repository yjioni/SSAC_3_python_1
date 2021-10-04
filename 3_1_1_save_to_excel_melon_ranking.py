from selenium import webdriver
from bs4 import BeautifulSoup

from tkinter import filedialog, Tk

root = Tk()
root.filename = filedialog.askopenfilename(title='chrome_driver',
                                           initialdir='C:/Users/',
                                           filetypes=(('exe files', '*.exe'),
                                                      ('all files', '*.*'))
                                           )
driver = webdriver.Chrome(root.filename)

# melon
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

melon_data = []
songs = soup.select('tbody > tr')

songs[0].select('div.rank02 > a')

# crawling
for rank, song in enumerate(songs):
    title = song.select('span > a')[0].text
    singer = [i.text for i in song.select('div.rank02 > a')]
    melon_data.append(['Melon', rank+1, title, singer])

# DataFrame
import pandas as pd
columns = ['서비스', '순위', '제목', '가수']
df_melon = pd.DataFrame(melon_data, columns=columns)

# save to_excel
save_name = filedialog.asksaveasfilename(title='save as',
                                         initialdir='C:/Users/',
                                         )
df_melon.to_excel(save_name, index=False)