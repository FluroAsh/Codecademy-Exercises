# Return true if little strings is in big string, otherwise return false
def contains(big_string, little_string):
  return little_string in big_string

contains("watermelon", "melon")
contains("watermelon", "berry")

# If character in string one is in string two, and char isn't already in common list, then append the character to common and return our common list at the end of the function
def common_letters(string_one, string_two):
  common = []
  for char in string_one:
    if (char in string_two) and not (char in common):
      common.append(char)
  return common

common_letters("banana", "cream")
