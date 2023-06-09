# Рекомендательный сервис для выбора активностей участниками проекта "Московское долголетие"

Этот репозиторий содержит код и ресурсы для хакатона "Лидеры цифровой трансформации" 2023 для решения задачи "Рекомендательный сервис для выбора активностей участниками проекта «Московское Долголетие»"

Целью этого проекта является разработка сервиса, который поможет участникам проекта «Московское долголетие» получать индивидуальные подборки рекомендованных занятий, основанные на интересах и накопленных данных об их личном прогрессе.

## Живая демонстрация

Доступен на [сайте](http://178.170.194.84/).

## Ссылка на [файл результата работы модели](https://drive.google.com/file/d/1lW-YjyNuKRvPxnHdQks5clGSljdko2np/view?usp=sharing)

## Описание сервиса

1. На данном сервисе представлены 2 основных раздела: "Рекомендации" и "Поиск".
2. В разделе "Рекомендации" можно просмотреть занятия, которые рекомендованы на основе Ваших предпочтений и которые не похожи на группы, ранее посещенные пользователем. А также можно увидеть ограниченные предложения проекта «Московское долголетие».
3. В разделе "Поиск" можно найти занятия с помощью предложенной фильтрации и поисковой строки. Для большего удобства система предлагает пользователю занятия, которые могут понравиться именно ему.
4. Пользователь может выбрать интересующие его направление (физическая активность, образование, творчество и т.д.), формат, район и день проведения занятия.
5. Система предлагает занятия, которые могут точно заинтересовать пользователя.
6. Для опытной эксплуатации проекта был создан раздел "Личный кабинет". 
7. В личном кабинете можно увидеть какой пользователь выбран и информацию о нем, а именно его имя, адрес и история посещений. Представлена возможность сменить пользователя на случайного из портала "Московское долголетие" и добавить нового. При создании нового пользователя предлагается пройти тестирование, которое поможет подобрать рекомендации, подходящие именно ему.

## Репозиторий 

В данном репозитории представлен бек, фронт и сопроводительная документация проекта.
Бек расположен в папке "server", фронт в папке "client", python-ноутбуки и все ml-исследование в папке "research" . Для запуска системы локально клонируйте репозиторий на свой компьютер.

## BACKEND

### Стек технологий
1. python3.9
2. flask
3. sqlalchemy
4. sklearn surprise
5. sklearn
6. pandas
7. numpy
8. flask-sheduler

1. Скачать проект из репозитория
2. Убедиться, что на компьютере есть python3.9
3. Установить pip
4. Создать виртуальное окружение
5. Установить зависимости с помощью команды pip install requirements.txt
6. Запускаем сервер с помощью команды flask run run.py

### Развертывание приложения
1. Для запуска приложения должен быть установлен python3.9, pip.
2. Перейдите в папку проекта
```sh
cd server
```
3. Создайте виртуальное окружение в своей IDE.
4. Чтобы установить зависимости выполните команду:
```sh
pip install requirements.txt
```
5. Для запуска приложения выполните команду
```sh
flask run run.py
```
6. После запуска проект будет запущен по адресу http://127.0.0.1:5000/. Так же адрес будет указан в терминале.

## FRONTEND

### Стек технологий
1. html + css + js
2. vue + vite
3. axios
4. jquery
5. owl carousel

### Развертывание приложения
1. Для запуска приложения должен быть установлен Node.js версии 16.0 или выше.
2. Перейдите в папку проекта
```sh
cd client
```
3. Для установки всех необходимых зависимостей выполните команду:
```sh
npm install
```
4. Для запуска приложения в режиме разработки выполните команду:
```sh
npm run dev
```
5. После запуска проект будет запущен по адресу http://127.0.0.1:5173/. Так же адрес будет указан в терминале.
6. Для создания сборки проекта выполните команду:
```sh
npm run build
```
7. Сборка создастся в папке ./dist в каталоге проекта.
