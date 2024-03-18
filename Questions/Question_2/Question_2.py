import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint

###### Info about columns : ##########################################################################
######################################################################################################
# Name - Name of the dish
# Question_1 - Question_1 used in the dish
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


    new_data = df.loc[(df['region'] != '-1') & (df['region'] != 'Null')]

    groups_by_region = new_data.groupby('region')
    for region_name, mini_df_per_region in groups_by_region:
        # print("The team name is: ", region_name)
        # print(mini_df_per_region)
        counter_course = mini_df_per_region['course'].value_counts().reset_index()
        #df['course_difficulty'].value_counts()

        print('*')

    #  Main course, Snack and  Dessert

