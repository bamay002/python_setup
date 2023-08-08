print('Hello from inside a file!')


def hello():
    print('Greetings user!')

hello()

def pack(a, b, c):
    return [a,b,c]

print(pack('abba', 'babba', 'cddc'))


def eat_lunch(my_list):
    if len(my_list) == 0:
        print('my lunchbox is empty')
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f'first i eat {my_list[0]}')
            else:
                print(f'next i eat {my_list[i]}')


eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])