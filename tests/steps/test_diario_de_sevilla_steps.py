from diario_de_sevilla import DiarioDeSevilla
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from browser import create_browser

scenarios("../feature/diario_de_sevilla.feature")
@given('I have created an instance of DiarioDeSevilla with a browser driver', target_fixture="news_site")
def given_instance():
    return DiarioDeSevilla(create_browser())

@when('I call go_local_news_page("Sevilla")')
def click_menu(news_site):
    news_site.go_local_news_page("Sevilla")

@then('I should be taken to the local news page')
def go_local(news_site):
    assert news_site.driver.current_url == 'https://www.diariodesevilla.es/sevilla/'