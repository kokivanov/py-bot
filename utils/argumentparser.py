def parse(content : str) -> list:
    res = []
    wrd = str()
    state = int(0)
    separator = str()

    if len(content) < 2:
        return [content]

    for c in content:
        if c == ' ':
            if state == 0 or state == 1 or state == 4:
                state = 1
            elif state == 2:
                res.append(wrd)
                wrd = ""
                state = 1
            elif state == 3:
                wrd += c
        elif c == '"' or c == "'":
            if state == 0 or state == 1:
                wrd = ""
                sep = c
                state = 3
            elif state == 2:
                res.append(wrd)
                wrd = ""
                sep = c
                state = 3
            elif state == 3:
                if c == sep:
                    res.append(wrd)
                    wrd = ""
                    state = 4
                else:
                    wrd += c
            elif state == 4:
                wrd = ""
                sep = c
                state = 3
        else:
            if state == 0 or state == 1 or state == 4:
                wrd = ""
                wrd += c
                state = 2
            elif state == 2 or state == 3:
                wrd += c

    if wrd != "":
        res.append(wrd)
        wrd = ""

    while ' ' in res:
        res.remove(' ')

    while '' in res:
        res.remove('')

    while None in res:
        res.remove(None)

    return res