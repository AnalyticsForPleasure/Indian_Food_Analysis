import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint

# **************************************************************************************************************
# Function  name: Retrieving_the_top_12_ingredients_in_each_region
# input:
# return value:
# ***************************************************************************************************************
def Retrieving_the_top_12_ingredients_in_each_region(df_word_cloud):
    global big_df
    # Initialize an empty list to store filtered dataframes
    filtered_dfs = []
    groups_by_region = df_word_cloud.groupby('region')
    for region_name, mini_df_per_region in groups_by_region:
        # print("The team name is: ", region_name)
        # print(mini_df_per_region)
        counter_ingredients = mini_df_per_region['ingredients'].value_counts()
        list_of_top_ingredients_per_region = list(counter_ingredients.index[0:12])

        filtered_df = mini_df_per_region[mini_df_per_region['ingredients'].isin(list_of_top_ingredients_per_region)]
        print('*')

        filtered_dfs.append(filtered_df)

    # Concatenate all filtered dataframes into one big dataframe
    big_df = pd.concat(filtered_dfs)
    # Print the concatenated dataframe
    print(big_df)
    big_df.to_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Questions/Question_1/input_data_tableau_for_word_cloud.csv', index=False)


    return big_df


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df_word_cloud = pd.read_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Questions/Question_1/prepering_word_cloud.csv')
    print('*')

    df_sorted =df_word_cloud.sort_values(by=['region', 'ingredients'], inplace=True)
    print('*')

    res=Retrieving_the_top_12_ingredients_in_each_region(df_word_cloud)
    print('*')


