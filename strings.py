# Adding new lines to strings using \n
languages = "Python\nJava\nC++\nJavascript"
print(languages)

# Using \t to add tabs in strings
language = "\tPython"
print(language)

# Using \n and \t together
message = "Languages:\n\tPython\n\tJava\n\tC++\n\tJavascript"
print(message)

# Removing whitespace from strings using strip(), lstrip(), and rstrip()
best_language = "Python "
print(best_language.rstrip()) # Right side
print(best_language.lstrip()) # Left side
print(best_language.strip()) # Both sides

