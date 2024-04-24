import pytest
from llamados import Llamados

@pytest.fixture
def driver():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from pyshadow.main import Shadow
    from browser import create_browser
    return create_browser()

class TestLlamados:
    def test_summarize(self, driver):
        llamados = Llamados(driver)
        text = "Pytest es un marco de prueba de software que facilita la escritura y ejecución de pruebas en Python de manera sencilla y eficiente. Con Pytest, puedes escribir pruebas más legibles y mantenibles usando una sintaxis simple y expresiva. Permite la escritura de pruebas funcionales, de integración y unitarias con facilidad. Pytest también ofrece características como fixtures para la configuración del entorno de prueba, assertions para verificar resultados y mocks para simular comportamientos. Es altamente extensible, con una amplia variedad de complementos disponibles. Pytest es ampliamente utilizado en la comunidad de desarrollo de Python y es compatible con muchos marcos de prueba, lo que lo convierte en una opción popular para la escritura de pruebas en Python."
        summary = llamados.summarize(text)
        assert 0 < len(summary) < len(text)
        # Verificar que la respuesta sea coherente con el input

    def test_clean_text(self):
        text = "Este texto tiene\nlineas y espacios"
        cleaned_text = Llamados._clean(text)
        assert cleaned_text == "Este texto tiene lineas y espacios"