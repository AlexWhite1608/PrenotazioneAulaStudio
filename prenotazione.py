from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import setup
import time


def nuova_prenotazione(fascia_oraria):
    # apre il form di prenotazione
    setup.driver.find_element_by_id("form").click()
    mattina = Select(setup.driver.find_element_by_xpath('//*[@id="servizio"]'))
    mattina.select_by_visible_text("Prenotazione Posto Aula di Studio " + fascia_oraria)

    # apre il calendario
    time.sleep(0.5)
    setup.driver.find_element_by_id("data_inizio-form").click()

    # ciclo per selezionare i giorni dal calendario
    count = 0
    while count <= 11: # FIXME: capisci come ottimizzare il ciclo
        count += 1
        lista_giorni = setup.driver.find_element_by_xpath('//*[@id="data_inizio-container"]/div[3]/div[1]/table/tbody')
        giorni = lista_giorni.find_elements_by_tag_name("td")
        for giorno in giorni:
            classe_giorno = giorno.get_attribute("class")
            giorni_selezionati = []
            if classe_giorno == "day" or classe_giorno == "active.day" and giorni_selezionati.count(giorno.text) == 0:
                giorni_selezionati.append(giorno.text)
                giorno.click()
                break
        setup.driver.find_element_by_id("verify").click()

        # seleziona i giorni prenotabili dalla lista
        giorni_prenotabili = setup.driver.find_elements_by_css_selector(
            "[title=\"Clicca per visualizzare gli orari.\"]")

        for giorno_prenotabile in giorni_prenotabili:
            giorno_prenotabile.find_element_by_class_name("show-more").click()

            try:
                WebDriverWait(setup.driver, 0.2).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "[title=\"Clicca per prenotare!\"]"))
                )

                setup.driver.find_element_by_css_selector("[title=\"Clicca per prenotare!\"]").click()
                # TODO: stampa le informazioni della prenotazione
                setup.driver.find_element_by_id("conferma").click() # prenotazione eseguita!

                # torna indietro al form della prenotazione
                setup.driver.find_element_by_class_name("hamburger").click()
                time.sleep(0.5)
                setup.driver.find_element_by_class_name("nav")
                setup.driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/ul/li[2]/a').click()

                # riesegue tutto il ciclo andando a creare una nuova prenotazione
                ciclo_prenotazione(fascia_oraria)

            except:
                print("Giorno non disponibile")


def ciclo_prenotazione(fascia_oraria):
    mattina = Select(setup.driver.find_element_by_xpath('//*[@id="servizio"]'))
    mattina.select_by_visible_text("Prenotazione Posto Aula di Studio " + fascia_oraria)

    # apre il calendario
    time.sleep(0.5)
    setup.driver.find_element_by_id("data_inizio-form").click()

    # ciclo per selezionare i giorni dal calendario
    count = 0
    while count <= 11:  # FIXME: capisci come ottimizzare il ciclo
        count += 1
        lista_giorni = setup.driver.find_element_by_xpath('//*[@id="data_inizio-container"]/div[3]/div[1]/table/tbody')
        giorni = lista_giorni.find_elements_by_tag_name("td")
        for giorno in giorni:
            classe_giorno = giorno.get_attribute("class")
            giorni_selezionati = []
            if classe_giorno == "day" or classe_giorno == "active.day" and giorni_selezionati.count(giorno.text) == 0:
                giorni_selezionati.append(giorno.text)
                giorno.click()
                break
        setup.driver.find_element_by_id("verify").click()

        # seleziona i giorni prenotabili dalla lista
        giorni_prenotabili = setup.driver.find_elements_by_css_selector(
            "[title=\"Clicca per visualizzare gli orari.\"]")

        for giorno_prenotabile in giorni_prenotabili:
            giorno_prenotabile.find_element_by_class_name("show-more").click()

            try:
                WebDriverWait(setup.driver, 0.2).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "[title=\"Clicca per prenotare!\"]"))
                )

                setup.driver.find_element_by_css_selector("[title=\"Clicca per prenotare!\"]").click()
                # TODO: stampa le informazioni della prenotazione
                setup.driver.find_element_by_id("conferma").click()  # prenotazione eseguita!

                # torna indietro al form della prenotazione
                setup.driver.find_element_by_class_name("hamburger").click()
                time.sleep(0.5)
                setup.driver.find_element_by_class_name("nav")
                setup.driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/ul/li[2]/a').click()

                # riesegue tutto il ciclo andando a creare una nuova prenotazione
                ciclo_prenotazione(fascia_oraria)

            except:
                print("Giorno non disponibile")
