# Рабочий скрипт, который имитирует рандомное написание кода на python и движение мышки от ChatGPT

import pyautogui
import random
import time
import keyboard

def generate_random_python_code():
    code_snippets = [
        # CI/CD запуск пайплайна и контроль состояний
        """import subprocess
result = subprocess.run(['git', 'pull'], capture_output=True)
if result.returncode == 0:
    print('Codebase updated, triggering pipeline...')
    subprocess.run(['gitlab-runner', 'exec', 'shell', 'deploy-pipeline'])
else:
    print('Git pull failed:', result.stderr.decode())""",

        # Проверка контейнера на уязвимости с выводом отчёта
        """import os
image = 'backend-service:latest'
print(f'🔍 Scanning {image} for vulnerabilities...')
os.system(f'trivy image --severity HIGH,CRITICAL {image}')""",

        # Prometheus + PushGateway логирование метрик
        """import requests
metrics = 'deployment_status{env="prod",app="auth"} 1\n'
resp = requests.post('http://localhost:9091/metrics/job/deployment', data=metrics)
print('Metrics pushed:', resp.status_code)""",

        # Контроль доступа на основе ролей
        """def has_permission(user):
    allowed_roles = {'devops', 'security', 'sre'}
    if user.get('role') not in allowed_roles:
        raise PermissionError(f"User {user['name']} is not authorized")
    return True
has_permission({'name': 'Ivan', 'role': 'security'})""",

        # Мониторинг ресурсов сервера
        """import psutil
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
if cpu > 80 or mem > 90:
    print(f'⚠️ High resource usage! CPU: {cpu}%, Memory: {mem}%')""",

        # Валидация инфраструктуры как кода (IaC) через Terraform
        """import subprocess
print('📦 Validating Terraform configuration...')
subprocess.run(['terraform', 'init', '-backend=false'])
subprocess.run(['terraform', 'validate'])""",

        # Проверка зависимостей на уязвимости
        """import subprocess
print('🔒 Scanning dependencies with Snyk...')
subprocess.run(['snyk', 'test', '--file=requirements.txt'])""",

        # Обработка алертов и уведомлений
        """import smtplib
def send_alert(subject, body):
    msg = f'Subject: {subject}\n\n{body}'
    server = smtplib.SMTP('smtp.internal', 25)
    server.sendmail('devsecops@corp.local', 'oncall@corp.local', msg)
send_alert('🔥 PROD incident', 'Alert: Pod crashloop in namespace prod-auth')""",

        # Чтение и валидация конфигурации из YAML
        """import yaml
with open('deployment.yaml') as f:
    cfg = yaml.safe_load(f)
if cfg.get('replicas', 0) < 2:
    print('⚠️ Warning: Low replica count')""",

        # Docker: мониторинг состояния контейнеров
        """import docker
client = docker.from_env()
for container in client.containers.list():
    print(f'🟢 {container.name} | Status: {container.status}')"""
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
    if random_x < editor_top_left[0]:
        random_x = editor_top_left[0]
    elif random_x > editor_bottom_right[0]:
        random_x = editor_bottom_right[0]

    if random_y < editor_top_left[1]:
        random_y = editor_top_left[1]
    elif random_y > editor_bottom_right[1]:
        random_y = editor_bottom_right[1]

    # Генерация случайного Python-кода
    random_code = generate_random_python_code()

    # Список действий
    actions = [
        lambda: human_like_mouse_move(random_x, random_y, 0.5),
        lambda: pyautogui.click(),
        lambda: pyautogui.write(random_code, interval=0.1),
        lambda: time.sleep(2),
        lambda: [pyautogui.press('backspace') for _ in range(random.randint(1, len(random_code)))],
        lambda: pyautogui.scroll(random.randint(100, 500)),
        lambda: time.sleep(1),
        lambda: pyautogui.scroll(random.randint(100, 500) * -1),
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

