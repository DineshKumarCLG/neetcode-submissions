class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_buy=prices[0]
        # max_profit=0
        # for price in prices:
        #     max_profit=max(max_profit, price-min_buy)
        #     min_buy=min(min_buy,price)
        # return max_profit

        l,r=0,1
        maxP=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP
