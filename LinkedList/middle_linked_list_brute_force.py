def generate_random_number(n):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 10, 6, 8]
    if n == 0:
        return
    else:
        ln = len(arr) - 1
        return arr[ln]

    # generate_random_number(n-1)


def middle_node(head):

    curr = head
    n = 0

    while curr != None:
        n = n + 1
        cur = cur.next

    start = 0
    end = n - 1

    mid = start + int((end - start) / 2)

    if n % 2 == 0:
        mid = mid
    else:
        mid = mid + 1

    cur = head
    m = 0
    while cur.next != None:
        if m == mid:
            return cur.data
        cur = cur.next
        m = m + 1
