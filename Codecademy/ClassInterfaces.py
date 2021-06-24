# When two classes have the same method names and attributes, 
# we say they implement the same interface. An interface in Python usually 
# refers to the names of the methods and the arguments they take.


class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005