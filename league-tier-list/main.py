from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.leagueofgraphs.com/pt/champions/builds/jungle/by-winrate")

champs_names = driver.find_elements(By.CLASS_NAME, 'name')
num_of_champs = [i for i, n in enumerate(champs_names)]


for i in num_of_champs:
    print(i, champs_names[i].text)

