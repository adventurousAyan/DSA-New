class BS:
    def search(self, arr, data):
        start = 0
        end = len(arr) - 1
        return self.binary_search(start, end, arr, data)

    def binary_search(self, start, end, arr, data):
        mid = start + (end - start) / 2
        mid = int(mid)
        if arr[mid] == data:
            return mid
        elif data > arr[mid]:
            return self.binary_search(mid + 1, end, arr, data)
        else:
            return self.binary_search(start, mid, arr, data)


ls = [-5, -4, -3, -2, 1, 0, 5, 7, 9]
bs = BS()
print(bs.search(ls, -2))

print(bs.search(ls, 9))
