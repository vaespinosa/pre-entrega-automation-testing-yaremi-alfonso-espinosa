"""
Funciones auxiliares para automatización de saucedemo.com
Cada función está documentada para facilitar el aprendizaje.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    """
    Realiza el login en saucedemo.com usando credenciales recibidas.
    Utiliza esperas explícitas para asegurar que los elementos estén disponibles antes de interactuar.
    Args:
        driver: instancia de WebDriver
        username: usuario para login
        password: contraseña para login
    """
    driver.get("https://www.saucedemo.com/")  # Navega a la página principal
    # Espera a que el campo de usuario sea visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(username)  # Ingresa el usuario
    driver.find_element(By.ID, "password").send_keys(password)   # Ingresa la contraseña
    driver.find_element(By.ID, "login-button").click()           # Hace clic en el botón de login
    # Espera a que la URL cambie a /inventory.html (login exitoso)
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

def get_first_product_info(driver):
    """
    Obtiene el nombre y precio del primer producto visible en el catálogo.
    Args:
        driver: instancia de WebDriver
    Returns:
        nombre (str), precio (str)
    """
    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio

def add_first_product_to_cart(driver):
    """
    Añade el primer producto del catálogo al carrito haciendo clic en el botón correspondiente.
    Args:
        driver: instancia de WebDriver
    """
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

def go_to_cart(driver):
    """
    Navega a la página del carrito de compras.
    Args:
        driver: instancia de WebDriver
    """
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def is_product_in_cart(driver, nombre):
    """
    Verifica si un producto con el nombre dado está presente en el carrito.
    Args:
        driver: instancia de WebDriver
        nombre: nombre del producto a buscar
    Returns:
        True si el producto está en el carrito, False si no
    """
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return any(nombre == p.text for p in productos)
