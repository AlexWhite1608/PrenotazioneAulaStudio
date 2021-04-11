import setup

def login():
    username = setup.driver.find_element_by_id("username")
    username.send_keys(setup.matricola)

    password = setup.driver.find_element_by_id("password")
    password.send_keys(setup.password)

    try:
        setup.driver.find_element_by_name("submit").click()
    except:
        print("Errore nell'autenticazione")