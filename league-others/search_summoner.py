from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/beatr/Development/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


def search_summoner(nick):
    driver.get("https://www.leagueofgraphs.com/")
    search_bar = driver.find_element(By.XPATH, '//*[@id="homepageForm"]/input')
    search_bar.send_keys(nick)

    search_button = driver.find_element(By.XPATH, '//*[@id="homepageForm"]/button')
    search_button.click()

    current_url = driver.current_url

    if "search" in current_url:
        summoner = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div/table/tbody/tr[2]/td[2]/div/div[2]/a')
        summoner.click()

    current_url = driver.current_url
    print(current_url)


summoners = input("Summoner Names: ")
summoners = summoners.split(", ")

for name in summoners:
    search_summoner(name)

