from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from progress.bar import Bar
import os
import setup
import time


def nuova_prenotazione(fascia_oraria):
    # apre il form di prenotazione
    setup.driver.find_element_by_id("form").click()
    time.sleep(0.2)

    # inizia il ciclo delle prenotazioni
    ciclo_prenotazione(fascia_oraria)


def ciclo_prenotazione(fascia_oraria):
    # seleziona la fascia oraria
    fascia = Select(setup.driver.find_element_by_xpath('//*[@id="servizio"]'))
    fascia.select_by_visible_text("Prenotazione Posto Aula di Studio " + fascia_oraria)

    # seleziona l'edificio
    edificio = Select(setup.driver.find_element_by_xpath('//*[@id="area"]'))
    edificio.select_by_visible_text("Sala Studio Edificio D14 Campus Novoli")

    # apre il calendario
    time.sleep(0.5)
    setup.driver.find_element_by_id("data_inizio-form").click()

    # ciclo per selezionare i giorni dal calendario
    count = 0
    while count <= 11:
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

        # apre anche i giorni successivi
        setup.driver.find_element_by_id("load_next").click()
        time.sleep(2)
        setup.driver.find_element_by_id("load_next").click()

        # seleziona i giorni prenotabili dalla lista
        giorni_prenotabili = setup.driver.find_elements_by_css_selector(
            "[title=\"Clicca per visualizzare gli orari.\"]")

        for giorno_prenotabile in giorni_prenotabili:
            giorno_prenotabile.find_element_by_class_name("show-more").click()

            # apre soltanto i giorni che sono prenotabili ed esegue la prenotazione
            try:
                WebDriverWait(setup.driver, 2).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "[title=\"Clicca per prenotare!\"]"))
                )

                time.sleep(1)
                setup.driver.find_element_by_css_selector("[title=\"Clicca per prenotare!\"]").click()

                # stampa informazioni prenotazione
                info_prenotazione()

                # prenotazione eseguita!
                setup.driver.find_element_by_id("conferma").click()

                # torna indietro al form della prenotazione
                setup.driver.find_element_by_class_name("hamburger").click()
                time.sleep(0.5)
                setup.driver.find_element_by_class_name("nav")
                setup.driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/ul/li[2]/a').click()

                # riesegue tutto il ciclo andando a creare una nuova prenotazione fino a quando si esauriscono i giorni
                ciclo_prenotazione(fascia_oraria)

            except:
                # se il giorno non è disponibile
                pass

        # torna alla pagina principale
        setup.driver.find_element_by_class_name("hamburger").click()
        time.sleep(0.5)
        setup.driver.find_element_by_class_name("nav")
        setup.driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/ul/li[1]/a').click()


def info_prenotazione():
    informazioni = setup.driver.find_elements_by_class_name("col-sm-6")

    for informazione in informazioni:
        if 'Sportello: ' in informazione.text:
            print("\n\n" + informazione.text + "\n")


def gestione_prenotazioni():
    # apre la pagina contenente tutte le prenotazioni
    setup.driver.find_element_by_id("mybookings").click()

    # aspetta il caricamento della pagina
    # TODO: implementa progressbar per il caricamento
    try:
        WebDriverWait(setup.driver, 15).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "col-xs-12"))
        )
    except NoSuchElementException:
        print("Pagina non caricata")

    counter = 0
    tabella = setup.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/table')
    body = tabella.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/table/tbody')
    prenotazioni = body.find_elements_by_tag_name('tr')

    os.system('cls')
    for prenotazione in prenotazioni:
        if counter < 16:
            print("\n" + prenotazione.text[34:-21] + "\n")  # FIXME: togli magic numbers

        counter += 1
