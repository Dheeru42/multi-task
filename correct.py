from textblob import TextBlob
inc = "heello my naem is dheeraj and i lobe nathural languge processibg"
output = TextBlob(inc).correct()
print(output)