
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint



# if __name__ == '__main__':
#     pd.set_option('display.max_rows', 5000)
#     df = pd.read_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Data/indian_food.csv')
#     #/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Data/indian_food.csv
#     print('*')
#
#

import pandas as pd
# Input DataFrame
data = {
    'Dish name': ['Boondi', 'Lessi','Sheera'],
    'ingredients': [['Gram flour', 'ghee', 'sugar'], ['Yogurt', 'milk', 'nuts', 'nuts', 'sugar'],['Semolina','ghee','nuts','milk']],
    'diet': ['veg', 'veg','veg'],
    'Region': ['West','North','West'],
}

df = pd.DataFrame(data)

# Function to expand DataFrame based on the number of ingredients
def expand_df(df):
    expanded_rows = []
    for index, row in df.iterrows():
        ingredients = row['ingredients']
        for ingredient in ingredients:
            expanded_rows.append({'Dish name': row['Dish name'], 'ingredients': ingredient, 'diet': row['diet'],'Region':row['Region']})
    return pd.DataFrame(expanded_rows)

# Expand the DataFrame
expanded_df = expand_df(df)

print(expanded_df)