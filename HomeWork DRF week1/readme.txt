
- Создаем виртуальное окружение python -m venv env
- Активируем виртуальное окружение env\Scripts\activate
- Устанавливаем зависимости pip install -r requirements.txt
- Запускаем проект -  python manage.py runserver
- Или запускаем start.bat для активации виртуального окружения и старта Django

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
- http://127.0.0.1:8000/stores/
    {
        "name": "Some name",
        "description": "Some description",
        "rating": 5
    }