from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.leagueofgraphs.com/champions/builds/jungle/by-winrate")

champs_names = driver.find_elements(By.CLASS_NAME, 'name')
champs_names = [name for i, name in enumerate(champs_names) if i != 0]
num_of_champs = [i for i, n in enumerate(champs_names)]
champs_data = driver.find_elements(By.CLASS_NAME, 'progressBarTxt')


for i in num_of_champs:
    print(i+1, champs_names[i].text)
    print(f"Popularity: {champs_data[i*3].text} | Winrate: {champs_data[(i*3)+1].text} | Banrate: {champs_data[(i*3)+2].text}")



