# https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559?leftPanelTab=1


def aggressiveCows(stalls, k):
    # Write your code here.
    stalls = sorted(stalls)
    n = len(stalls)
    low = 0
    high = stalls[n - 1] - stalls[0]

    while low <= high:

        mid = low + (high - low) // 2

        if canPlaceCows(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1

    return high


def canPlaceCows(stalls, mid, k):
    cnt = 1

    cord = 0

    for i in range(1, len(stalls)):

        if stalls[i] - stalls[cord] >= mid:
            cnt += 1
            cord = i

        if cnt == k:
            return True

    return False
