import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docegla.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

print("Verificando criação de superusuário...")

if not username or not email or not password:
    print("Variáveis do superusuário não definidas corretamente.")
else:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("Superusuário criado com sucesso!")
    else:
        print("Superusuário já existe.")