import library

def main():
    h1 = ''
    h2 = ''
    h3 = ''

    while True:

        library.clear()
        library.header(h1, h2, h3)

        wantedaction = input(">")

        if wantedaction == "exit":
            break
        if wantedaction not in ["add", "sub", "mul", "div"]:
            print("Invalid input, please write 'add', 'sub', 'mul', 'div' or 'exit'.")
            input("Press Enter to continue...")
            continue

        try:
            number1 = float(input("> "))
            number2 = float(input("> "))
            if  wantedaction == "add":
                result_sum = f"{number1} + {number2} = {number1 + number2}"
            elif wantedaction == "sub":
                result_sum = f"{number1} - {number2} = {number1 - number2}"
            elif wantedaction == "mul":
                result_sum = f"{number1} * {number2} = {number1 * number2}"
            elif wantedaction == "div":
                if number2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result_sum = f"{number1} / {number2} = {number1 / number2}"


            h1, h2, h3 = h2, h3, result_sum

        except ValueError:
            print("Invalid number")
            input("Press Enter to continue...")
        except ZeroDivisionError as exc:
            print(exc)
            result_sum = f"{number1} / {number2} = Infinity"
            h1, h2, h3 = h2, h3, result_sum
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()