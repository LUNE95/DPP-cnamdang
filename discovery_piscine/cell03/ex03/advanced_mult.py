i = 0
while i <= 10:
    lint = "Table de" + str(i) + ":"
    j = 0
    while j <= 10:
        lint += " " + str(i * j)
        j += 1
        print(lint)
        i += 1