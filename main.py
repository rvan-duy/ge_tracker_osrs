import stats

prices = stats.get_latest_prices()
for item in prices:
    print(item, prices[item])