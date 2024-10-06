CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if scale == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}C iz equal to {converted_temp}F.")
        elif scale == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}F os equal to {converted_temp}F.")
        else:
            raise ValueError("Invalid scale. Please enter C for celsius or F for Fahrenheit. ")
    except ValueError as e:
        print(f"Error: {e}. Please enter a numeric value for the temperature.")
