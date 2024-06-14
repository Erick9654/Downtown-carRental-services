class carStore:
    def __init__(self, store_id, car_type, total_cars, rented_cars):
        self.store_id = store_id
        self.car_type = car_type
        self.total_cars = total_cars
        self.rented_cars = rented_cars

    def show_number_of_cars(self):
        available_cars = self.total_cars - self.rented_cars
        print(f"Available cars: {available_cars}")

    def rent_hourly(self, num_cars):
        if self.rented_cars + num_cars <= self.total_cars:
            self.rented_cars += num_cars
            print(f"Rented {num_cars} car(s) on an hourly basis.")
        else:
            print("Not enough cars available to rent.")

    def rent_daily(self, num_cars):
        if self.rented_cars + num_cars <= self.total_cars:
            self.rented_cars += num_cars
            print(f"Rented {num_cars} car(s) on a daily basis.")
        else:
            print("Not enough cars available to rent.")

    def rent_weekly(self, num_cars):
        if self.rented_cars + num_cars <= self.total_cars:
            self.rented_cars += num_cars
            print(f"Rented {num_cars} car(s) on a weekly basis.")
        else:
            print("Not enough cars available to rent.")

    def return_car(self, customer):
        if customer.rentType == 1:
            rate = 900  # hourly rate
        elif customer.rentType == 2:
            rate = 2200  # daily rate
        elif customer.rentType == 3:
            rate = 1000  # weekly rate
        else:
            rate = 0

        if rate != 0:
            bill = customer.rentPeriod * rate
            self.rented_cars -= 1
            print(f"Car returned. Total bill: Ksh{bill}")
        else:
            print("Invalid rent type")

class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.rentType = 0
        self.rentPeriod = 0

    def car_request(self):
        return 1  # Assuming customer always requests 1 car for simplicity
