pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# To produce our string, use a loop with occuptation (key), value in our dictionary (pct_women_in_occupation) 
# and use .items to get BOTH the keys and values.
for occuptation, value in pct_women_in_occupation.items():
  print('Women make up: ' + str(value) + ' percent of ' + str(occuptation) + 's.')
