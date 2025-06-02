# Рабочий скрипт, который имитирует рандомное написание кода на python и движение мышки от Grok версия 2

import pyautogui
import random
import time
import keyboard

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
""",
        f"""
# Настройка мониторинга безопасности с {random.choice(tools)}
from prometheus_client import Counter, start_http_server
import time

security_violations = Counter('security_violations', 'Detected security issues', ['target'])
def monitor_{random.choice(targets).split()[0]}():
    start_http_server(8000)
    while True:
        security_violations.labels(target="{random.choice(targets)}").inc()
        time.sleep(60)
monitor_{random.choice(targets).split()[0]}()
""",
        f"""
# Развёртывание безопасного кластера K8s с {random.choice(tools)}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: secure
  template:
    metadata:
      labels:
        app: secure
    spec:
      containers:
      - name: app
        image: nginx:latest
        securityContext:
          runAsNonRoot: true
        ports:
        - containerPort: 80
""",
        f"""
# Сканирование уязвимостей {random.choice(targets)} с {random.choice(tools)}
import {random.choice(tools).lower()}
try:
    scan_result = {random.choice(tools).lower()}.scan(target="{random.choice(targets)}", platform="{random.choice(platforms)}")
    if scan_result.vulnerabilities:
        print(f"Обнаружены уязвимости в {{scan_result.target}} для {random.choice(compliance)}")
    else:
        print(f"Сканирование завершено, {random.choice(targets)} безопасны")
except Exception as e:
    print(f"Ошибка сканирования: {{e}}")
""",
        f"""
# Настройка политик безопасности с {random.choice(tools)}
resource "aws_iam_policy" "secure_policy" {{
  name = "secure_{random.choice(targets).split()[0]}_policy"
  policy = jsonencode({{
    Version = "2012-10-17",
    Statement = [
      {{
        Effect = "Allow",
        Action = ["{random.choice(targets).split()[0]}:Read"],
        Resource = "*"
      }}
    ]
  }})
}}
""",
        f"""
# Автоматизация {random.choice(targets)} через {random.choice(tools)}
from ansible_runner import Runner
playbook = "{random.choice(targets).split()[0]}_secure.yml"
Runner.run(playbook=playbook, inventory="{random.choice(platforms).lower()}-hosts")
print(f"{random.choice(actions).capitalize()} {random.choice(targets)} завершено для {random.choice(compliance)}")
""",
        f"""
# Интеграция {random.choice(tools)} с {random.choice(platforms)} для {random.choice(targets)}
from {random.choice(tools).lower()} import Client
client = Client(platform="{random.choice(platforms)}")
client.{random.choice(actions).lower()}(
    target="{random.choice(targets)}",
    compliance="{random.choice(compliance)}"
)
print(f"Интеграция {random.choice(targets)} завершена")
""",
        f"""
# Проверка compliance для {random.choice(targets)}
import {random.choice(tools).lower()}
def check_compliance():
    result = {random.choice(tools).lower()}.audit("{random.choice(targets)}")
    if result.passed:
        print(f"Соответствие {random.choice(compliance)} подтверждено")
    else:
        print(f"Нарушение {random.choice(compliance)} в {random.choice(targets)}")
check_compliance()
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