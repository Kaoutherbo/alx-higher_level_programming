#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the names defined by hidden_4"""
    import hidden_4

    names = dir(hidden_4)

    for i in names:
        if i[:2] != "__":
            print(i)
