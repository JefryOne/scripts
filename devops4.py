import pyautogui
import random
import time
import keyboard
import psutil
import win32gui  # Для Windows, для мониторинга активного окна
import win32process
import sys

def get_active_window_title():
    """Получает заголовок активного окна (Windows)."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(hwnd)
    except:
        return ""

def get_active_process_id():
    """Получает ID процесса активного окна (Windows)."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return pid
    except:
        return None

def get_running_processes():
    """Получает список текущих процессов."""
    return set(p.pid for p in psutil.process_iter())

def generate_random_devsecops_code():
    # Списки терминов для senior DevSecOps
    tools = ["Terraform", "Kubernetes", "Helm", "Vault", "GitLab CI", "Jenkins", "Snyk", "Aqua Security", "Prometheus", "Falco", "AWS IAM", "Azure AD"]
    platforms = ["AWS", "Azure", "GCP", "on-premises"]
    targets = ["контейнеры", "кластер K8s", "IAM политики", "CI/CD пайплайн", "secrets", "сеть", "код", "инфраструктуру"]
    compliance = ["CIS", "NIST", "SOC2", "GDPR", "ISO 27001"]
    actions = ["автоматизируем", "сканируем", "настраиваем", "аудитим", "оптимизируем", "разворачиваем", "шифруем"]

    # Шаблоны кода для senior DevSecOps
    code_snippets = [
        f"""
# Настройка {random.choice(tools)} для безопасного деплоя на {random.choice(platforms)}
resource "aws_security_group" "secure_app" {{
  name = "secure_{random.choice(targets).split()[0]}_sg"
  ingress {{
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }}
  tags = {{
    Compliance = "{random.choice(compliance)}"
  }}
}}
output "sg_id" {{
  value = aws_security_group.secure_app.id
}}
""",
        f"""
# Автоматизация ротации секретов с {random.choice(tools)}
from vault import VaultClient
import time

def rotate_secrets():
    client = VaultClient("{random.choice(platforms).lower()}-vault")
    secrets = client.list_secrets("{random.choice(targets).split()[0]}")
    for secret in secrets:
        client.rotate_secret(secret)
        print(f"Ротация секрета {{secret}} завершена {random.choice(compliance)}")
rotate_secrets()
""",
        f"""
# Конфигурация {random.choice(tools)} для {random.choice(targets)} в {random.choice(platforms)}
stages:
  - security_scan
  - build
  - deploy
security_scan:
  image: {random.choice(tools).lower()}:latest
  script:
    - echo "{random.choice(actions).capitalize()} {random.choice(targets)} для {random.choice(compliance)}"
    - {random.choice(tools).lower()} scan --severity high
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
"""
    ]
    return random.choice(code_snippets)

def human_like_mouse_move(x, y, duration):
    start_x, start_y = pyautogui.position()
    steps = int(duration * 100)
    
    for i in range(steps):
        current_x = start_x + (x - start_x) * (i / steps) + random.uniform(-1, 1)
        current_y = start_y + (y - start_y) * (i / steps) + random.uniform(-1, 1)
        pyautogui.moveTo(current_x, current_y)
        time.sleep(duration / steps)

# Длительность в секундах для выполнения скрипта (8 часов)
duration = 8 * 60 * 60
end_time = time.time() + duration

# Настройте координаты начальной строки и высоту строки
line_start_position = (399, 78)  # Пример координат, замените на ваши
line_height = 20  # Высота строки в пикселях, настройте под ваш VS Code

# Границы окна редактора
editor_top_left = (490, 180)
editor_bottom_left = (488, 298)
editor_top_right = (735, 186)
editor_bottom_right = (751, 279)

# Начальные параметры для отслеживания
initial_window_title = get_active_window_title()  # Заголовок окна редактора
initial_pid = get_active_process_id()  # PID редактора
initial_processes = get_running_processes()  # Начальный список процессов
editor_name = "Visual Studio Code"  # Укажите имя редактора (например, "Visual Studio Code")

current_line = 0

while time.time() < end_time:
    # Проверка нажатия 'q' для выхода
    if keyboard.is_pressed('q'):
        print("Скрипт остановлен пользователем.")
        break

    # Проверка горячих клавиш для переключения вкладок или окон
    if keyboard.is_pressed('alt+tab') or keyboard.is_pressed('ctrl+tab'):
        print("Обнаружено переключение окон или вкладок. Скрипт остановлен.")
        sys.exit()

    # Проверка активного окна
    current_window_title = get_active_window_title()
    if editor_name not in current_window_title or current_window_title != initial_window_title:
        print("Обнаружено новое окно или переключение. Скрипт остановлен.")
        sys.exit()

    # Проверка нового процесса
    current_processes = get_running_processes()
    new_processes = current_processes - initial_processes
    if new_processes:
        print(f"Обнаружены новые процессы: {new_processes}. Скрипт остановлен.")
        sys.exit()

    # Проверка, что активное окно принадлежит тому же процессу
    current_pid = get_active_process_id()
    if current_pid != initial_pid:
        print("Активное окно принадлежит другому процессу. Скрипт остановлен.")
        sys.exit()

    # Генерация случайных координат в пределах окна редактора
    random_x = random.randint(editor_top_left[0], editor_bottom_right[0])
    random_y = random.randint(editor_top_left[1], editor_bottom_right[1])

    # Проверка, чтобы координаты не выходили за границы
    random_x = max(editor_top_left[0], min(random_x, editor_bottom_right[0]))
    random_y = max(editor_top_left[1], min(random_y, editor_bottom_right[1]))

    # Генерация случайного DevSecOps-кода
    random_code = generate_random_devsecops_code()

    # Список действий
    actions = [
        lambda: human_like_mouse_move(random_x, random_y, 0.5),
        lambda: pyautogui.click(),
        lambda: pyautogui.write(random_code, interval=0.1),
        lambda: time.sleep(2),
        lambda: [pyautogui.press('backspace') for _ in range(random.randint(1, len(random_code)))],
        lambda: pyautogui.scroll(random.randint(100, 500)),  # Прокрутка вверх
        lambda: time.sleep(1),
        lambda: pyautogui.scroll(random.randint(100, 500) * -1),  # Прокрутка вниз
        lambda: time.sleep(random.uniform(0.5, 1.5))
    ]

    # Перемешивание списка действий
    random.shuffle(actions)

    # Выполнение действий в случайном порядке
    for action in actions:
        action()

    # Перемещение к следующей строке
    current_line += 1

    # Если достигнута десятая строка, вернуться на первую строку
    if current_line >= 10:
        current_line = 0