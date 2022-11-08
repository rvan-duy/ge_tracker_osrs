import requests
from items import items_to_track

def get_latest_prices():
    """Get the latest prices of items_to_track from the OSRS Grand Exchange API.
    Returns a dictionary of item names and prices."""
    response = requests.get('https://prices.runescape.wiki/api/v1/osrs/latest')
    data = response.json()
    prices = {}
    for tracked_item in items_to_track.items():
        prices[tracked_item[0]] = {}  # Create a dictionary for each item
        prices[tracked_item[0]]['high'] = data['data'][tracked_item[1]]['high']
        prices[tracked_item[0]]['low'] = data['data'][tracked_item[1]]['low']
    return prices