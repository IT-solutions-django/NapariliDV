# Напарили ДВ

Сайт для строительной компании Напарили ДВ

## О проекте 

Сайт создан для получения консультаций, строительства и сдачи современных каркасных домов. Пользователи могут ознакомиться с проектами компании, фильтровать проекты по таким параметрам, как материал, категория, тип кровли, цена, площадь и так далее. По каждому проекту можно получить подробную информацию и фотографии.

## Стек технологий 

Django, Sqlite, Redis, Celery, Nginx.

## Приложения 

### Приложение home 

Отвечает за главную страницу сайта и всё, с ней связанное. 

Модели: 
- Slide - Слайд. Хранит информацию, которая должна отображаться на слайдах на главной странице
- CompanyInfo - Информация о компании (синглтон). Хранит описание, историю, адрес и другие данные о компании, в том числе факты, предоставляемые услуги и преимущества.
- PrivacyPolicy - Политика конфиденциальности (синглтон). Хранит текст документа с политикой конфиденциальности компании.
- PopularQuestion - Часто задаваемые вопросы. Хранит сами вопросы и ответы на них.
- CooperationStage - Этапы сотрудничества. Хранит название этапа и соответствующую иконку 

Все модели представлены в административной панели.

### Приложение projects 

Отвечает за данные о проектах компании. 

Модели:
- Category - Категория. Модель-справочник, хранящая категории: "Дома", "Бани" и "Коттеджи".
- Material - Материал. Модель-справочник, хранящая материалы, например, "Сосна", "Лиственница" и так далее.
- RoofType - Тип кровли. Модель-справочник, хранящая реализуемые в проектах компании типы кровли.
- Project - Проект. Хранит данные о проектах: название, описание, площадь, количество комнат, категория и так далее. Каждому проекту можно добавить информацию о его этажах, если она есть.
- Floor - Этаж. Хранит такие данные, как номер и площадь этажа проекта.

Все модели представлены в административной панели.

### Приложение reviews

Отвечает за загрузку и хранение отзывов со следующих источников: 
- 2GIS
- VL.ru
- Яндекс Карты

Модели:
- Review - Отзыв. Хранит данные об отзывах: оценку, имя автора, текст и дату публикации.

Все модели представлены в административной панели.

### Приложение contacts 

Отвечает за хранение контактных данных пользователей и компании.

Модели: 
- Worker - Сотрудник. Хранит данные о ключевых сотрудниках компании: ФИО, роль и фотографию.
- Request - Заявка. Хранит контактные данные пользователей, которые те оставили на сайте через форму обратной связи, а также флаг "Обработано/Не обработано".

Все модели представлены в административной панели.