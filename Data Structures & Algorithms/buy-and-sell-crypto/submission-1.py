class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        maxProfit = 0

        for sell in prices[1:]:
            maxProfit = max(maxProfit,sell - minBuy)
            minBuy = min(minBuy,sell)
        return maxProfit








        def old():
            max_profit = 0
            buy_price = prices[0]

            for price in prices:

                buy_price = min(buy_price,price)
                max_profit = max(max_profit,price-buy_price)
            return max_profit
            