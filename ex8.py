formatter = "%r %r %r %r"
# This line defines the variable formatter, using 4 other variables.

print formatter % (1, 2, 3, 4)
# This line displays the output of the formatter variable, defined in-line.

print formatter % ("one", "two", "three", "four")
# This line displays the output of the formatter variable, defined in-line.

print formatter % (True, False, False, True)
# This line displays the output of the formatter variable, defined in-line.

print formatter % (formatter, formatter, formatter, formatter)
# This line displays the output of the formatter variable, defined in-line.

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
# These lines display the output of the formatter variable, defined over 4 lines. For some reason, the third line displays with double quotes, but not any of the others.
