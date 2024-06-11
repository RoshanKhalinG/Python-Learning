def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters': {'feet': value * 3.28084, 'meters': value},
        'feet': {'meters': value / 3.28084, 'feet': value}
    }
    return conversions[from_unit][to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'kilograms': {'pounds': value * 2.20462, 'kilograms': value},
        'pounds': {'kilograms': value / 2.20462, 'pounds': value}
    }
    return conversions[from_unit][to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def main():
    print("Welcome to the Unit Converter!")
    print("Choose the type of conversion:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        print("You chose Length conversion.")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit (meters/feet): ").lower()
        to_unit = input("Enter the to unit (meters/feet): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '2':
        print("You chose Weight conversion.")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit (kilograms/pounds): ").lower()
        to_unit = input("Enter the to unit (kilograms/pounds): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '3':
        print("You chose Temperature conversion.")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit (celsius/fahrenheit/kelvin): ").lower()
        to_unit = input("Enter the to unit (celsius/fahrenheit/kelvin): ").lower()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    else:
        print("Invalid choice. Please restart the program and choose a valid option.")

if __name__ == "__main__":
    main()
