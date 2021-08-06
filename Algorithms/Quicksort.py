def qsort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i >= pivot]
        return qsort(less) + [pivot] + qsort(more)

def main():
    arr=[]
    while True:
        num = input("Enter a number--> ")
        if num != '':
            arr.append(float(num))
        else:
            break
    return qsort(arr)

if __name__=="__main__":
    print(main())