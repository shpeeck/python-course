
- Создаем виртуальное окружение python -m venv env
- Активируем виртуальное окружение env\Scripts\activate
- Устанавливаем зависимости pip install -r requirements.txt
- Запускаем проект -  python manage.py runserver
- Или запускаем start.bat для активации виртуального окружения и старта Django

--------------------------------
HomeWork1

endpoints:
- http://127.0.0.1:8000/today/
- http://127.0.0.1:8000/hello_world/
- http://127.0.0.1:8000/my_name/?name=Joe%20Satriani
- http://127.0.0.1:8000/calculator/
    {
        "action": "minus",
        "number1": 10,
        "number2": 5
    }
    {
        "action": "plus",
        "number1": 10,
        "number2": 5
    }
    {
        "action": "divide",
        "number1": 10,
        "number2": 5
    }
    {
        "action": "multiply",
        "number1": 10,
        "number2": 5
    }
- http://127.0.0.1:8000/stores-old/
    {
        "name": "Some name",
        "description": "Some description",
        "rating": 5
    }


--------------------------------
HomeWork2

- юзер и токен 
    python manage.py shell
    from rest_framework.authtoken.models import Token
    from django.contrib.auth.models import User
    User.objects.all()
    t = Token.objects.all()
    user = User.objects.create(username='John Doe')
    token = Token.objects.create(user=user)

    token = af6289d26c4c196a87d5dc64b3a245179ca70c7b


endpoints:
- http://127.0.0.1:8000/stores/ ALL TORES
- http://127.0.0.1:8000/stores/1/ ONE STORE
- http://127.0.0.1:8000/my_stores/ ALL STORES AUTORIZED USER
- http://127.0.0.1:8000/my_stores/1/ PUT
- http://127.0.0.1:8000/my_stores/10/mark_as_active/
- http://127.0.0.1:8000/my_stores/10/mark_as_deactivated/

- admin и токен 
    python manage.py shell
    from rest_framework.authtoken.models import Token
    from django.contrib.auth.models import User
    user = User.objects.create(username='John NotDoe')
    token = Token.objects.create(user=user)
    -----
    user = User.objects.get(username="John NotDoe")
    user.is_staff = True
    user.save()

    token = bd5e34b499e009eb03aadc91e224e4dbef77e5e3

endpoints
- http://127.0.0.1:8000/admin_stores/
- http://127.0.0.1:8000/admin_stores/1/
- http://127.0.0.1:8000/admin_stores/?status=in_review
- http://127.0.0.1:8000/admin_stores/?search=Some
- http://127.0.0.1:8000/admin_stores/1/mark_as_active/
