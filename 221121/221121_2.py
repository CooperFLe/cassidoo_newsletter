def veritcal_slashes(slashes):
    spaces = 0
    for x in range(len(slashes)):
        if x == 0:
            print(slashes[x])
        else:
            current = slashes[x]
            previous = slashes[x-1]
            spaces = shift(current, previous, spaces)
            output = ' ' * spaces + slashes[x]
            print(output)
def shift(current, previous, spaces):
    if current == previous:
        if current == '\\':
            return spaces + 1
        else:
            return spaces - 1
    else:
        return spaces

veritcal_slashes('\\\//\/\\')