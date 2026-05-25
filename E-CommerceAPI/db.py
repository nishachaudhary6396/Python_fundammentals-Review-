import json
import os

file_path = 'Product.json'


# LOAD DATA
def load_data() -> dict:

    if not os.path.exists(file_path):

        with open(file_path, 'w') as f:

            json.dump({}, f)

        return {}

    with open(file_path, 'r') as f:

        return json.load(f)


# SAVE DATA
def save_data(data: dict):

    with open(file_path, 'w') as f:

        json.dump(data, f, indent=4)