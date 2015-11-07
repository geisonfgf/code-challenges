"""
in: "This is some text in a file on disk. You will need to print every third word."
out: ['some', 'a', 'disk', 'need', 'every']
"""

statement = "This is some text in a file on disk. You will need to print every third word."
def print_third_word(statement):
    third_words, counter = [], 1
    for word in statement.split(" "):
        if counter == 3:
            third_words.append(word)
            counter = 0
        counter += 1
    return third_words

print "Expected: ", ['some', 'a', 'disk', 'need', 'every']
print "Result: ", print_third_word(statement)
