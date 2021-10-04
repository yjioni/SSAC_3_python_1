from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog

# execute a chromedriver
root = Tk()
root.filename = filedialog.askopenfilename(title='Chrome_webdriver',
                                           initialdir='C:/Users/',
                                           filetypes=(('exe files', '*.exe'),
                                                      ('all files', '*.*'))
                                           )

driver = webdriver.Chrome(root.filename)

# indicate an url for the chromedriver
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

# get html data
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# crwaling_a ranking
songs = soup.select('tbody > tr')

# print the ranking
for rank, song in enumerate(songs):
    title = song.select('span > a')[0].text
    singer = [i.text for i in song.select('div.ellipsis.rank02 > a')]
    print(f'{rank+1}\t{title}\t{singer}')

