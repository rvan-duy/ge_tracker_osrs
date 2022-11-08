import stats


try:
    prices = stats.get_latest_prices()
    for item in prices:
        print(item, prices[item])
except Exception as e:
    print(e)
