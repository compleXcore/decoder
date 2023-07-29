def compleXdecoder(password):
    print("Password: ", password)
    password_reverse = password[::-1]
    print("Password reverse: ", password_reverse)
    password_ascii = ""
    for i in password_reverse:
        password_ascii = password_ascii + "" + chr(ord(i)+1)
    print("Password reverse ascii+1 char: ", password_ascii)

    password_ascii_number = ""
    for i in password_ascii:
        password_ascii_number = password_ascii_number + "-" + str(ord(i))
    password_ascii_number = password_ascii_number[1:]
    print("Password reserve ascii+1 number: ", password_ascii_number)
    """ 1-! 2-? 3-# 4-$ 5-% 6-' 7-* 8-+ 9-@ 0-~"""
    """ !-l9HW ?-IXgv #-zjiy $-{kl| %-oDe7 '-?84R *-7?9! +-?5s1 @-_%5M ~-x0if"""
    password_replace = password_ascii_number
    password_replace = password_replace.replace("1", "!")
    password_replace = password_replace.replace("2", "?")
    password_replace = password_replace.replace("3", "#")
    password_replace = password_replace.replace("4", "$")
    password_replace = password_replace.replace("5", "%")
    password_replace = password_replace.replace("6", "'")
    password_replace = password_replace.replace("7", "*")
    password_replace = password_replace.replace("8", "+")
    password_replace = password_replace.replace("9", "@")
    password_replace = password_replace.replace("0", "~")
    print("Password replace(1): ", password_replace)
    password_replace = password_replace.replace("!", "l9HW")
    password_replace = password_replace.replace("?", "IXgv")
    password_replace = password_replace.replace("#", "zjiy")
    password_replace = password_replace.replace("$", "{kl|")
    password_replace = password_replace.replace("%", "oDe7")
    password_replace = password_replace.replace("'", "k84R")
    password_replace = password_replace.replace("*", "7q9p")
    password_replace = password_replace.replace("+", "m5s1")
    password_replace = password_replace.replace("@", "_}5M")
    password_replace = password_replace.replace("~", "x0if")
    print("Password replace(2): ", password_replace)

    password_compleX = []
    count = 0
    count2 = 0
    for i in password_replace:
        count += 1
        if i == "-" or count == len(password_replace):
            password_compleX.append(password_replace[count2:count].replace("-", ""))
            count2 = count

    print("Arayy and Delete this '-' symbol:", password_compleX)

    temp = password_compleX.copy()

    count = 1
    lenght = len(password_compleX)
    for i in range(lenght):
        password_compleX[i] = temp[lenght-count]
        count += 1

    print("Switch index?:",password_compleX)
    password_finish = ""
    for i in password_compleX:
        password_finish = password_finish + "-" + i

    password_finish = password_finish[1:] + "-xCore"
    print("Final:", password_finish)

compleXdecoder("compleXcore")