def fonction():
    string=input().lower()
    string=list(string)
    liste_voyelle=["a","e","i","o","u","y"]
    for i in range(len(string)):
        if string[i] in liste_voyelle:
            string[i] = string[i].upper()
    string = "".join(string)
    print(string)
fonction()



