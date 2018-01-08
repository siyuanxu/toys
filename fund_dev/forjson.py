import json
import pandas as pd
import matplotlib.pyplot as plt

with open('1.json', 'r') as f:
    data = f.readlines()[0]

data = data.replace("'",'"')

# data = json.loads(data)

data = pd.read_json(data).T

plt.plot(data.total)

plt.show()