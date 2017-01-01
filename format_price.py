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
    num_of_signs = 3
    reversed_left_side = left_side_string[::-1]
    formatted_left_side_string_list = list(reversed([''.join(list(reversed(reversed_left_side[x: x+num_of_signs])))
                                                     for x in (range(0, len(reversed_left_side), num_of_signs))]))
    return ' '.join(formatted_left_side_string_list)


def output_value(value):
    print("Отформатированное значение - {}".format(value))


if __name__ == '__main__':
    number_value = parse_arguments()
    formatted_value = format_price(number_value)
    output_value(formatted_value)
