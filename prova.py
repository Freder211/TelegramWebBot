browser = webdriver.Firefox() #crea il browser virtuale
browser.implicitly_wait(5) #aspetta ogni volta 5 secondi per il browser che carichi
browser.get('https://web.whatsapp.com/') #va sul link assegnato
xpath_prova = '//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div/div/div[1]' #xpath di prova
msg = browser.find_element_by_xpath(last_msg_xpath).get_attribute('innerHTML') #esempio di gettarsi un messaggio da xpath