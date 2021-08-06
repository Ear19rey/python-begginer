def longestSequence(start, words):
    if start == "":
        return []
    best = []
    last_letter = start[-1]
    for i in range(len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            candidate = longestSequence(words[i], words[0 : i] + words[i + 1 : len(words)])
            if len(candidate) > len(best):
                best = candidate
    return [start] + best

def loadNames():
    names = []
    with open("D:\Download\Periodic Table of Elements.csv", "r",encoding='utf-8') as inf:
        for line in inf:
            parts = line.split(",")
            names.append(parts[1])
        names.remove(names[0])
    return names

def main():
    names = loadNames()
    start = input("Enter the name of an element: ")
    start = start.capitalize()
    try:
        names.remove(start)
        sequence = longestSequence(start, names)
        print("A longest sequence that starts with", start, "is:")
        for element in sequence:
            print(element)
    except ValueError:
        print("Invalid element name!!")

main()