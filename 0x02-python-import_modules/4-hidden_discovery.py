#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    all_names = dir(hidden_4)

    for i in range(len(all_names)):
        if all_names[i][:2] != "__":
            print(all_names[i])
