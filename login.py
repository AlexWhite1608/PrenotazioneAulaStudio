import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():

    try:
        WebDriverWait(setup.driver, 5).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
    except:
        print("Errore nell'apertura del sito")
        setup.driver.quit()

    username = setup.driver.find_element_by_id("username")
    username.send_keys(setup.matricola)

    password = setup.driver.find_element_by_id("password")
    password.send_keys(setup.password)

    try:
        setup.driver.find_element_by_name("submit").click()
    except:
        print("Errore nell'autenticazione")