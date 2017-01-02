import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('number')
    number_value = parser.parse_args().number
    return number_value


def format_price(price):
    price_string = try_to_float_else_throw_exception(price)
    formatted_price_string = []
    left_side_string, right_side_string = price_string.split('.')[0], price_string.split('.')[1]
    left_side = make_left_side(left_side_string)
    formatted_price_string.append(left_side)
    if bool(int(right_side_string)) is not False:
        formatted_price_string.append(right_side_string)
    return '.'.join(formatted_price_string)


def try_to_float_else_throw_exception(price):
    try:
        price_string = str(float(price))
        return price_string
    except ValueError:
        print(" '{}' не является допустимым значением.".format(price))
        quit()


def make_left_side(left_side_string):
    thouthand_len = 3
    # Реверсим строку левой части цены
    reversed_left_side = left_side_string[::-1]
    formatted_left_side_string_list = []
    # Реверснутую строку разбиваем на элементы по 3 символа
    for x in range(0, len(reversed_left_side), thouthand_len):
        three_symbol_elem = reversed_left_side[x: x+thouthand_len]
        # Реверсим полученные элементы, чтобы они приняли изначальную последовательность
        reversed_elem = ''.join(list(reversed(three_symbol_elem)))
        formatted_left_side_string_list.append(reversed_elem)
    # Реверсим список из полученных элементов
    formatted_string = ' '.join(list(reversed(formatted_left_side_string_list)))
    return formatted_string


def output_value(value):
    print("Отформатированное значение - {}".format(value))


if __name__ == '__main__':
    number_value = parse_arguments()
    formatted_value = format_price(number_value)
    output_value(formatted_value)
