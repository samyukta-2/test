import inflect

p = inflect.engine()

number = 12345

words = p.number_to_words(number)

print(f"{number} in words is: {words}")
