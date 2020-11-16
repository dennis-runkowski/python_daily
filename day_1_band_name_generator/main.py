"""Create a band name. """
from datetime import datetime, time


def main():
    """Main method to generate band name. """
    print("################################")
    print("       Band Name Generator      ")
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

    city = input("What city did you grow up in?\n")
    print("")
    pet = input("What is the name of your pet?\n")
    band_name = f"{city} {pet}"
    print("")
    print(f"The name of your band is {band_name}")


if __name__ == "__main__":
    main()
