tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

# Empty dictionary for our 'spread'
spread = {}

# Using 'pop' to remove the card from our 'tarot' deck, adding it to the 'spread'
# No default value assigned, could use: tarot.pop(13, 'No card!') for eg if not found 
spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)

# Iterate through our spread (dictionary), and print a string to represent the 'time' & card 'value'
for time, value in spread.items():
  print('Your ' + str(time) + ' is the ' + str(value) + ' card.' )
