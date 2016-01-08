name = 'Peter Lytle'
# This line defines the name variable.

age = 30
# This line defines the age variable.

height = 72 # inches
# This line defines the height variable.

weight = 150 # pounds
# This line defines the weight variable.

eyes = 'brown'
# This line defines the eyes variable.

teeth = 'white'
# This line defines the teeth variable.

hair = 'brown'
# This line defines the hair variable.

print "Let's talk about %s." % name
# This line displays some text, referencing a variable set in-line as "name".

print "He's %d inches tall." % height
# This line displays some text, referencing a variable set in-line as "weight".

print "He's %d pounds." % weight
# This line displays some text, referencing a variable set in-line as "weight".

print "Actually, that's not too heavy."
# This line displays some text.

print "He's got %s eyes and %s hair." % (eyes, hair)
# This line displays some text, referencing two different variables set in-line as "eyes" and "hair".

print "His teeth are usually %s, depending on the coffee." % teeth
# This line displays some text, referencing a variable set in-line as "teeth".

# This line is tricky, try to get it exactly right.
# This is a line of text supplied by the teacher, commented out.

print "If I add %d, %d and %d, I get %d." % (age, height, weight, age + height + weight)
# This line displays some text, referencing multiple variables and displaying the result of an arithmetic equation using said variables.
