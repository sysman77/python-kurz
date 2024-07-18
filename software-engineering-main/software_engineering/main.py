from models import NumbersList
from controllers import *
from views import *


def run():
    nums = NumbersList()
    while True:
        print_main_menu()
        user_choice = user_choice_input("5")

        if user_choice == "1":
            user_input = nums_input()
            nums = create_nums_list(user_input)

        elif user_choice == "2":
            max_num = find_max(nums)
            print_max(max_num)

        elif user_choice == "3":
            min_num = find_min(nums)
            print_min(min_num)

        elif user_choice == "4":
            save_data(parse_list, nums)

        elif user_choice == "5":
            save_data(parse_min_max, nums)

        elif user_choice == "0":
            exit_program()
            break

        else:
            wrong_input_message()






run()