from selenium import webdriver

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

songs = driver.find_elements_by_css_selector('table > tbody > tr')
for song in songs:
    title = song.find_elements_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
    print(title)


