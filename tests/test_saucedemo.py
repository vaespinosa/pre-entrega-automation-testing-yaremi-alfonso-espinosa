"""
Tests automatizados para saucedemo.com
Cada test está documentado para facilitar el aprendizaje.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.saucedemo_utils import login, get_first_product_info, add_first_product_to_cart, go_to_cart, is_product_in_cart
import os
import time

@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture de Pytest que inicializa el navegador Chrome y lo maximiza.
    Si el test falla, toma una captura de pantalla y la guarda en reports/assets/.
    Al finalizar, cierra el navegador.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    def fin():
        # Si el test falla, tomar captura
        rep_call = getattr(request.node, 'rep_call', None)
        if rep_call and rep_call.failed:
            test_name = request.node.name
            screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'reports', 'assets')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
            driver.save_screenshot(screenshot_path)
    request.addfinalizer(fin)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest para obtener el resultado de cada fase del test (setup, call, teardown).
    Permite saber si el test falló y así tomar la captura en el fixture.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Test 1: Login automatizado
def test_login(driver):
    time.sleep(2)  # Espera para observar el login
    """
    Test de login en saucedemo.com
    - Ingresa credenciales válidas
    - Valida que la URL sea /inventory.html
    - Valida que el título sea 'Swag Labs'
    """
    login(driver, "standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title

# Test 2: Verificación de catálogo
def test_catalogo(driver):
    time.sleep(2)  # Espera para observar el catálogo
    """
    Test de navegación y verificación del catálogo
    - Valida el título de la página
    - Verifica que hay productos visibles
    - Valida presencia de menú y filtros
    - Lista nombre y precio del primer producto
    """
    login(driver, "standard_user", "secret_sauce")
    assert "Swag Labs" in driver.title
    nombre, precio = get_first_product_info(driver)
    assert nombre != ""  # Verifica que hay al menos un producto
    assert precio != ""
    assert driver.find_element(By.ID, "react-burger-menu-btn")  # Menú hamburguesa
    assert driver.find_element(By.CLASS_NAME, "product_sort_container")  # Filtros

# Test 3: Interacción con productos y carrito
def test_carrito(driver):
    time.sleep(2)  # Espera para observar el proceso de agregar al carrito
    """
    Test de interacción con productos y carrito
    - Agrega el primer producto al carrito
    - Verifica que el contador del carrito se incrementa
    - Navega al carrito y valida que el producto está presente
    """
    login(driver, "standard_user", "secret_sauce")
    nombre, precio = get_first_product_info(driver)
    add_first_product_to_cart(driver)
    cart_badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1"  # El contador debe mostrar 1
    go_to_cart(driver)
    assert is_product_in_cart(driver, nombre)  # El producto debe estar en el carrito
