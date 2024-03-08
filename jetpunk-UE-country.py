from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
options = Options()
options.add_argument("--user-data-dir=D:\\Temp\\chrome") 
driver = webdriver.Chrome(options=options)

driver.get("https://www.jetpunk.com/user-quizzes/6121/pays-deurope-en-une-minute")

time.sleep(5)

# Start button
driver.find_element(By.ID, 'start-button').click()

pays = ["Albanie", "Allemagne", "Andorre", "Autriche",
        "Belgique",
        "Biélorussie",
        "Bosnie",
        "Bulgarie",
        "Croatie",
        "Danemark",
        "Espagne",
        "Estonie",
        "Finlande",
        "France",
        "Grèce",
        "Hongrie",
        "Irlande",
        "Islande",
        "Italie",
        "Kosovo",
        "Lettonie",
        "Liechtenstein",
        "Lituanie",
        "Luxembourg",
        "Macédoine",
        "Malte",
        "Moldavie",
        "Monaco",
        "Monténégro",
        "Norvège",
        "Pays-Bas",
        "Pologne",
        "Portugal",
        "tchequie",
        "Roumanie",
        "Royaume-Uni",
        "Russie",
        "Saint-Marin",
        "Serbie",
        "Slovaquie",
        "Slovénie",
        "Suède",
        "Suisse",
        "Ukraine",
        "Vatican"]

for country in pays:
    driver.find_element(By.NAME, 'stopitchrome').send_keys(country)
    time.sleep(0.1)

# close browser after 20s 
time.sleep(20) 