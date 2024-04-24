import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyshadow.main import Shadow

class Llamados():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.shadow_driver = Shadow(driver)

    @staticmethod
    def _clean(text):
        text = text.replace('\n',' ')
        return text
    
    def summarize(self,text):
        prompt =  "Resume este texto, sin añadir nada más al output: " + self._clean(text)
        self.driver.get('https://www.llama2.ai/')

        time.sleep(2)
        textarea = self.driver.find_element(By.NAME,"prompt")
        textarea.send_keys(prompt)
        time.sleep(2)
        textarea.send_keys(Keys.ENTER)
        time.sleep(12)
        response = self.driver.find_element(By.TAG_NAME, "article").find_elements(By.XPATH, "./div")[-2].text[2:]
        return response