// Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

// The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

// For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

// Example 1:

// Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
// Output: [null,1,1,1,2,1,4,6]
// Explanation:
// First, S = StockSpanner() is initialized.  Then:
// S.next(100) is called and returns 1,
// S.next(80) is called and returns 1,
// S.next(60) is called and returns 1,
// S.next(70) is called and returns 2,
// S.next(60) is called and returns 1,
// S.next(75) is called and returns 4,
// S.next(85) is called and returns 6.

// Note that (for example) S.next(75) returned 4, because the last 4 prices
// (including today's price of 75) were less than or equal to today's price.

// Note:

// Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
// There will be at most 10000 calls to StockSpanner.next per test case.
// There will be at most 150000 calls to StockSpanner.next across all test cases.
// The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

type tuple struct {
	span int
	val  int
}

type StockSpanner struct {
	stack []tuple
}

func Constructor() StockSpanner {
	return StockSpanner{}
}

func (this *StockSpanner) Next(price int) int {
	if this.stack == nil {
		this.stack = append(this.stack, tuple{1, price})
	} else {
		if this.stack[len(this.stack)-1].val > price {
			this.stack = append(this.stack, tuple{1, price})
		} else {
			cur_span := 1
			cur_ind := len(this.stack) - 1
			for cur_ind >= 0 && this.stack[cur_ind].val <= price {
				cur_span += this.stack[cur_ind].span
				cur_ind -= this.stack[cur_ind].span
			}
			this.stack = append(this.stack, tuple{cur_span, price})
		}
	}
	return this.stack[len(this.stack)-1].span
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */