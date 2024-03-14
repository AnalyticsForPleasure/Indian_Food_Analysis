import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint

###### Info about columns : ##########################################################################
######################################################################################################
# Name - Name of the dish
# Ingredients - Ingredients used in the dish
# Diet - Vegetarian/NonVegetarian
# Prep_time - Time consumed in preparation of the dish
# Cook_time -  Time consumed in cooking the dish
# Flavor_profile - Sweet/Spicy/other flavor profile
# Course - Main Course/ Dessert /Starters
# State - Indian State where the dish originated
# Region -  Region in which the dish originated
# Img_url -  URL for the image of dish


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Indian_Food_Analysis/Data/indian_food.csv')
    print('*')

    unique_region = pd.unique(df['region'])
    print(unique_region)
    print('*')

    # Taking the data only  with region ( not taking the '-1' region )
    new_data = df.loc[df['region'] != '-1', :]
    new_data = new_data.loc[df['region'] != 'Null', :]
    print('*')


    all_diet_categories = ['vegetarian','non vegetarian']
    # Split the string in each row by comma and convert to list
    new_data['Total time'] = new_data.loc[:, 'prep_time'] + new_data.loc[:, 'cook_time']
    print('*')
    # Filter number 1: Filtering by region
    groups_by_region = new_data.groupby('region')
    for region_name, mini_df_region in groups_by_region:
        #print("The region name is: ", region_name)
        amount_of_flavor_at_each_region = mini_df_region['flavor_profile'].value_counts().reset_index()
        # mini_df_region.sort_values(by = ['Total time'] , ascending=False,inplace=True)
        # print(amount_of_flavor_at_each_region)

        # Filter number 2: Filtering by diet_category
        for diet_category in all_diet_categories:
            print("The region name is: ", region_name, "Type: ",diet_category )
            filtered_data_by_region_diet = mini_df_region.loc[mini_df_region['diet']== diet_category, :]
            print('*')


            ingredient_lists = mini_df_region['ingredients'].str.split(',').tolist()
            # Flatten the list of lists and remove leading/trailing spaces
            all_ingredients = [ingredient.strip() for sublist in ingredient_lists for ingredient in sublist]
            pprint(Counter(all_ingredients))

            # print(all_ingredients)
