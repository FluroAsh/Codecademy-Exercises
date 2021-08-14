highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Split our list into individual lists using ',' as the delimiter
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list, '\n')

# For every poem in our poems list strip away the space and append it to our new list highlighted_poems_stripped
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped, '\n')


highlighted_poems_details = []
# For every poem (list of 3 elements) in highlighted_poems_stripped, split our lists at our delimiter (':') and append it to highlighted_poems_details
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

print(highlighted_poems_details, '\n',)

titles = []
poets = []
dates = []

# for every poem (list) in our mega list (higlighted_poems_details), append each index as below into it's own list as above
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[-2])
  dates.append(poem[-1])

# For every index in the range of 0-2 (AKA Titles, Poets, Dates) print this string with 'x' formatting using every index as a reference. 
for i in range(0, len(highlighted_poems_details)):
  print('The poem {}, was published by {} in {}.'.format(titles[i], poets[i], dates[i]))
