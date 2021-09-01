class InsurancePolicy:
  # Constructs our variable to be used in 'VehicleInsurance' & 'HomeInsurance' 
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# These 2 classes are used to perform different calculations depending on the needs of the client 
# They use the same 'INTERFACE' (different classes performing the same operation, despite having different implementation)
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.00005
