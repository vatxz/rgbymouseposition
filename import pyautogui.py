import pyautogui
import time

def get_mouse_info():
    # Obtiene la posición actual del mouse
    x, y = pyautogui.position()
    # Captura el color RGB del píxel en la posición del mouse
    rgb = pyautogui.screenshot().getpixel((x, y))
    return (x, y, rgb)

try:
    while True:
        x, y, rgb = get_mouse_info()
        print(f"Posición del mouse: ({x}, {y}) - Color RGB: {rgb}")
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada lectura
except KeyboardInterrupt:
    print("\nPrograma detenido.")

