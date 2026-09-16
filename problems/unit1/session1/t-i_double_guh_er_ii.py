# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

# def tiggerfy(word):
# 	pass
# Example Usage:

# word = "Trigger"
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)
# Example Output:

# "r"
# "eplan"
# "chor"
def tiggerfy(word):
    word = word.lower()
    word = word.replace("t", "")
    word = word.replace("i", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")
    return word