#二元搜尋必須在排序後的list
def binary_search(ls,target):
    ls.sort()
    low = 0
    high = len(ls)-1
    while low<=high:
        mid = (low+high)//2
        guess = ls[mid]
        if guess == target:
            return f'{guess} is at offset {mid}.'
        if guess > target:
            high = mid-1
        else:
            low = mid+1
    return f'{target} not found!'

if __name__=="__main__":
    a=[1,2,3,1,23435675,53,5,3452,352452345,1,3,74768,2,5465,25]
    target = 5465
    print(binary_search(a,target))