FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_input = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'F':
    converted = convert_to_celsius(temperature_input)
    print(f"{temperature_input}°F is {converted}°C")
elif unit == 'C':
    converted = convert_to_fahrenheit(temperature_input)
    print(f"{temperature_input}°C is {converted}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")