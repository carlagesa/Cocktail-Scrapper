# import requests
# import pandas as pd
# import io
# from PIL import Image
# import base64
# import xlsxwriter

# url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'

# # Set the first letter of the cocktail name to search for
# first_letter = 'a'

# # Set the query parameters for the API request
# params = {'f': first_letter}

# # Send the API request and store the response in a variable
# response = requests.get(url, params=params)

# # Extract the JSON data from the response
# data = response.json()

# # Create a list to store the cocktail data
# cocktails = []

# # Iterate over the cocktails in the JSON data and extract the name, image, and instructions
# for drink in data['drinks']:
#     name = drink['strDrink']
#     image_url = drink['strDrinkThumb']
#     instructions = drink['strInstructions']

#     # Load the image from the URL and save it to a BytesIO object
#     image_response = requests.get(image_url)
#     image_bytes = io.BytesIO(image_response.content)

#     # Open the image using Pillow and resize it to fit in the Excel cell
#     image = Image.open(image_bytes)
#     max_size = (200, 200)
#     image.thumbnail(max_size)

#     # Convert the image to a base64-encoded string
#     image_buf = io.BytesIO()
#     image.save(image_buf, format='PNG')
#     image_data = image_buf.getvalue()
#     image_base64 = base64.b64encode(image_data).decode()

#     # Add the cocktail data to the list of cocktails
#     cocktails.append({'name': name, 'image': image_base64, 'instructions': instructions})

# # Create a DataFrame from the list of cocktails
# df = pd.DataFrame(cocktails)

# # Set up the XlsxWriter engine and worksheet
# writer = pd.ExcelWriter('cocktails.xlsx', engine='xlsxwriter')
# workbook = writer.book
# worksheet = workbook.add_worksheet('Cocktails')

# # Set the width of the columns to fit the data
# worksheet.set_column('A:A', 30)
# worksheet.set_column('B:B', 20)
# worksheet.set_column('C:C', 50)

# # Write the column headers to the worksheet
# worksheet.write('A1', 'Name')
# worksheet.write('B1', 'Image')
# worksheet.write('C1', 'Instructions')

# # Iterate over the cocktails and write the data to the worksheet
# for i, cocktail in enumerate(cocktails):
#     # Write the name and instructions to the worksheet
#     worksheet.write(i + 1, 0, cocktail['name'])
#     worksheet.write(i + 1, 2, cocktail['instructions'])

#     # Write the image to the worksheet as a base64-encoded string
#     image_base64 = cocktail['image']
#     image_data = base64.b64decode(image_base64)
#     image_buf = io.BytesIO(image_data)
#     worksheet.insert_image(i + 1, 1, 'image.png', {'image_data': image_buf})

# # Save the worksheet and close the workbook
# writer.save()




# import requests
# import pandas as pd

# url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'

# # Set the first letter of the cocktail name to search for
# first_letter = 'a'

# # Set the query parameters for the API request
# params = {'f': first_letter}

# # Send the API request and store the response in a variable
# response = requests.get(url, params=params)

# # Extract the JSON data from the response
# data = response.json()

# # Create a DataFrame from the 'drinks' list in the JSON data
# df = pd.DataFrame(data['drinks'])

# # Save the DataFrame to an Excel file
# writer = pd.ExcelWriter('cocktails.xlsx', engine='xlsxwriter')
# df.to_excel(writer, index=False)
# writer.save()


import requests
import pandas as pd

url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
# params = {'s': 'a'}
# params = {'s': ''}
# loop through letters a-z
for letter in 'abcdefghijklmnopqrstuvwxyz':
    params = {'s': letter}
    response = requests.get(url, params=params)
    data = response.json()


# iterate through alphabets a to z
# for letter in range(97, 123):
#     # set the value of the s parameter for the current search
#     params['s'] = chr(letter)
#     # make the API request with the current search query
#     response = requests.get(url, params=params)
#     # process the response data as needed
#     data = response.json()

# response = requests.get(url, params=params)

# data = response.json()

cocktails = []
for cocktail_data in data['drinks']:
    cocktail = {
        'drink': cocktail_data['strDrink'],
        'DrinkAlternate': cocktail_data['strDrinkAlternate'],
        'Tags': cocktail_data['strTags'],
        'category': cocktail_data['strCategory'],
        'IBA': cocktail_data['strIBA'],
        'alcoholic': cocktail_data['strAlcoholic'],
        'glass': cocktail_data['strGlass'],
        'instructions': cocktail_data['strInstructions'],
        'image': cocktail_data['strDrinkThumb'],
        'Ingredient1': cocktail_data['strIngredient1'],
        'Ingredient2': cocktail_data['strIngredient2'],
        'Ingredient3': cocktail_data['strIngredient3'],
        'Ingredient4': cocktail_data['strIngredient4'],
        'Ingredient5': cocktail_data['strIngredient5'],
        'Ingredient6': cocktail_data['strIngredient6'],
        'Ingredient7': cocktail_data['strIngredient7'],
        'Ingredient8': cocktail_data['strIngredient8'],
        'Ingredient9': cocktail_data['strIngredient9'],
        'Ingredient10': cocktail_data['strIngredient10'],
        'Measure1': cocktail_data['strMeasure1'],
        'Measure2': cocktail_data['strMeasure2'],
        'Measure3': cocktail_data['strMeasure3'],
        'Measure4': cocktail_data['strMeasure4'],
        'Measure5': cocktail_data['strMeasure5'],
        'Measure6': cocktail_data['strMeasure6'],
        'Measure7': cocktail_data['strMeasure7'],
        'Measure8': cocktail_data['strMeasure8'],

    }
    cocktails.append(cocktail)

df = pd.DataFrame(cocktails)

writer = pd.ExcelWriter('cocktails.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()
