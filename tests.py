list = {
    "Wong": {
        "queso": 8.990,
        "jamon": 18.0,
        "leche": 4.50,
        "huevos": 6.650,
        "arroz": 17.50
    },
    "PlazaVea": {
        "queso": 8.1,
        "jamon": 14,
        "leche": 4.3,
        "huevos": 6.6,
        "arroz": 16.99
    },
    "Tottus": {
        "queso": 8.1,
        "jamon": 10.46,
        "leche": 4.3,
        "huevos": 8.45,
        "arroz": 17.89
    }
}

total = []
temp = 0

for counter in list.values():
    for x in counter.values():
        temp = temp+x
    total.append(temp)
    temp = 0

print(total)
