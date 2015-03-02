# define variable formatter with 4 formatters in it
formatter = "%r %r %r %r"

# various fillings for the formatters in formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# use line breaks to avoid more than 80 characters
# per line
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)