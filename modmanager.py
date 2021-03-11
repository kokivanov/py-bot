import utils

def main():
    mods = dict()
    lst = dir(utils)

    mods["config"] = getattr(getattr(utils, "config"), "config")

    # for i in lst:
    #     if str(i).startswith("__"): continue
    #     mods[str(i)] = getattr(getattr(utils, str(i)), str(i))
    
    print(mods)
    pass

if __name__ == "__main__":
    main()