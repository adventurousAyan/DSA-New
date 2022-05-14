def array_of_array_products(arr):
    # your code goes here
    n = len(arr)
    if n == 0 or n == 1:
        return []
    pf_array = [1] * n
    sf_array = [1] * n

    for i in range(1, len(arr)):
        pf_array[i] = pf_array[i - 1] * arr[i - 1]

    for i in range(n - 2, -1, -1):

        sf_array[i] = sf_array[i + 1] * arr[i + 1]

    for i in range(n):
        arr[i] = pf_array[i] * sf_array[i]

    return arr


print(array_of_array_products([2, 7, 3, 4]))

print(array_of_array_products([8, 10, 2]))
