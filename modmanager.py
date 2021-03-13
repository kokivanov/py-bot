import utils, commands

def main():
    mods = dict()
    lst = dir(commands)

    print(lst)

    for l in lst:
        if l.startswith("__"): continue
        else:
            mods[l] = getattr(getattr(commands, l), l)

    print(mods)
    pass

if __name__ == "__main__":
    main()