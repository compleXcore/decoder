def compleXcoder(hashcode):
    hashcode = hashcode.replace("-xCore", "")

    password_replace = hashcode
    password_replace = password_replace.replace("l9HW", "!")
    password_replace = password_replace.replace("IXgv", "?")
    password_replace = password_replace.replace("zjiy", "#")
    password_replace = password_replace.replace("{kl|", "$")
    password_replace = password_replace.replace("oDe7", "%")
    password_replace = password_replace.replace("k84R", "'")
    password_replace = password_replace.replace("7q9p", "*")
    password_replace = password_replace.replace("m5s1", "+")
    password_replace = password_replace.replace("_}5M", "@")
    password_replace = password_replace.replace("x0if", "~")
    print("Password replace(2): ", password_replace)
    password_replace = password_replace.replace("!", "1")
    password_replace = password_replace.replace("?", "2")
    password_replace = password_replace.replace("#", "3")
    password_replace = password_replace.replace("$", "4")
    password_replace = password_replace.replace("%", "5")
    password_replace = password_replace.replace("'", "6")
    password_replace = password_replace.replace("*", "7")
    password_replace = password_replace.replace("+", "8")
    password_replace = password_replace.replace("@", "9")
    password_replace = password_replace.replace("~", "0")
    print("Password replace(1): ", password_replace)

    password_compleX = []
    count = 0
    count2 = 0
    for i in password_replace:
        count += 1
        if i == "-" or count == len(password_replace):
            password_compleX.append(password_replace[count2:count].replace("-", ""))
            count2 = count

    print(password_compleX)

    password_reverse = ""
    for i in password_compleX[::-1]:
        password_reverse = password_reverse + "" + chr(int(i)-1)
    
    password_reverse = password_reverse[::-1]
    print(password_reverse)
compleXcoder("l9HWx0ifx0if-l9HWl9HWIXgv-l9HWl9HWx0if-l9HWl9HWzjiy-l9HWx0if_}5M-l9HWx0ifIXgv-m5s1_}5M-l9HWx0ifx0if-l9HWl9HWIXgv-l9HWl9HWoDe7-l9HWx0ifIXgv-xCore")