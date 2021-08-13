authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names, '\n')

author_last_names = []
# For every name in author_names split using space and select the last name at index -1 (which is the last name)
for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)
