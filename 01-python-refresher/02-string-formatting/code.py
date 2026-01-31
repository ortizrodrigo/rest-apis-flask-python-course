name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)