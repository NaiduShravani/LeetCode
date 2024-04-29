class Solution(object):
    def maxProfit(self, prices):
        #consider prices[i] from right to left 
        #if left smaller than right then take diff
        #max diff< than diff..update max diff return max diff
        '''
        #works only for small array as time complexity increases with nested for loops
        max_diff=0
        
        for left in range(len(prices)-1):
            for right in range(left+1, len(prices)):
                diff= prices[right] - prices[left]
                if (diff>max_diff):
                    max_diff=diff               
        return max_diff  
         '''
        #consider you buy on a certain ith day at prices[i] price, 
        #if prices[j]<prices[i]...you buy at prices[j]
        #else if prices[j]>prices[i] then calc profit= prices[i]-prices[j] >org_profit
        #then sell and return max profit
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit       
