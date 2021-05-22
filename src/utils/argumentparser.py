from . import exceptions

from .abc import userRequestHandler

from .configmanager import cfg

import string

def parse(config : cfg, raw: str) -> userRequestHandler:
    cmd = str()
    wrd = str()
    args : list[str] = []
    flags = {}
    state = int(0)
    key = str()
    quotes = str()

    err = str()

    cmd = (raw.split(" ")[0])[len(config.prefix):]

    content = raw[len(cmd)+len(config.prefix):]

    content += " "

    i = len(cmd)+len(config.prefix)-2

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
                raise exceptions.InputError(msg="Unresolved symbols, please try to escape them or use word without quotes", index=i, src=raw)

        # quote closes
        elif state == 4:
            if c == " ":
                quotes = ""
                state = 1
            else:
                state = 15
                raise exceptions.InputError(msg="Error while parsing. Looks like there is symbol right after quotes on index {}".format(i), index=i, src=raw)

        #symbol after escape
        elif state == 5:
            if c == " ":
                wrd += "\ "
            else:
                wrd += str(c)
            state = 3

        # Symbol flag state
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
                raise exceptions.InputError(msg="Unexpected character оf flag name on index {}".format(i), index=i, src=raw)

        # Named flag state
        elif state == 7:
            if c == "-":
                wrd += str(c)
                state = 2
            elif c.isalpha():
                key = ""
                key += str(c)
                state = 9
            elif c == " ":
                args += [wrd]
                wrd = ""
                state = 1
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character оf flag name on index {}".format(i), index=i, src=raw)

        # Quiting symbol flag state
        elif state == 8:
            if c == "=":
                state = 10
            elif c == " ":
                flags[key] = None
                key = ""
                state = 1
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character after letter flag on index {}".format(i), index=i, src=raw)

        # Inside named flag state
        elif state == 9:
            if c == "=":
                state = 10
            elif c.isalpha():
                key += str(c)
            elif c == " ":
                flags[key] = None
                key = ""
                state = 1
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character in flag on index {}".format(i), index=i, src=raw)
        
        # Expecting argument within or out of quotes
        elif state == 10:
            if c == "\"" or c == "'":
                wrd = ""
                quotes = str(c)
                state = 12
            elif c.isalnum():
                wrd = ""
                wrd += str(c)
                state = 11
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character or space after seting flag parameter on index {}".format(i), index=i, src=raw)

        # Argument without quotes state
        elif state == 11:
            if c == " ":
                flags[key] = wrd
                key = wrd = ""
                state = 1
            elif c.isalnum():
                wrd += str(c)
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character in flag parameter on index {}".format(i), index=i, src=raw)

        # Argument within quotes state 
        elif state == 12:
            if c == quotes:
                flags[key] = wrd
                key = wrd = ""
                quotes = ""
                state = 13
            elif c == "\\":
                state = 14
            elif c.isalnum() or c == '"' or c == '\'' or c == ' ' or (c in string.punctuation):
                wrd += str(c)
            else:
                state = 15
                raise exceptions.InputError(msg="Unexpected character in flag parameter on index {}".format(i), index=i, src=raw)

        #  Quiting quotes expecting space
        elif state == 13:
            if c == " ":
                state = 1
            else:
                state = 15
                raise exceptions.InputError(msg="Error while parsing. Looks like there is symbol right after quotes on index {}".format(i), index=i, src=raw)

        # escape character in quotes of argument parameter
        elif state == 14:
            if c == " ":
                wrd += "\\ "
                state = 12
            else:
                wrd += str(c)
                state = 12

        elif state == 15:
            raise exceptions.InputError(msg="Error while parsing.", index=i, src=raw)

    if quotes != "":
        args += [wrd]
        last = len(args) - 1
        args[last] = args[last][0 : (len(args[last]) - 1)]

    return userRequestHandler(command=cmd, args=args, flags=flags)