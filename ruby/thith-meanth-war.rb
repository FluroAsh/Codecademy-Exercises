# Replaces the letter "S" with "th"
# Thankth for thaying hello!
print "Pleathe enter a thtring: " 
user_input = gets.chomp
user_input.downcase!

if user_input.include?("s")
  user_input.gsub!(/s/, "th")
  puts user_input
else
  print "There are no \"S\"s in your string!"
end
