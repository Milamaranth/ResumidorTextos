from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from browser import create_browser
from llamados import Llamados

scenarios("../feature/llamados.feature")

@given(parsers.parse('I have a text'), target_fixture="text")
def given_text():
    return  "Pytest es un marco de prueba de software que facilita la escritura y ejecución de pruebas en Python de manera sencilla y eficiente. Con Pytest, puedes escribir pruebas más legibles y mantenibles usando una sintaxis simple y expresiva. Permite la escritura de pruebas funcionales, de integración y unitarias con facilidad. Pytest también ofrece características como fixtures para la configuración del entorno de prueba, assertions para verificar resultados y mocks para simular comportamientos. Es altamente extensible, con una amplia variedad de complementos disponibles. Pytest es ampliamente utilizado en la comunidad de desarrollo de Python y es compatible con muchos marcos de prueba, lo que lo convierte en una opción popular para la escritura de pruebas en Python."

@when('I send the text to Llamados for summarization', target_fixture="summary")
def when_send_llamados(text):
    driver = create_browser()
    llamados = Llamados(driver)
    return llamados.summarize(text)

@then('the response should be a summary of the original text')
def then_summary(text, summary):
    assert 0 < len(summary) < len(text)