import re

# Character classes are enclosed in square brackets

# Here we use a character class to match upper and lowercase Python
print(re.search(r'[Pp]ython', 'python'))

# Here we define a range of characters using a dash
print(re.search(r'[a-z]way', 'Thataway'))

# Does not match...
print(re.search(r'[a-z]way', 'That way'))

# Negate with a circumflex: this regex matches the !
print(re.search(r'[^a-zA-Z]', 'Thataway!'))

# use the | to mean OR
print(re.search(r'cat|dog', 'I only like cats'))

# To find all matches, use findall instead of search!
print(re.findall(r'cat|dog', 'I like cats and dogs'))

# Repeated matches: .* means any character, as many as possible
print(re.search(r'Py.*n', 'Pygmalion'))
# returns Pygmalion
print(re.search(r'Py.*n', 'Python programming'))
# returns Python programmin; remember, it's greedy!
print(re.search(r'Py[a-z]*n', 'Python programming'))
# returns Python because it does not match the space

# + matches one or more occurrences
print(re.search(r'o+l+', 'goldfish')) #ol
print(re.search(r'o+l+', 'woollen')) #ooll
print(re.search(r'o+l+', 'boil')) # None

# ? means one or 0
print(re.search(r'o+l+d?', 'goldfish')) #ol

# Escape characters with a backslash
print(re.search(r'\.com') # would find the .com in a domain
# \ can also escape special string characters
# \w matches letters, numbers, and underscores
print(re.search(r'\w*', 'aflw_898 97')
# \d matches digits and \s matches whitespace, \b matches word boundaries

# Use ^ and $ to match the beginning and end of words:
print(re.search(r'^A.*a$', 'Argentina')) # will match this but not Azerbaijan

#Check the validity of a variable name in Python
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
print(re.search(pattern, '_This_is_valid_44'))




