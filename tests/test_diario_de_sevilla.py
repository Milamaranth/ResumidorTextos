import pytest
from diario_de_sevilla import DiarioDeSevilla

@pytest.fixture
def driver():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from browser import create_browser
    return create_browser()

def test_go_local_news_page(driver):
    news_site = DiarioDeSevilla(driver)
    news_site.go_local_news_page("Sevilla")
    assert driver.current_url == 'https://www.diariodesevilla.es/sevilla/'

def test_extract_local_news_links(driver):
    news_site = DiarioDeSevilla(driver)
    news_site.go_local_news_page("Sevilla")
    links = news_site.extract_news_links()
    assert len(links) == 10
