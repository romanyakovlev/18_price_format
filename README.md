# 18_price_format

Скрипт, представляющий строку из числа в более удобочитаемому виду. Работает в интерфейсе CLI, а также в качестве импортируемого модуля.

# Запуск

# 1.Запускаем скрипт 

```sh
python3 python3 format_price.py 12345.67
```
где в качестве примера аргумента представлено число "12345.6". Число должно быть вещественным. 

# 2.Запускаем его в качестве модуля

В качестве модуля импортируем функцию и вызовем ее с аргументом в виде строки.

```sh
from price_format import price_format

formated_string = format_string('12345.6')
```
