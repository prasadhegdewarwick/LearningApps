from Resources import location


def show_header():

    print("----------------------------------------------")
    print("       Welcome To Weather App")
    print("----------------------------------------------")
    print()


if __name__ == '__main__':
    show_header()
    location.get_location()





