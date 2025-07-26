# 🧠 Flask User Auth App

Веб-приложение на Flask с поддержкой:

- ✅ Регистрации пользователей  
- ✅ Авторизации и выхода из аккаунта  
- ✅ Редактирования профиля (имя, email, пароль)  
- ✅ Валидации форм и флеш-сообщений  
- ✅ CSRF-защиты через Flask-WTF

---

## 📁 Структура проекта

```
VD07/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── register.html
│       ├── login.html
│       └── account.html
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Установка

1. Клонируй проект:

    ```bash
    git clone https://github.com/your-username/VD07.git
    cd VD07
    ```

2. Создай виртуальное окружение:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3. Установи зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запусти сервер:

    ```bash
    python main.py
    ```

---

## 🚀 Использование

Открой в браузере: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Основные маршруты:

- 🔐 `/register` — регистрация нового пользователя  
- 🔑 `/login` — вход в систему  
- 👤 `/account` — редактирование профиля (только после входа)  
- 🚪 `/logout` — выход из аккаунта  

---

## 🧾 Используемые технологии

- `Flask`
- `Flask-WTF`
- `Flask-Login`
- `Flask-Bcrypt`
- `SQLite` (можно заменить на PostgreSQL или MySQL)

---

## ✅ Идеи для доработки

- [ ] Добавить загрузку аватарки  
- [ ] Реализовать восстановление пароля  
- [ ] Добавить подтверждение email  
- [ ] Сделать адаптивный дизайн через Bootstrap

---

## 👨‍💻 Автор

Сделано [SergeyTatarintcev](https://github.com/SergeyTatarintcev)
