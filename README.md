# Multi-Day Strategy Backtest

A single-file, browser-based backtester for a simple moving-average trading rule.
It tests whether the rule would have added value over buying and holding, after trading costs.

**Live use:** open `index.html` in any modern browser. There is no build step and no dependencies.

## What it does

- Runs a **moving-average crossover** rule: hold the asset when the fast average is above the slow average, otherwise hold cash.
- Lets you set the fast average, slow average, and trading cost (basis points per switch).
- Reports strategy vs buy-and-hold on:
  - total return and CAGR
  - Sharpe ratio (zero risk-free rate, 252 trading days)
  - maximum drawdown
  - trade count, closed-trade hit rate, and time in market
- Shows the equity curve, price with both averages, drawdown, and a recent trade log.
- Accepts an uploaded CSV of daily closes (two columns: date, close; at least 250 rows). The file is parsed in the browser and never leaves the machine.

## Method, and why it avoids look-ahead bias

1. The signal is computed from the **close on day t**.
2. The position is entered at that close and earns the return from **t to t+1**. The trade never uses the return it is trading on.
3. Trading cost is charged on every switch in or out.
4. Averages are only used once they are fully defined.

## Verification

- Metrics were recalculated independently in Python on the same price path and match the page to the displayed precision (total return, buy-and-hold return, Sharpe, max drawdown, CAGR, trade count, hit rate, time in market).
- The page renders with no console errors and no horizontal overflow at desktop and phone widths.

## Limitations

- The default data is a **simulated** price path (geometric Brownian motion, seed 7, 22% annual volatility, 750 days). It shows the engine works. It says nothing about any real asset.
- One parameter pair on one history is prone to overfitting. Results are a test of the rule's mechanics, not a recommendation.
- No short selling, leverage, dividends, or slippage beyond the cost input.
- Not investment advice.

## Possible extensions

- Walk-forward testing: choose parameters on one window, evaluate on the next.
- Transaction costs as a function of volume, and a spread model.
- A second strategy (for example, a volatility-targeted position size) for comparison.

## Files

- `index.html`: the complete application (HTML, CSS and JavaScript in one file)
- `README.md`: this file
