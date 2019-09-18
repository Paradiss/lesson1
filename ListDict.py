print("List")
lasagne = ['Лист теста',"Бешамель","сыр","Болоньезе"]
lasagne.append("базилик")
lasagne.remove("Лист теста")
print(f'Сырный соус {lasagne[1:3]}')
print(lasagne[lasagne.index("базилик")])
print(lasagne)
lasagne.remove(lasagne[-1])
print(lasagne)

print('\n')
print("Dict")
Spyce = {
    "name" : "Paprika",
    "stock" : 2,
    "price" : 253,
}

print(Spyce["name"])