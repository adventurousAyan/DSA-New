##Complete this function
def ternarySearch(self, arr, N, K):
    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid1 = int(start + (end - start) / 3)
        mid2 = int(end - (end - start) / 3)
        if arr[mid1] < K and arr[mid2] > K:
            start = mid1 + 1
            end = mid2 - 1
        elif arr[mid1] > K:
            end = mid1 - 1
        elif arr[mid2] < K:
            start = mid2 + 1
        else:
            return 1
    return -1
