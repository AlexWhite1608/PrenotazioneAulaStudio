import login
import setup
import prenotazione
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# inserire matricola e password
setup.matricola = input("Matricola: ")
setup.password = input("Password: ")

# apre il sito
setup.driver.get("https://kairos.unifi.it/portalePlanning/BIBL/login.php")

# fa il login con matricola e password
login.login()

try:
    pagina_principale = WebDriverWait(setup.driver, 10).until(
        EC.presence_of_element_located((By.ID, "titolo-pagina"))
    )

    prenotazione.gestione_prenotazioni()

except:
    print("Impossibile aprire pagina prenotazioni!")
# TODO: chiedere all'utente che azione svolgere (prenotazione/cancellazione/gestione prenotazioni)

'''
# aspetta che la pagina principale venga caricata
try:
    pagina_principale = WebDriverWait(setup.driver, 5).until(
        EC.presence_of_element_located((By.ID, "titolo-pagina"))
    )

    # esegue prenotazione per la mattina
    prenotazione.nuova_prenotazione("Mattina")

except:
    print("Finito Mattina")

try:
    pagina_principale = WebDriverWait(setup.driver, 5).until(
        EC.presence_of_element_located((By.ID, "titolo-pagina"))
    )

    # esegue prenotazione per il pomeriggio
    prenotazione.nuova_prenotazione("Pomeriggio")

except:
    print("Finito pomeriggio")

# finite le prenotazioni, chiude tutto
print("Tutte le prenotazioni sono state eseguite!")
setup.driver.quit()

'''
