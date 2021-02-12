import discord


def parseArguments(message, prefix: str) -> []:
    args = message.content.split(" ")[len(prefix)-1:]
    ind = []
    splitter: str
    for i in message.content:
        if i == "'" or i == '"':
            splitter = i
    i: int = 0
    for ar in args:
        if len(ar) > 1 and ('"' in ar):
            ind.append(i)
        elif ar == '"':
            ind.append(i)
        elif len(ar) > 1 and ("'" in ar):
            ind.append(i)
        elif ar == "'":
            ind.append(i)
        i += 1

    del i
    print(ind)
    last: bool = False
    if len(ind) % 2 == 1:
        ind.append(ind[len(ind)-1])
        last = True

    ar_i: int = 0
    ind_i: int = 0
    newArgs = []
    while (ar_i < len(args)):
        if ind_i+1 <= len(ind) - 1 and ar_i < ind[ind_i]:
            newArgs.append(args[ar_i])
        else:
            newArgs.append(args[ar_i])
            if last and ind_i+1 == len(ind) - 1:
                for it in args[ind[ind_i]+1:]:
                    newArgs[len(newArgs)-1] += " " + it
                break

            if ind_i < len(ind)-1:
                for it in args[ind[ind_i]+1: ind[ind_i+1]+1]:
                    newArgs[len(newArgs)-1] += " " + it
                ar_i += ind[ind_i+1] - ind[ind_i]
                ind_i += 2
        ar_i += 1
    args = newArgs

    del ar_i
    del ind_i
    for item in args:
        if splitter in item:
            i = 0
            for abc in args:
                if abc == item:
                    break
                i += 1
            args[i] = item.replace(splitter, "")

    while '' in args:
        args.remove('')

    return args
