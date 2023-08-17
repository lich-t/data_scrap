from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.goafricaonline.com/tg/annuaire/sante")

# Attendre le chargement complet de la page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME , "footer")))

domains = driver.find_elements(By.CSS_SELECTOR, "h3.text-16")

for domain in domains:
  section = domain.text
  print("DOMAINE :", section)
  domain.click()

  # Attendre le chargement dynamique des éléments
  hospitals = []
  while len(hospitals) < 1: # exemple de nombre attendu
    
    hospitals = driver.find_elements(By.CSS_SELECTOR, "h2.m-0")
    time.sleep(10)

  for hospital in hospitals:
  
    # récupérer les infos de l'hôpital

    name = hospital.text
    print("Nom:", name)

    hospital.click()

    address = driver.find_element(By.CSS_SELECTOR, "address.text-14").text
    print("Adresse :", address)

    phones = driver.find_elements(By.CSS_SELECTOR, "div.flex.text-16 span")
    for phone in phones:
      print("Téléphone:", phone.text)

    website = driver.find_element(By.CSS_SELECTOR, "div.flex.group a").get_attribute("href")
    print("Site web:", website)

    driver.back()
   
driver.quit()