import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuración de tus Sitios de InfinityFree ---
SITIOS = {
    "anime": {
        "url": "https://inventarioncc.infinityfreeapp.com/Anime/Calificaciones/calificaciones.php",
        "img_path": "./Imagenes/anime.jpg"
    },
    "mangas": {
        "url": "https://inventarioncc.infinityfreeapp.com/Manga/Calificaciones/calificaciones.php",
        "img_path": "./Imagenes/mangas.jpg"
    },
    "series": {
        "url": "https://inventarioncc.infinityfreeapp.com/Series/Calificaciones/calificaciones.php",
        "img_path": "./Imagenes/series.jpg"
    }
}


def tomar_capturas():
    # Configurar Selenium Headless (sin interfaz gráfica para que corra en el servidor de GitHub)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "--window-size=1280,720")  # Proporción 16:9 ideal

    #service = Service(executable_path=r"C:\chromedriver.exe")
    
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    os.makedirs("./Imagenes", exist_ok=True)

    try:
        for nombre, info in SITIOS.items():
            print(f"Abriendo {nombre}...")
            driver.get(info["url"])

            # Esperamos 6 segundos para asegurar que carguen estilos, base de datos e imágenes
            time.sleep(6)

            driver.save_screenshot(info["img_path"])
            print(f"✓ Captura de {nombre} guardada con éxito.")

    finally:
        driver.quit()


if __name__ == "__main__":
    tomar_capturas()
