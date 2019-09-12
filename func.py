def discounted(price, discount):
    if discount >= 100:
        return "слишком большая скидка"
    else:
        return price - (price * discount / 100)

price = input("введи цену: ")

discount = input("введи скидку: ")

print(discounted(float(price),float(discount)))