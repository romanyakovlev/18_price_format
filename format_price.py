import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('number')
    number_value = parser.parse_args().number
    return number_value


def format_price(price):
    price_string = try_to_float(price)
    formatted_price_string = []
    left_side_string, right_side_string = price_string.split('.')[0], price_string.split('.')[1]
    left_side = make_left_side(left_side_string)
    formatted_price_string.append(left_side)
    is_all_zeros = sum(1 for x in right_side_string if x is '0') is len(right_side_string)
    if not is_all_zeros:
        formatted_price_string.append(right_side_string)
    return '.'.join(formatted_price_string)


def try_to_float(price):
    try:
        price_string = str(float(price))
        return price_string
    except ValueError:
        print(" '{}' не является допустимым значением.".format(price))
        quit()


def make_left_side(left_side_string):
    amount_of_three_nums_through_space = len(left_side_string) // 3
    whole_numbers_amount = amount_of_three_nums_through_space * 3
    if amount_of_three_nums_through_space:
        nums_through_space_list = []
        after_three_nums = left_side_string[:-whole_numbers_amount]
        if after_three_nums:
            nums_through_space_list += after_three_nums
        three_nums_through_space_string = left_side_string[-whole_numbers_amount:]
        three_nums_through_space_list = [three_nums_through_space_string[x*3: x*3 + 3]
                                         for x in range(amount_of_three_nums_through_space)]
        nums_through_space_list += three_nums_through_space_list
        return ' '.join(nums_through_space_list)
    else:
        nums_without_space = left_side_string
        return nums_without_space


if __name__ == '__main__':
    number_value = parse_arguments()
    print(format_price(number_value))
