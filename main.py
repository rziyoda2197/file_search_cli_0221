import os

path = input("Papka: ")
name = input("Qidiruv nomi: ")

for root, dirs, files in os.walk(path):
    for f in files:
        if name in f:
            print(os.path.join(root, f))
