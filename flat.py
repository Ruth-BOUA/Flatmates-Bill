class Bill:
    """
    Object that contains a bill information as amount and period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    A flatmate person that has a name, a number of days spent in the house and pays a part of a bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, second_flatmate):
        weight = self.days_in_house / (self.days_in_house + second_flatmate.days_in_house)
        return round(bill.amount * weight, 2)
