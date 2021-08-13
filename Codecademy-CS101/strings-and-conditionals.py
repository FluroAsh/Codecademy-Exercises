# For every character in word,check to see if character = our letter that we have passed to the function. 
# If it matches return true, if not return false. 
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

letter_check('strawberry', 'a')
letter_check('strawberry', 'o')
