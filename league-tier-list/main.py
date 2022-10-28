from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://u.gg/lol/jungle-tier-list")

champs_names = driver.find_elements(By.CLASS_NAME, 'champion-name')
num_of_champs = [i for i, n in enumerate(champs_names)]
tier_champs = driver.find_elements(By.CSS_SELECTOR, "b")


for rank in num_of_champs:
    print(rank+1)
    print(champs_names[rank].get_attribute("textContent"))
    print(tier_champs[rank].get_attribute("textContent"))

