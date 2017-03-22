class Taxi_Rank:
    def __init__(self, cars, info, operator, income, outcome, employment, setup_terminal):
        self.cars = cars
        self.info = info
        self.operator = operator
        self.income = income
        self.outcome = outcome
        self.employment = employment
        self.setup_terminal = setup_terminal

    def cars(self, space, driver):
        self.space = int(4)
        self.driver = driver
        if driver is 'free':
            dispach.carID()         