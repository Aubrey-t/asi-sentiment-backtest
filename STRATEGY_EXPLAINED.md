**Kasi Sentiment-Driven Regime Strategy: Methodology Overview**

**Regime Definition & Thresholds**

I use the Kasi Consumer Confidence Index (CCI) to define market regimes. The cutoffs are based on the historical distribution: RISK-ON if CCI is above the 67th percentile, RISK-OFF if below the 33rd, and NEUTRAL in between. With 119 months of data, these thresholds usually land around -10 (33rd) and +5 (67th). So, about a third of the time is spent in each regime.

**Index Selection by Regime**

For each regime, I select JSE sector indices that make sense for the environment:
- RISK-ON: Top 40 TR, Telcos, Consumer Discretionary, Industrials
- RISK-OFF: Healthcare, Financials, Consumer Staples, Telcos
- NEUTRAL: Everything, equal-weighted

The logic is straightforward: growth sectors (Top 40, Discretionary, Industrials) tend to do well when sentiment is strong, while defensives (Healthcare, Financials, Staples) hold up better when confidence is low. Telcos are in both camps—they’re steady regardless of the cycle. I skip sectors in a regime if their return profile doesn’t fit the macro backdrop. For example, Discretionary is out in RISK-OFF because people cut back on non-essentials when they’re worried.

**Momentum-Based Allocation**

Within each regime, I use 6-month momentum to size positions. If all eligible indices have negative or missing momentum, I just split the allocation equally. Otherwise, I allocate in proportion to positive momentum—if an index is lagging, it gets zero. For example, in a RISK-ON month:

- Top 40: +12%
- Telcos: +3%
- Discretionary: -2%
- Industrials: +1%

Total positive: 16. So, Top 40 gets 75%, Telcos 18.75%, Industrials 6.25%, and Discretionary is out. If everything’s negative, it’s 25% each.

**Portfolio Construction & Rebalancing**

Returns are calculated monthly as the weighted sum of the selected indices. I only rebalance when the regime changes—no need to churn the portfolio every month. Allocations stay put until the next shift, which keeps turnover and costs down.

**Performance & Risk Analytics**

I benchmark against the ALSI Total Return and track all the usual stats: annualized and cumulative returns, volatility, Sharpe, beta, capture ratios, and drawdowns. Everything is vectorized in pandas/numpy, and I’ve made sure the code doesn’t break if there’s missing or constant data.

**Sector Correlation & Significance**

I also look at how sectors move together and which ones matter most for both the portfolio and the ALSI. This helps explain what’s driving returns and how diversified the exposures really are.


**Example Output**

Here’s what a typical RISK-ON allocation might look like:

Index                  | 6M Momentum | Weight  
-----------------------|-------------|---------
Top 40 TR              | 12%         | 75%     
Telcos                 | 3%          | 18.75%  
Industrials            | 1%          | 6.25%   
Consumer Discretionary | -2%         | 0%      

Monthly returns are just the weighted sum of these indices for that month.



