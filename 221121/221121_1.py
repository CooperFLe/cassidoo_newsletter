def veritcal_slashes(slashes):
    spaces = 0
    for slash in slashes:
        output = " " * spaces + slash
        print(output)
        if slash == '\\':
            spaces = spaces + 1
        if slash == '/':
            spaces = spaces -1

veritcal_slashes('\\\//\/\\')