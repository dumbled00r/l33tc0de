"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
"""


class StockSpanner:
    #
    # def __init__(self):
    #     self.stack = []
    #     self.stack2 = []
    #     self.tempAns = []
    #     self.index = 0
    #     pass
    #
    # def next(self, price: int) -> int:
    #     ans = 1
    #     while self.stack and self.stack2 and self.stack2[-1] <= price:
    #         idx = self.stack.pop()
    #         self.stack2.pop()
    #         ans = self.index - idx + self.tempAns[idx]
    #     self.stack.append(self.index)
    #     self.stack2.append(price)
    #     self.index += 1
    #     self.tempAns.append(ans)
    #     return ans


    ### little bit better solution

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, ans))
        return self.stack[-1][1]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    obj = StockSpanner()
    print(obj.next(100))
    print(obj.next(80))
    print(obj.next(60))
    print(obj.next(70))
    print(obj.next(60))
    print(obj.next(75))
    print(obj.next(85))