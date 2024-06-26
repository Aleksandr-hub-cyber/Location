Итоговая аттестация (виртуальная стажировка) SkillFactory.
Спринт/Задание по созданию Rest API в рамках совместной разработки мобильного приложения для Android и IOS ФСТР (Федерации Спортивного Туризма России).
Описание
ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней. Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет. Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Требования к Rest API

Метод POST submitData

Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:

координаты объекта и его высоту;
название объекта;
несколько фотографий;
информацию о пользователе, который передал данные о перевале:
имя пользователя (ФИО строкой);
почта;
телефон.
После этого турист нажмёт кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод submitData твоего REST API.

После того, как турист с помощью мобильного приложения и твоего REST API добавит в БД информацию о новом перевале, сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле status. Нужно добавить это поле в таблицу перевалов, который будет хранить статус модерации.

Допустимые значения поля status:

new;
pending — если модератор взял в работу;
accepted — модерация прошла успешно;
rejected — модерация прошла, информация не принята.

Понадобится добавить в него методы, с помощью которых ты будешь пополнять информацию в таблицах базы данных. Именно эти методы будет вызывать код твоего REST API при вызове метода POST submitData.

FSTR_DB_HOST: путь к базе данных;
FSTR_DB_PORT: порт базы данных;
FSTR_DB_LOGIN: логин, с которым происходит подключение к БД;
FSTR_DB_PASS: пароль, с которым происходит подключение к БД.

Три метода:
GET /submitData/<id> — получить одну запись (перевал) по её id.
Выведи всю информацию об объекте, в том числе статус модерации.
PATCH /submitData/<id> — отредактировать существующую запись (замена), если она в статусе new.
Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. Метод принимает тот же самый json, который принимал уже реализованный тобой метод submitData.

В качестве результата верни два значения:
state:
1 — если успешно удалось отредактировать запись в базе данных.
0 — в противном случае.
message — если обновить запись не удалось, напиши почему.
GET /submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер
