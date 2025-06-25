with open("bear.txt") as bear_list:
    bear = bear_list.read()

# print(bear[0:9])
with open("first.txt","w") as first_list:
    texto = bear[0:91]
    first_list.write(texto)
