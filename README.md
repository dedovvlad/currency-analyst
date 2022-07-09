## TODO:

### Функционал:
1. ~~Получать курс евро и доллара в текущий момент с фильтрацией по валюте, а так же массивом.~~
2. Получать курс евро и доллара за диапазон времени, отображать максимальный, минимальный и средний курс
3. Получать курс евро и доллара за диапазон времени и выводить массив разбивая по условию, 
   1. если диапазон меньше суток то выводить максимальный, минимальный и средний курс
   2. если диапазон больше суток, но меньше 2 то выводить список за каждый час максимальный, минимальный и средний курс
   3. если больше двух дней, но меньше двух недель то выводить максимальный, минимальный и средний курс за каждый день
   4. есди больше одной недели, но меньше месяца, то выводить за каждую полную неделю и остаток за неполную максимальный, минимальный и средний курс
   5. если больше месяца, но меньше года, вывводить за каждый месяц и остаток еще за один
   6. если больше года, то ...
4. Организовать хранилище стоимости валюты для построения графиков в графане за последний год с частотой минимум в 1 минуту
5. Добавить телеграм бота

### Тех:
1. ~~Добавить тесты~~
2. ~~Добавить запуск через файл make~~
3. ~~Описать Dockerfile~~
4. ~~Добавить .env~~
5. ~~Добавить линтеры~~
6. Добавить обработку исключений
7. ~~Добавить кеширование~~
8. Изменить мок на реальный запрос кодов валюты
9. Вынести вспомогательные функции в Utils
10. Добавить юнит тесты к редису 