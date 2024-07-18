

def print_main_menu():
    print("""
-----------MAIN MENU----------
[1] - zadať čisla
[2] - ukáž maximum
[3] - ukaž minimum
[4] - zapiš zoznam čisel do suboru
[5] - zapis min max hodnoty do suboru
[0] - ukonči program
    """)


def file_name_input():
    return input("zadaj nazov suboru: ")


def user_choice_input(last_choice):
    return input(f"zadaj volbu od 0 do {last_choice}: ")


def nums_input():
    nums = input("Zadaj čisla odelene medzerami: ")
    return nums


def print_max(num):
    print(f"""Maximum zo zadanych cisel je {num}""")


def print_min(num):
    print(f"""Minimum zo zadanych cisel je {num}""")


def exit_program():
    print("nashledanou a zase nabuduce")


def wrong_input_message():
    print("zadal si neplatnu volbu!")


def print_done_message():
    print("data zapisane do suboru")
