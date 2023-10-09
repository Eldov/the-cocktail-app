# Imports
import requests
import pandas as pd

def getDrink(drink_name):
    # Settings for the request,'drink_name' being an input from user
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?"
    querystring = {"s": drink_name}
    
    # Making the request
    response = requests.get(url, params=querystring)
    
    # Jumping into the 'drinks' layer
    drinks = response.json()['drinks']
    
    # Filtering the fields we need
    df = pd.DataFrame(drinks, columns=[
        'idDrink',
        'strDrink',
        'strCategory',
        'strAlcoholic',
        'strGlass',
        'strInstructions',
        'strDrinkThumb',
        'dateModified'])
    
    # Renaming the fields as specified by email
    df = df.set_axis([
        'Id',
        'Name',
        'Category',
        'Alcoholic',
        'Glass',
        'Instructions',
        'Thumbnail',
        'Date Modified'
    ], axis=1)
    
    # Extracting ingredients and their measures from each drink in the drinks response
    ingredients_list = []
    for drink in drinks:
        ingredients = []
        
        for i in range(1, 16):
            ingredient_key = f'strIngredient{i}'
            measure_key = f'strMeasure{i}'
    
            if ingredient_key in drink and measure_key in drink:
                ingredient = drink[ingredient_key]
                measure = drink[measure_key]
    
                if ingredient and measure:
                    ingredients.append(f'{ingredient}: {measure}')
    
        ingredients_list.append(', '.join(ingredients))
    
    # Tranforming the ingredients list into a column in the DataFrame
    df['Ingredients'] = ingredients_list
    
    # Getting the result back to JSON as specified by the email
    return df
