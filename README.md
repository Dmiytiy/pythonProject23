# Простое веб-приложение для отображения информации о кандидатах
Этот проект представляет собой простое веб-приложение, которое отображает информацию о кандидатах на вакансии. Приложение создано с использованием Flask и предоставляет пользователю возможность просматривать профили кандидатов, а также фильтровать их по навыкам.
Откройте браузер и перейдите по адресу http://localhost:5000/, чтобы увидеть список доступных кандидатов.

Вы можете выбрать конкретного кандидата, перейдя на его профиль по ссылке http://localhost:5000/candidate/<id>, где <id> - это идентификатор кандидата.

Вы также можете просмотреть кандидатов с определенными навыками, перейдя по ссылке http://localhost:5000/skills/<skill>, где <skill> - это навык, по которому вы хотите фильтровать кандидатов.

Структура проекта
main.py: Главный файл приложения, который создает экземпляр Flask и определяет маршруты для отображения списка кандидатов, профиля кандидата и кандидатов с определенными навыками.
utils.py: Модуль для загрузки данных о кандидатах из JSON-файла.
