import math

class Caculator():
    '''Performs basic arithmetic operations'''
    def __init__(self) -> None:
        self.result = '0'

    def execute(self, user_input):
        '''perfoms addition, substraction, multiplication, floor division and classic division'''
        try:
            input = user_input.replace('×', '*')
            input = input.replace('÷', '/')
            input = input.replace('^', '**')
            self.result = eval(input)
            return self.result
        except SyntaxError:
            return 'Error: Invalid character present'
        except:
            return 'Unknown error'
        
    def square_of(self, number):
        '''Gets number squared'''
        self.result = eval(number+'**2')
        return self.result
    
    def square_root_of(self, number):
        for char in str(number):
            if char in '+-÷×^*/':
                return 'Error'
        self.result = math.sqrt(int(number) | float(number))
        return self.result
 
    def clear_dot_zero(self, answer):
        answer = str(answer)
        if answer[-2] == '.' and answer[-1] == '0':
            answer = answer[:-2]
            return answer
