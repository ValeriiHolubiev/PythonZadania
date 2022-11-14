zero = [" xxxx ",
        "x    x",
        "x    x",
        "x    x",
        "x    x",
        "x    x",
        " xxxx "]

one = ["  x ",
       " xx ",
       "x x ",
       "  x ",
       "  x ",
       "  x ",
       "xxxx"]

two = [" xxxx ",
       "x    x",
       "    x ",
       "   x  ",
       "  x   ",
       " x    ",
       "xxxxxx"]

three = [" xxxx ",
         "x   x ",
         "   x  ",
         "  xxx ",
         "     x",
         "x    x",
         " xxxx "]

four = ["x    x",
        "x    x",
        "x    x",
        "xxxxxx",
        "     x",
        "     x",
        "     x"]

five = ["xxxxxx",
        "x     ",
        "x     ",
        "xxxxx ",
        "     x",
        "x    x",
        " xxxx "]

six = [" xxxx ",
       "x    x",
       "x     ",
       "xxxxx ",
       "x    x",
       "x    x",
       " xxxx "]

seven = ["xxxxxx",
         "x    x",
         "    x ",
         "   x  ",
         "  x   ",
         " x    ",
         "x     "]

eight = [" xxxx ",
         "x    x",
         "x    x",
         " xxxx ",
         "x    x",
         "x    x",
         " xxxx "]

nine = [" xxxx ",
        "x    x",
        "x    x",
        " xxxxx",
        "     x",
        "x    x",
        " xxxx "]

dot = [" ",
       " ",
       " ",
       " ",
       " ",
       " ",
       "x"]

plus = ["       ",
        "   x   ",
        "   x   ",
        "x x x x",
        "   x   ",
        "   x   ",
        "       "]

equal = ["       ",
         "       ",
         " xxxxx ",
         "       ",
         " xxxxx ",
         "       ",
         "       "]

x = input("podaj liczbe: ")

for i in range(7):
    tekst = ""
    for k in range(len(x)):

        if x[k] == "0":
            tekst += zero[i]

        if x[k] == "1":
            tekst += one[i]

        if x[k] == "2":
            tekst += two[i]

        if x[k] == "3":
            tekst += three[i]

        if x[k] == "4":
            tekst += four[i]

        if x[k] == "5":
            tekst += five[i]

        if x[k] == "6":
            tekst += six[i]

        if x[k] == "7":
            tekst += seven[i]

        if x[k] == "8":
            tekst += eight[i]

        if x[k] == "9":
            tekst += nine[i]

        if x[k] == ".":
            tekst += dot[i]

        if x[k] == "+":
            tekst += plus[i]

        if x[k] == "=":
            tekst += equal[i]

        tekst += "  "

    print(tekst)