import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint

# **************************************************************************************************************
# Function  name: expand_df
# input: ingredients contain several ingredients
# return value:
# ***************************************************************************************************************
# Define the function to expand DataFrame based on the number of ingredients
def expand_df(new_data):
    expanded_rows = []
    for index, row in new_data.iterrows():
        ingredients = row['ingredients'].split(', ')  # Split the ingredients string into a list
        for ingredient in ingredients:
            expanded_rows.append({'name': row['name'], 'ingredients': ingredient.strip(), 'diet': row['diet'],'region': row['region']})
    return pd.DataFrame(expanded_rows)

if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Data/indian_food.csv')
    print('*')
    # Filter the data
    new_data = df.loc[(df['region'] != '-1') & (df['region'] != 'Null')]

    # Expand the DataFrame
    expanded_df = expand_df(new_data)
    print(expanded_df)

    # Count occurrences of each ingredient
    ingredient_counts = expanded_df['ingredients'].value_counts()

    # Sort DataFrame based on the number of rows for each ingredient
    sorted_df = expanded_df[expanded_df['ingredients'].isin(ingredient_counts.index)].sort_values(by='ingredients', key=lambda x: ingredient_counts[x['ingredients']], ascending=False) # TODO: Need to check this in order it will work

    sorted_df.to_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Questions/Question_1/preparing_word_cloud.csv', index=False)
    print('*')
