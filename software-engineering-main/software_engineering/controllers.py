from models import NumbersList
from views import file_name_input, print_done_message

def create_nums_list(nums):
    parse_nums = [int(n) for n in nums.split()]
    return NumbersList(parse_nums)


def find_max(nums: NumbersList):
    """
    :param nums: object type NumberList
    :return: max int
    """
    return max(nums.nums)


def find_min(nums: NumbersList):
    return min(nums.nums)


def save_data(fun, data):
    file_name = file_name_input()
    str_data = fun(data)
    with open(f"{file_name}.txt", "w") as f:
        f.write(str_data)
    print_done_message()


def parse_list(data: NumbersList):
    return " ".join([str(n) for n in data.nums])


def parse_min_max(data: NumbersList):
    return f"{min(data.nums)} {max(data.nums)}"
