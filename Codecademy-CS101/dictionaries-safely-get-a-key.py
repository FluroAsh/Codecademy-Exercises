user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Get 'teraCoder' user ID with 10000 as a default value, if it doesn't exist store in 'tc_id'
tc_id = user_ids.get('teraCoder', 10000)
print(tc_id)

# Notice how it doesn't exist in our dictionary, so we print '100000'
stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)
