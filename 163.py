try:
    import re
    pat = re.compile('\w*[a]{1,}\w*[e]{1,}\w*[i]{1,}\w*[o]{1,}\w*[u]{1,}\w*[y]{1,}')
    n = input("Enter a file name:")
    with open(n,'r') as f:
        f=f.read().replace("\n"," ").split(" ")
        print(f)
        for word in f:
            m=pat.match(word)
            if m != None:
                print(word)

except FileNotFoundError:
    print("Invalid file name!")