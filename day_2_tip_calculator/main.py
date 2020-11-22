"""Tip Calculator."""
from datetime import datetime, time

VALID_PERCENT = {
    "10": 0.1,
    "12": 0.12,
    "15": 0.15,
    "20": 0.2
}


def main():
    """Main method for the tip calculator. """
    print("################################")
    print(" Welcome to the tip Calculator  ")
    print("################################")
    print("")

    current_time = datetime.now()
    now_time = current_time.time()
    if now_time >= time(17, 00) and now_time <= time(23, 59):
        print("Good Evening!")
    elif now_time >= time(12, 00) and now_time <= time(17, 00):
        print("Good Afternoon!")
    elif now_time >= time(00, 00) and now_time <= time(12, 00):
        print("Good Morning!")
    else:
        print("Hello")

    total = input("What was the total bill? ")
    try:
        total = float(total)
    except Exception as e:
        raise TypeError("Please pass in a valid number!")

    percent = input("What percentage tip would you like to give (10, 12, 15, or 20)? ")  # noqa
    percent = VALID_PERCENT.get(percent)
    if not percent:
        raise ValueError("Please pass in a valid percent!")

    number_people = input("How many people to split the bill? ")
    try:
        number_people = float(number_people)
    except Exception as e:
        raise TypeError("Please pass in a valid number of people!")

    result = round((total + (total * percent)) / number_people, 2)
    print(f"Each person should pay: ${result}")


if __name__ == "__main__":
    main()
