def f_to_c():
    f = float(input('\n Enter Fahrenheit > '))
    c = (f - 32) * 5/9
    print(f'\n {f} F To Celsius Is: {c}')
    print('\n Visit My Website :) https://lukkshh.ga/')
def c_to_f():
    c = float(input('\n Enter Celsius > '))
    f = c * 1.8 + 32
    print(f'\n {c} C To Fahrenheit Is: {f}')
    print('\n Visit My Website :) https://lukkshh.ga/')
def main():
    user_choice = input('\n Celsius To Fahrenheit (c) Or Fahrenheit To Celsius (f) ? (f/c) > ')
    if user_choice == 'f':
        f_to_c()
    elif user_choice == 'c':
        c_to_f()
    else:
        main()
if __name__ == '__main__':
    main()