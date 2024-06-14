#!/usr/bin/env python3

from models.cars import carStore, Customer
from tqdm import tqdm


def main():
    store = carStore(1, 'sedan', 10, 0)
    cust = Customer(101)

    while True:
        print("""
        *************************************************
        1. Show available number of cars in store
        2. Rent a Car on hourly basis for Ksh900/hr
        3. Rent a Car on daily basis for Ksh2200/day
        4. Rent a Car on weekly basis for Ksh1000/week
        5. Return a rented Car back.
        6. Exit
        *************************************************
        """)
        choice = int(input("\nHow would you like to use Downtown Car Rental services\n"))

        if choice == 1:
            store.show_number_of_cars()
        elif choice == 2:
            cust.rentType = 1
            n = cust.car_request()
            if n != 0:
                for _ in range(n):
                    store.rent_hourly(1)
                hours = int(input("\nHow many hours would you like to rent the car?\n"))
                cust.rentPeriod = hours
        elif choice == 3:
            cust.rentType = 2
            n = cust.car_request()
            if n != 0:
                for _ in range(n):
                    store.rent_daily(1)
                days = int(input("\nHow many days would you like to rent the car?\n"))
                cust.rentPeriod = days
        elif choice == 4:
            cust.rentType = 3
            n = cust.car_request()
            if n != 0:
                for _ in range(n):
                    store.rent_weekly(1)
                weeks = int(input("\nHow many weeks would you like to rent the car?\n"))
                cust.rentPeriod = weeks
        elif choice == 5:
            store.return_car(cust)
        else:
            print("\nThanks for your visit; Merci pour votre service\n")
            exit()


if __name__ == '__main__':
    main()
