def miniMaxSum(arr):
    list1 = []
    total = 0
    for num in arr:
        total += num
    for i in range(len(arr)):
        total1 = total-arr[i]
        list1.append(total1)
    maxi = max(list1)
    mini = min(list1)
    return maxi, mini
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    maximum, minimum = miniMaxSum(arr)
    print(minimum,maximum)
