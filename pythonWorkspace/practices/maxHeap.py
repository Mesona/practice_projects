inf = float("inf")

class maxHeap:
  def __init__(self, array = [0]):
    if array[0] != 0:
      self.heap = [0] + array
    else:
      self.heap = array

    self.length = len(self.heap)

  def insert(self, num):
    self.heap.insert(1, num)
    self.heapify(num)

  def pop(self):
    old = self.heap[1]
    self.heap.remove(old)
    self.insert(self.heap.pop())
    return old

  def find(self, num):
    pass

  def show(self):
    return self.heap

  def heapify(self, num):
    idx = self.heap.index(num)
    left = self.left(num)
    right = self.right(num)
    if num < left:
      [self.heap[idx], self.heap[idx * 2]] = [self.heap[idx * 2], self.heap[idx]]
      self.heapify(num)
      self.heapify(left)
    elif num < right:
      [self.heap[idx], self.heap[(idx * 2) + 1]] = [self.heap[(idx * 2) + 1], self.heap[idx]]
      self.heapify(num)
      self.heapify(right)

  def left(self, num):
    idx = self.heap.index(num)
    left = idx * 2
    if self.length > left:
      return self.heap[idx * 2]
    else:
      return -inf

  def right(self, num):
    idx = self.heap.index(num)
    right = (idx * 2) + 1
    if self.length > right:
      return self.heap[right]
    else:
      return -inf



