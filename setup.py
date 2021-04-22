from selenium import webdriver

# ignora gli errori ssl
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# imposta il chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)
driver.minimize_window()

'''
# definisce matricola e password
matricola = "7033449"
password = "Alessandro1"
'''


