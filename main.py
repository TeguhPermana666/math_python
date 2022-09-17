from decimal import DivisionByZero
from math_function import add,mul,div


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")
    try:
        if operator == "+":
            result = add(data_1, data_2)
            
        if operator == "*":
            result = mul(data_1,data_2)
        if operator == "/":
            try:    
                result = div(data_1,data_2)
            except DivisionByZero:
                print("ZeroDivisionError Occurred and Handle")
    except NameError:
        print("NameError Occurred and Handled")
    finally:
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
        


if __name__ == "__main__":
    print("Hello Main !")
    main()