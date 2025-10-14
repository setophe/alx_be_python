def perform_operation(num1 : float,num2 :float ,operation : str):
    operations_available = ["add","subtract","multiply","divide"]

    if not operation in operations_available:
        return "Invalid operation"
    else:

        match operation:
            case "add":
                return num1 + num2
            case "substract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                if num2 == 0:
                    return "You can't divide by zero"
                else:
                    return num1 / num2
            case _:
                return "Invalid operation"