import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging

class DiarioDeSevilla():
    def __init__(self, driver) -> None:
        self.driver = driver

    def go_local_news_page(self, provincia):
        # Abrir la página web de noticias
        self.driver.get("https://www.diariodesevilla.es/")
        
        # Esperar a que salga Aceptar y Continuar
        time.sleep(2)
        # Aceptar y continuar:
        aceptar = self.driver.find_element(By.LINK_TEXT, "Aceptar y continuar")
        aceptar.click()

        # Crear un objeto ActionChains
        action = ActionChains(self.driver)

        # Encontrar elemento y clickear:
        secciones = self.driver.find_element(By.XPATH,"//*[@id='nav']/ul/li[4]/a")
        # Mover el ratón sobre el elemento
        action.move_to_element(secciones).perform()
        # Esperar a que aparezca el menú flotante
        time.sleep(3)
        # Hacer clic en el elemento del menú flotante
        noticias_sevilla = self.driver.find_element(By.LINK_TEXT, provincia)
        noticias_sevilla.click()

    def extract_news_links(self):
        logging.info("Extracting news links")
        news_links = []
        for i in range(10):
            enlace = self.driver.find_element(By.XPATH, f"//*[@id='browse-target']/article[{i+1}]/h2/a")
            href = enlace.get_attribute('href')
            news_links.append(href)
        return news_links

    def extract_text(self,link):
        logging.info(f"Extracting article text from {link}")
        self.driver.get(link)
        # Esperar unos segundos para cargar la página de la noticia
        time.sleep(2)
        # Obtener el texto de la página
        article_elem = self.driver.find_element(By.TAG_NAME,'article')
        article_body = article_elem.find_element(By.CSS_SELECTOR, "div[itemprop='articleBody']")
        no_ads = "\n".join([p.text for p in article_body.find_elements(By.TAG_NAME, "p")])
        logging.info(f"Article text length {len(no_ads)}")
        title = article_elem.find_element(By.TAG_NAME, "h1").text
        return title, no_ads
