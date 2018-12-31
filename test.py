icons = ['a', 'b', 'c', 'd']

# colorset
colorkeys = {}
for i in range(3):
    icon = icons[i]
    color = []
    for value in range(3):
        value = 1
        color.append(value)
    colorkeys.update({icon:color})

# wall maker
for key, value in colorkeys.items():
    print(key, value)


