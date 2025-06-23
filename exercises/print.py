def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
result = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentence_maker(user_input))

print(result)