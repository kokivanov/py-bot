import utils, commands

def main():
    mods = dict()
    lst = dir(commands)

    print(lst)

    mods["ping"] = getattr(getattr(commands, "ping"), "ping")

    # for i in lst:
    #     if str(i).startswith("__"): continue
    #     mods[str(i)] = getattr(getattr(utils, str(i)), str(i))
    
    mods["ping"]()

    print(mods)
    pass

if __name__ == "__main__":
    main()