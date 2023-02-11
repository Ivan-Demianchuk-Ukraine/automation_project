import json
with open('config.json') as f:
    config = json.load(f)
base_url = config['base_url']