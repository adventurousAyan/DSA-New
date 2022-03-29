class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ls = [0] * capacity
        self.ln = 0

    def isFull(self):
        return self.ln == self.capacity

    def isEmpty(self):
        return self.ln == 0

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) <= self.ln

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) <= self.ln

    def swap(self, index1, index2):
        self.ls[index1], self.ls[index2] = self.ls[index2], self.ls[index1]

    def showContents(self):
        print(self.ls)

    def heapifyUp(self, index):
        if self.hasParent(index):
            parIdx = self.getParentIndex(index)
            if self.ls[index] > self.ls[parIdx]:
                self.swap(index, parIdx)
            index = parIdx
            self.heapifyUp(index)

    def heapifyDown(self, index=0):
        if self.hasLeftChild(index):
            lindex = self.getLeftChildIndex(index)
            if self.ls[index] < self.ls[lindex]:
                self.swap(index, lindex)
                self.heapifyDown(lindex)
        if self.hasRightChild(index):
            rindex = self.getRightChildIndex(index)
            if self.ls[index] < self.ls[rindex]:
                self.swap(index, rindex)
                self.heapifyDown(rindex)

    def insert(self, data):
        if self.isFull():
            raise ("Heap is Full")
        else:
            self.ls[self.ln] = data
            self.heapifyUp(self.ln)
            self.ln = self.ln + 1

    def delete(self):
        if self.isEmpty():
            raise ("Heap is empty")
        else:
            self.ln = self.ln - 1
            self.ls[0] = self.ls[self.ln]
            self.ls[self.ln] = 0
            self.heapifyDown()


def heapsort(arr):
    ls = [0] * len(arr)
    n = len(ls)
    maxheap = MaxHeap(n)
    for a in arr:
        maxheap.insert(a)
    solve(maxheap, ls, n)
    print(ls)


def solve(maxheap, ls, n):
    if n == 0:
        return ls
    else:
        ls[n - 1] = maxheap.ls[0]
        maxheap.delete()
        solve(maxheap, ls, n - 1)


# maxheap = MaxHeap(7)
# maxheap.insert(20)
# maxheap.insert(10)
# maxheap.insert(15)
# maxheap.insert(5)
# maxheap.insert(6)
# maxheap.insert(30)
# maxheap.insert(40)
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()
# maxheap.delete()
# maxheap.showContents()

heapsort([10, 8, 12, 4, 3, 9])
