#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hiden = dir(hidden_4)
    for i in range(len(hiden)):
        if hiden[i][:2] == "__":
            continue
        print(hiden[i])
