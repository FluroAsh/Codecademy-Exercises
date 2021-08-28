love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

# for every line in love_maybe_lines strip spaces and append to our love_maybe_lines_stripped list
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

# After we've executed our loop join our list with new lines between each index
# (note 2 lines at the end as we have '\n' in it's own index within the string)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)
