import json

OFFER_CODES_FILENAME = "offer_codes.json"

data = None

try:
    with open(OFFER_CODES_FILENAME, 'r') as f:
        offer_codes_list = json.load(f)
except FileNotFoundError:
    print(f"File '{OFFER_CODES_FILENAME}' not found.")
    offer_codes_list = dict()
except json.JSONDecodeError:
    print(f"File '{OFFER_CODES_FILENAME}' contains invalid JSON data.")
    offer_codes_list = dict()