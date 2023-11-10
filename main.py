import random

def number():

    number_list = []
    number = random.randint(1, 45)

    for i in range(6):
        while number in number_list:
            number = random.randint(1, 45)
        number_list.append(number)
        if number in number_list:
            print("number_list에 해당 숫자가 있습니다.")

    number_list.sort()
    return number_list

print("생성된 로또번호는 {} 입니다.".format(number()))