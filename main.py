def convert_to_int(f_number, s_number):
    """
    Function to convert inputs to integers
    :param f_number:string
    :param s_number:string
    :return:integer
    """
    try:
        f_number = int(f_number)
        s_number = int(s_number)
    except ValueError:
        print("Entered invalid number, taken default values (1, 1)")
        return 1, 1
    else:
        return f_number, s_number


first_number = input('Enter first number: ')
second_number = input('Enter second number: ')

print(convert_to_int(first_number, second_number))