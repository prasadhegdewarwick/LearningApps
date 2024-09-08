import datetime


def print_header():
    print("-------------------------------")
    print("Welcome to Birthday Calender")
    print("-------------------------------")
    print()


def get_birthday_from_user():
    print("Please Enter your Birthday Here")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    birth_day = datetime.date(year, month, day)
    return birth_day


def compute_dates_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    date_difference = this_year - target_date
    return  date_difference.days



def print_birthday_information(num_days):
    if num_days < 0 :
        print(f"You already Had birthday before {num_days * -1} Days Back")
    elif num_days > 0:
        print(f"Your birthday is coming in {num_days} days")
    else:
        print("Wish you Happy Birthday")



def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_dates_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()