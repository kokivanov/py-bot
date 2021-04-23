from . import exceptions
import string

def parse(content: str) -> list:
    cmd = str()
    wrd = str()
    args : list[str] = []
    flags = {}
    state = int(0)
    key = str()
    quotes = str()

    err = str()

    content += " "

    i = -1

    for c in content:
        i += 1

        # init and after space
        if state == 0 or state == 1:
            if c == '-':
                wrd = ""
                wrd += str(c)
                state = 6
            elif c == '\"' or c == '\'':
                wrd = ""
                quotes = str(c)
                state = 3
            elif c == ' ':
                state = 1
            else:
                wrd = ""
                wrd += str(c)
                state = 2
        
        # inside string
        elif state == 2:
            if c == ' ':
                args += [wrd]
                wrd = ""
                state = 1
            else:
                wrd += str(c)

        # inside quotes
        elif state == 3:
            if c == quotes:
                args += [wrd]
                state = 4
            elif c == '\\':
                state = 5
            elif c.isalnum() or c == '"' or c == '\'' or c == ' ' or (c in string.punctuation):
                wrd += str(c)
            else: 
                state = 15
                raise exceptions.InputError("Unresolved symbols, please try to escape them or use word without quotes", index=i)

        # quote closes
        elif state == 4:
            if c == " ":
                quotes = ""
                state = 1
            else:
                state = 15
                raise exceptions.InputError("Error while parsing. Looks like there is symbol right after quotes on index {}".format(i), index=i)

        #symbol after escape
        elif state == 5:
            if c == " ":
                wrd += "\ "
            else:
                wrd += str(c)
            state = 3

        elif state == 6:
            if c == "-":
                wrd += str(c)
                state = 7
            elif c.isalpha():
                key = str(c)
                state = 8
            elif c == " ":
                args += [wrd]
                wrd = ""
                state = 1
            else:
                state = 15
                raise exception.InputError("Unexpected character if flag name on index {}".format(i), i)
                
    if quotes != "": 
        args += [wrd]
        last = len(args) - 1
        args[last] = args[last][0 : (len(args[last]) - 1)]
    return args