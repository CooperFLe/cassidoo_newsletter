def veritcal_slashes(slashes):
    spaces = 0
    answer = []
    for x in range(len(slashes)):
        if slashes[x] not in '\\|/':
            print("ERROR: Line " + str(x) + " not valid char")
            exit(1)
        if x == 0:
            answer.append(slashes[x])
        else:
            current = slashes[x]
            previous = slashes[x-1]
            spaces = shift(current, previous, spaces)
            if spaces < 0:
                spaces = spaces + 1
                answer = shift_all(answer)
            output = ' ' * spaces + slashes[x]
            answer.append(output)
    print_answer(answer)
def shift(current, previous, spaces):
    if current == '|':
        if previous == '\\':
            return spaces + 1
        else:
            return spaces - 1
    if current == previous:
        if current == '\\':
            return spaces + 1
        else:
            return spaces - 1
    else:
        if previous == '|':
            if current == '\\': 
                return spaces + 1
            else:
                return spaces - 1 
        return spaces
def shift_all(lines):
    newlines = []
    for line in lines:
        newlines.append(' ' + line)
    return newlines
def print_answer(answer):
    for line in answer:
        print(line)

veritcal_slashes('/|///|\\\\|\\\\|//|\\')