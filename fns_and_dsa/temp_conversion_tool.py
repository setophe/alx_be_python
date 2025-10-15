FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * FAHRENHEIT_TO_CELSIUS_FACTOR

temperature = int(input("Enter the temperature to convert: "))
type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if type == "C":
    print(f"{temperature} °C is {convert_to_fahrenheit(temperature)} °F")
elif type == "F":
    print(f"{temperature} °F is {convert_to_celsius(temperature)} °C")