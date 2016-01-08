print "Mary had a little lamb."
# This line displays some text.

print "Its fleece was white as %s." % 'snow'
# This line displays some text, including a variable defined in-line.

print "and everywhere that Mary went."
# This line displays some text.

print "." * 10 # What did this line do?
# This line prints ten "." 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# These 12 lines define different variables.

# Watch that comma at the end. Try removing it to see what happens.

print end1 + end2 + end3 + end4 + end5 + end6,
# This line displays the output from the first 6 variables. The comma ensures the next line prints to the same line when displayed.

print end7 + end8 + end9 + end10 + end11 + end12
# This line displays the output from the second 6 variables. Due to the comma at the end of the previous line, it will appear on the same line.
