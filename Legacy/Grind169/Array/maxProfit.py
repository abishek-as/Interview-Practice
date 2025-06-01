class Solution:
    def maxProfit(self, prices):
        # Edge case: If less than 2 prices, no transaction possible
        if not prices or len(prices) < 2:
            return 0

        # Initialize two pointers:
        # 'buy_day' tracks the day we consider buying the stock (starts at day 0)
        # 'sell_day' scans ahead to find a profitable day to sell
        buy_day = 0
        sell_day = 1

        # Track the best profit seen so far
        max_profit = 0

        # Iterate until the sell_day reaches the end of the price list
        while sell_day < len(prices):
            current_buy_price = prices[buy_day]
            current_sell_price = prices[sell_day]

            if current_sell_price > current_buy_price:
                # Found a profitable transaction
                current_profit = current_sell_price - current_buy_price
                max_profit = max(max_profit, current_profit)
            else:
                # Found a lower price to buy, update buy_day
                buy_day = sell_day

            # Move to the next day
            sell_day += 1

        return max_profit


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Input:", prices1)
    print("Maximum Profit:", solution.maxProfit(prices1))
    print()

    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    print("Input:", prices2)
    print("Maximum Profit:", solution.maxProfit(prices2))
    print()

    # Custom Test
    prices3 = [2, 4, 1]
    print("Input:", prices3)
    print("Maximum Profit:", solution.maxProfit(prices3))
