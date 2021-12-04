class Solution:
    def minCost(self, costs):
        return self.minCostRecursive(costs,0,1,1,1)
    
    def minCostRecursive(self,costs,index,idx1,idx2,idx3):
        
        if index == len(costs):
            return 0
        cost1 = 0
        cost2 = 0
        cost3 = 0
        
        if idx1:
            cost1 = costs[index][0] + self.minCostRecursive(costs,index+1,0,1,1)
        if idx2:
            cost2 = costs[index][1] + self.minCostRecursive(costs,index+1,1,0,1)
        if idx3:
            cost3 = costs[index][2] + self.minCostRecursive(costs,index+1,1,1,0)
        
        return min(cost1,cost2,cost3)

sol = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(sol.minCost(costs))