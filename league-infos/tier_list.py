from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import json

chrome_driver_path = MY_CHROME_DRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.leagueofgraphs.com/champions/builds/jungle/by-winrate")

reject_all = driver.find_element(By.XPATH, '//*[@id="ncmp__tool"]/div/div/div[3]/div[1]/a')
reject_all.click()

champs_names = driver.find_elements(By.CLASS_NAME, 'name')
champs_names = [name for i, name in enumerate(champs_names) if i != 0]
num_of_champs = [i for i, n in enumerate(champs_names)]
champs_data = driver.find_elements(By.CLASS_NAME, 'progressBarTxt')


def multiple_tabs():
    champ_in_url = [champs.text.lower().replace("&", "").replace("'", "").replace(".", "").replace(" ", "") for champs in champs_names]

    for i, champ in enumerate(champ_in_url):
        print(champ)
        if champ == "wukong":
            champ = "monkeyking"
        if champ == "nunuwillump":
            champ = "nunu"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i+1])
        driver.get(f'https://www.leagueofgraphs.com/champions/builds/{champ}/jungle')

        with open(f'images/champ{i}.png', 'wb') as file:
            file.write(driver.find_element(By.XPATH,
                '//*[@id="pageContent"]/div[1]/div/div[1]/img').screenshot_as_png)


with open('data/champs_jungle.json', "w") as empty_file:
    empty = {"champs": []}
    json.dump(empty, empty_file)


for i in num_of_champs:
    print(i+1, champs_names[i].text)
    print(f"Popularity: {champs_data[i*3].text} | Winrate: {champs_data[(i*3)+1].text} | Banrate: {champs_data[(i*3)+2].text}")

    champ_info = {
                "name": champs_names[i].text,
                "popularity": str(champs_data[i*3].text),
                "winrate": str(champs_data[(i*3)+1].text),
                "banrate": str(champs_data[(i*3)+2].text)
                }

    with open('data/champs_jungle.json', "r") as old_file:
        file_champ_info = json.load(old_file)

    file_champ_info["champs"].append(champ_info)

    with open('data/champs_jungle.json', 'w') as file:
        json.dump(file_champ_info, file, indent=4)


driver.quit()

