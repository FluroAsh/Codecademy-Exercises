class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  # Returns the amount of lawyers that have been initialized correpsonding to 'practice'
  def __len__(self):
    return len(self.lawyers)

  # Check to see if our 'lawyer' is contained in 'lawyers'
  # 'lawyer' is constructed in __init__
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
  
  def __repr__(self):
    return self.lawyers
      
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
