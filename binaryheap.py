#!/usr/bin/env python3
"""
binaryheap.py
This demonstration uses a list to build and maintain a minHeap tree.
@author Dexter Renick
@version 2018-04-25
"""

class BinaryHeap():
    """The BinaryHeap class implements the Binary Heap Abstract
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heapList = [0]  # not used. Here just to make parent-
                             # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1
        self.currentsize = 0

    def insert(self,value):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        self.heapList.append(value)
        self.currentsize += 1
        self.percolateUp(self.currentsize)

    def percolateUp(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        while i != 0:
            if self.heapList[i//2] > self.heapList[i]:
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
                i = i//2
            else:
                break

    def delMin(self):
        """This is a bit trickier. It's easy to return the minimum item,
        the first item on the list, but how do we readjust the heap then?
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentsize]
        self.percolateDown(1)
        self.heapList.pop()
        self.currentsize -= 1
        return retval

    def percolateDown(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        while (i * 2) <= self.currentsize:
            if i * 2 + 1 > self.currentsize:
                minChild = i*2
            else:
                if self.heapList[i*2] < self.heapList[i*2+1]:
                    minChild = i * 2
                else:
                    minChild = i * 2 + 1
            if self.heapList[minChild] < self.heapList[i]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild

    def findMin(self):
        """Returns the minimum item in the heap, without removing it.
        """
        return self.heapList[1]

    def isEmpty(self):
        if self.currentsize == 0:
            return True
        else:
            return False

    def size(self):
        return self.currentsize

    def buildHeap(self, list_of_keys):
        i = len(list_of_keys)//2
        self.currentsize = len(list_of_keys)
        self.heapList = [0] + list_of_keys[:]
        while (i > 0):
            self.percolateDown(i)
            i = i - 1


    def __repr__(self):
        return "BinaryHeap" + str(self.heapList)

def main():
    print("Demonstrating minHeap binary tree")
    bh = BinaryHeap()
    values = [2, 3, 9, 4, 1, 8, 7, 15, 20, 41, 32, 5]
    bh.buildHeap(values)
    print(bh)
    bh.delMin
    print(bh)


if __name__ == "__main__":
    main()
