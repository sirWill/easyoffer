<h1 align="center"> 👾 easyoffer </h1>

[easyoffer.ru](https://easyoffer.ru) - набор инструментов, что проще трудоустроиться в IT



## Описание
- analytic (требования) - работа с API HeadHunter, парсинг данных по заданным поисковым запросам и анлиз частотности технологий. Для работы с API вам потребуется [зарегистрировать приложение HeadHuner](https://dev.hh.ru/)
- mentor - создание / редактирование / публикация ментора, отзывы
- rating - вопросы с собесов, ответы на них, вероятность встречи, ссылки и моки
- access - выдает / забирает полный доступ к сайту. Доступ по ссылке выдается через [телеграм бота](https://easyoffer.ru)

## Установка
Создайте и запустите виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
Соберите проект в Docker
```
docker compose up --build
```

## Обратная связь
Сайт сделан в учебных целях, на нем много ошибок, буду благодарен за любой фидбэк по коду и его улучшению. Напишите мне в [телегу](https://t.me/kivaiko)