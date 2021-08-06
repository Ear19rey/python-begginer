with open('162text.txt','r+') as f:
    line = f.read()
    words = line.replace("\n"," ").split(" ")
    total = 0
    for word in words:
        if total+len(word)>50:
            print(total)
            total = 0
        print(word,end=" ")
        total += len(word)+ 1



