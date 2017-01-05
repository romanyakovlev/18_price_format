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
        if price.count(",") is 1:
            formatted_price = price.replace(",", ".")
            price_string = str(float(formatted_price))
            return price_string
        price_string = str(float(price))
        return price_string
    except ValueError:
        print(" '{}' не является допустимым значением.".format(price))
        quit()


def make_left_side(left_side_string):
    formatted_price = separate_by_3_signs_from_right(left_side_string)
    return formatted_price


def separate_by_3_signs_from_right(string):
    """
    Функция форматирует строку, ставя разделитель в виде пробела после
    каждого 3-го числа. Так как отсчет для разделения начинаем слева, делаем
    реверс строки и разделяем ее, после чего делаем реверс обратно. 
    """
    signs_in_1000 = 3
    reversed_left_side = string[::-1]
    #formatted_left_side_string_list = []
    reversed_list_of_separated_elements = []
    for elem_index in range(0, len(reversed_left_side), signs_in_1000):
        reversed_three_sign_list = reversed_left_side[elem_index: elem_index+signs_in_1000]
        three_sign_string = ''.join(list(reversed(reversed_three_sign_list)))
        reversed_list_of_separated_elements.append(three_sign_string)
    formatted_string = ' '.join(list(reversed(reversed_list_of_separated_elements)))
    return formatted_string


def output_value(value):
    print("Отформатированное значение - {}".format(value))


if __name__ == '__main__':
    number_value = parse_arguments()
    formatted_value = format_price(number_value)
    output_value(formatted_value)
