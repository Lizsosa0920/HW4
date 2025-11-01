# HW4 Stock Market Trading
# this program will read the TESLA stock prices
# it will print each trade's buy and sell price, profit, total profit,
# first buy price, and overall percent return
# -------

# 1st, read tesla prices from TSLA.txt
with open("hw4/TSLA.txt") as file:
  stock_prices = [round(float(line.strip()), 2) for line in file if line.strip() != ""]
  
# 2nd, initialize variables
buy_price = None # current
first_buy_price = None # first price
total_profit = 0 # profit from all the trades

# 3rd, print the header
print("TSLA Mean Reversion Strategy Output: 2024 - 2025 Data")

# 4th, start looping all the prices starting at 5
for i in range(5, len(stock_prices)):
    current_price = stock_prices[i]
    five_day_average = round(sum(stock_prices[i - 5:i]) / 5, 2)

    # BUY: price is 2% below 5 day average
    if current_price < five_day_average * .98:
        if buy_price is None: # buys if not already holding
            buy_price = round(current_price, 2)
            if first_buy_price is None:
                first_buy_price = buy_price
            print(f"buying at: {buy_price:.2f}")

    # SELL: current price is 2% above 5 day average
    elif current_price > five_day_average * 1.02:
        if buy_price is not None: # will sell if currently holding
            sell_price = round(current_price, 2)
            trade_profit = round(sell_price - buy_price, 2)
            total_profit += trade_profit
            print(f"selling at: {sell_price:.2f}")
            print(f"trade profit: {trade_profit:.2f}")
            buy_price = None # resets after selling

# 5th, print the summary section
print()
print(f"Total profit: {round(total_profit, 2):.2f}")

if first_buy_price is not None: # this will check if we bought a stock
    final_profit_percentage = round((total_profit / first_buy_price) * 100, 2)
    print(f"First buy: {first_buy_price:.2f}")
    print(f"% return: {final_profit_percentage:.2f}%")
else: # this will let you know if you didn't buy anything
    print("No trades were made during the simulation")

