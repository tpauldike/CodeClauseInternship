
class Arithmetics():
    '''Performs basic arithmetic operations'''
    def __init__(self, first: int, sign: str, second: int) -> None:

        self.first = first
        self.sign = sign
        self.second = second
        self.answer

def execute(a, b, choice):
    '''perfoms the arithmetic operation based on the user's choice'''
    a = int(a)
    b = int(b)
    choice == choice.strip()

    if choice == '1':
        print(f'{a} + {b} = {a+b}')
    elif choice == '2':
        print(f'{a} - {b} = {a-b}')
    elif choice == '3':
        print(f'{a} × {b} = {a*b}')
    elif choice == '4':
        if (a % b) == 0:
            print(f'{a} ÷ {b} = {a//b}')
        else:
            print(f'{a} ÷ {b} = {a/b}')
    else:
        print(f'Error: "{choice}" is an invalid choice')


def is_valid(user_input):
    try:
        int(user_input.strip())
        return True
    except:
        print(f'"{user_input}" is not valid')
        return False