import login
import setup
import prenotazione
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# apre il sito
setup.driver.get("https://kairos.unifi.it/portalePlanning/BIBL/login.php")

# fa il login con matricola e password
login.login()

# aspetta che la pagina principale venga caricata
try:
    pagina_principale = WebDriverWait(setup.driver, 5).until(
        EC.presence_of_element_located((By.ID, "titolo-pagina"))
    )

    # esegue prenotazione
    prenotazione.nuova_prenotazione("Mattina")

except:
    #setup.driver.quit()
    print("ASPETTA")

#driver.quit()
