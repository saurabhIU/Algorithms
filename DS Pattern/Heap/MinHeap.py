# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        firstParentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx,len(array)-1,array)
        return array

    def siftDown(self,start,end,heap):
        # Write your code here.
        left = (start*2)+1
        
        while left <= end:
            lower_idx = 0
            right = (start*2)+2 if (start*2)+2 <= end else None
            if right and heap[right]<heap[left]:
                lower_idx = right
            else:
                lower_idx = left
            if heap[lower_idx] < heap[start]:
                self.swap(start,lower_idx,heap)
            else:
                return
            start = lower_idx
            left = (start*2)+1
                
            
        

    def siftUp(self,array):
        # Write your code here.
        current_index = len(array)-1
        parent_index = (current_index-1)//2
        while parent_index > 0:
            if array[parent_index] > array[current_index]:
                self.swap(parent_index,current_index,array)
            else:
                return
            current_index = parent_index
            parent_index = (current_index-1)//2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0,len(self.heap)-1,self.heap)
        valueRemoved = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        return valueRemoved

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        return self.siftUp(self.heap)
    
    def swap(self,idx1,idx2,heap):
        heap[idx1] = heap[idx1]+heap[idx2]
        heap[idx2] = heap[idx1]-heap[idx2]
        heap[idx1] = heap[idx1]-heap[idx2]
        
        
def isMinHeapPropertySatisfied(array):
        for currentIdx in range(1, len(array)):
            parentIdx = (currentIdx - 1) // 2
            if array[parentIdx] > array[currentIdx]:
                return False
        return True

array1 = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]

minHeap = MinHeap(array1)
print(minHeap.remove())
print(minHeap.peek())
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.heap)
print(minHeap.insert(-8))
print(minHeap.heap)
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.peek())
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.remove())
print(minHeap.insert(8))
print(minHeap.peek())
