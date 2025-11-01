# HW4 Stock Market Trading
# this program will read the TESLA stock prices
# it will print each trade's buy and sell price, profit, total profit,
# first buy price, and overall percent return
# -------

# First, read tesla prices from TSLA.txt
with open(r"hw4/TSLA.txt") as file:
  stock_prices = [round(float(line.strip()), 2) for line in file if line.strip() != ""]
