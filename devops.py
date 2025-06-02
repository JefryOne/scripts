'''В скрипт добавлен рандомный текст из сферы devsecops'''


import pyautogui
import random
import time
import keyboard

def generate_random_devsecops_code():
    # Списки терминов и шаблонов, характерных для DevSecOps
    tools = ["Jenkins", "GitLab CI", "CircleCI", "Docker", "Kubernetes", "Terraform", "Ansible", "Snyk", "OWASP ZAP", "SonarQube"]
    actions = ["внедряем", "настраиваем", "автоматизируем", "сканируем", "оптимизируем", "разворачиваем", "проводим аудит"]
    targets = ["CI/CD пайплайн", "контейнеры", "уязвимости", "инфраструктуру", "IAM политики", "код", "сеть"]
    outcomes = ["для повышения безопасности", "для ускорения деплоя", "для соответствия стандартам", "для минимизации рисков"]

    # Шаблоны кода и конфигураций, связанных с DevSecOps
    code_snippets = [
        f"""
# Настройка {random.choice(tools)} для {random.choice(targets)}
def configure_pipeline():
    print("{random.choice(actions).capitalize()} {random.choice(targets)} {random.choice(outcomes)}")
    # Пример: запуск сканирования
    import {random.choice(tools).lower()}
    {random.choice(tools).lower()}.run_scan()
""",
        f"""
# Автоматизация {random.choice(targets)} с помощью {random.choice(tools)}
stages:
  - build
  - test
  - deploy
security_scan:
  script:
    - echo "{random.choice(actions).capitalize()} {random.choice(targets)}"
    - {random.choice(tools).lower()} scan --full
""",
        f"""
# Скрипт для {random.choice(actions)} {random.choice(targets)}
import os
os.system("{random.choice(tools).lower()} --check {random.choice(targets)}")
print("Завершено: {random.choice(outcomes)}")
""",
        f"""
# Конфигурация {random.choice(tools)} для {random.choice(targets)}
resource "{random.choice(targets).replace(' ', '_')}" "example" {{
  provider = "{random.choice(tools).lower()}"
  name = "secure_{random.choice(targets).split()[0]}"
}}
""",
        f"""
# Автоматизация проверки безопасности
from {random.choice(tools).lower()} import Scanner
scanner = Scanner()
scanner.{random.choice(actions).lower()}("{random.choice(targets)}")
print("{random.choice(outcomes).capitalize()}")
""",
        f"""
# Проверка уязвимостей с помощью {random.choice(tools)}
import {random.choice(tools).lower()}
try:
    {random.choice(tools).lower()}.scan("{random.choice(targets)}")
except SecurityError:
    print("Обнаружены уязвимости в {random.choice(targets)}")
""",
        f"""
# Деплой {random.choice(targets)} с {random.choice(tools)}
kubectl apply -f deployment.yaml
print("{random.choice(actions).capitalize()} {random.choice(targets)} {random.choice(outcomes)}")
""",
        f"""
# Настройка мониторинга безопасности
from {random.choice(tools).lower()} import Monitor
monitor = Monitor()
monitor.{random.choice(actions).lower()}("{random.choice(targets)}")
print("Мониторинг {random.choice(targets)} активирован")
""",
        f"""
# Автоматизация {random.choice(targets)} через {random.choice(tools)}
ansible-playbook secure_{random.choice(targets).split()[0]}.yml
print("{random.choice(actions).capitalize()} {random.choice(targets)} завершено")
""",
        f"""
# Проверка соответствия стандартам
import {random.choice(tools).lower()}
{random.choice(tools).lower()}.compliance_check()
print("{random.choice(outcomes).capitalize()}")
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

current_line = 0

while time.time() < end_time:
    if keyboard.is_pressed('q'):  # Нажмите 'q' для выхода
        print("Скрипт остановлен пользователем.")
        break

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