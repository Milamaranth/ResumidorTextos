from diario_de_sevilla import DiarioDeSevilla
from copilot import Copilot
from llamados import Llamados
from browser import create_browser
import logging

logging.basicConfig(level="INFO")

def main():
    driver = create_browser()
    news_site = DiarioDeSevilla(driver)
    copilot = Copilot(driver)
    llamados = Llamados(driver)

    news_site.go_local_news_page("Sevilla")
    links = news_site.extract_news_links()

    for link in links:
        title, text = news_site.extract_text(link)
        summary = llamados.summarize(text)
        persist(title, summary)

def persist(title, summary):
    file_name = "output/" + title + ".txt"
    with open(file_name,'w') as f:
        f.write(summary)

if __name__ == '__main__':
    main()
