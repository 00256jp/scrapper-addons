from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("?? Iniciando o Web Scraper Add-on...")

try:
    # Configurações do Chrome headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Inicializar o navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # URL do login
    login_url = "https://www.exemplo.com/login"
    driver.get(login_url)
    print("?? Página de login carregada.")

    # Preencher os campos de login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("seu_usuario")
    password_field.send_keys("sua_senha")
    password_field.submit()

    # Esperar a página carregar
    time.sleep(5)
    print("?? Login realizado com sucesso.")

    # Página de dados
    data_url = "https://www.exemplo.com/dados"
    driver.get(data_url)
    print("?? Página de dados carregada.")

    # Extrair dados
    dados = driver.find_elements(By.CLASS_NAME, "classe-dados")
    for dado in dados:
        print("?? Dado extraído:", dado.text)

    # Encerrar o navegador
    driver.quit()
    print("? Scraper finalizado com sucesso!")

except Exception as e:
    print("? Erro durante a execução:", e)
