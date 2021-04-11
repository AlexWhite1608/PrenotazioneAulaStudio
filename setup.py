from selenium import webdriver

# imposta il chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# ignora gli errori ssl
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# definisce matricola e password
matricola = "7033449"
password = "Alessandro1"