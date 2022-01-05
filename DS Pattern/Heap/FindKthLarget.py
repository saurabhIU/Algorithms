class FindKthLargest:
    
    def findKthLargest(self, nums,k) :
        self.heap = self.buildHeap(nums)
        for i in range(0,k-1):
            self.remove(self.heap)
        return self.peek()
    
    def buildHeap(self,array):
        start = (len(array)-1)//2
        for i in range(start,-1,-1):
            self.shiftDown(i,len(array)-1,array)
        return array
    
    def shiftDown(self,start,end,array):
        left = (start*2)+1
        while left<=end:
            right = (start*2)+2
            if right<=end and array[right]>array[left]:
                max_idx = right
            else:
                max_idx = left
            if array[max_idx] > array[start]:
                self.swap(start,max_idx,array)
            start=max_idx
            left = (start*2)+1
        return array
    
    def peek(self):
        return self.heap[0]
    
    def remove(self,heap):
        self.swap(0,len(heap)-1,heap)
        element_removed = heap.pop()
        self.shiftDown(0,len(heap)-1,heap)
        
    
    def swap(self,idx1,idx2,array):
        array[idx1],array[idx2] = array[idx2],array[idx1]


nums = [3,2,3,1,2,4,5,5,6]
handler = FindKthLargest()
print(handler.findKthLargest(nums,1))