class Bill:
    """
        Object that contains data about a bill, such total amount and period of the bill.
    """

    def __init__(self, period, amount):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmates person who lives in the flat and pays a share of the bill
    """

    def __init__(self, days_in_house, name):
        self.name= name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
