browser = webdriver.Firefox() #crea il browser virtuale
browser.implicitly_wait(5) #aspetta ogni volta 5 secondi per il browser che carichi
browser.get('https://web.telegram.org/') #va sul link assegnato

if browser.current_url=="https://web.telegram.org/#/login":
    tel = "3347799058"
    path_telefono = "//*[@id=\"ng-app\"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input"
    input_tel=browser.find_element_by_xpath(path_telefono)
    input_tel.click
    input_tel.send_keys(tel)

    path_avanti = "/html/body/div[1]/div/div[2]/div[1]/div/a"
    avanti = browser.find_element_by_xpath(path_avanti)
    avanti.click

#xpath_prova = '//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div/div/div[1]' #xpath di prova
#msg = browser.find_element_by_xpath(last_msg_xpath).get_attribute('innerHTML') #esempio di gettarsi un messaggio da xpath