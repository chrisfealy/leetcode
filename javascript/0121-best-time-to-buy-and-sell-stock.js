var maxProfit = function(prices) {
    let [l, r, maxProfit] = [0, 1, 0]
    while (r < prices.length) {
        if (prices[r] > prices[l]) {
            profit = prices[r] - prices[l]
            maxProfit = Math.max(profit, maxProfit)
        }
        else {
            l = r
        }
        r++
    }
    return maxProfit
};
