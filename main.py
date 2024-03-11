import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



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

    # Split the string in each row by comma and convert to list
    ingredient_lists = df['ingredients'].str.split(',').tolist()

    # Flatten the list of lists and remove leading/trailing spaces
    all_ingredients = [ingredient.strip() for sublist in ingredient_lists for ingredient in sublist]

    print(all_ingredients)