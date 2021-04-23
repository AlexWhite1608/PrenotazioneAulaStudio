import login
import setup
import prenotazione
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# inserire matricola e password
setup.matricola = input("Matricola: ")
setup.password = input("Password: ")

# apre il sito
setup.driver.get("https://kairos.unifi.it/portalePlanning/BIBL/login.php")

# fa il login con matricola e password
login.login()

mode = int(input("\nNuova prenotazione -> 1 \nVisualizza prenotazioni -> 2\n"))

if mode == 1:  # nuova prenotazione
    # aspetta che la pagina principale venga caricata
    try:
        pagina_principale = WebDriverWait(setup.driver, 5).until(
            EC.presence_of_element_located((By.ID, "titolo-pagina"))
        )

        # esegue prenotazione per la mattina
        prenotazione.nuova_prenotazione("Mattina")

    except NoSuchElementException:
        print("Finito Mattina")

    try:
        pagina_principale = WebDriverWait(setup.driver, 5).until(
            EC.presence_of_element_located((By.ID, "titolo-pagina"))
        )

        # esegue prenotazione per il pomeriggio
        prenotazione.nuova_prenotazione("Pomeriggio")

    except NoSuchElementException:
        print("Finito pomeriggio")

    # finite le prenotazioni, chiude tutto
    print("Tutte le prenotazioni sono state eseguite!")

elif mode == 2:  # visualizza prenotazioni
    try:
        pagina_principale = WebDriverWait(setup.driver, 10).until(
            EC.presence_of_element_located((By.ID, "titolo-pagina"))
        )

        prenotazione.gestione_prenotazioni()

    except NoSuchElementException:
        print("Impossibile aprire pagina prenotazioni!")
else:
    print("Comando errato!")

setup.driver.quit()
