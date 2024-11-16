import csv
from ast import literal_eval

data = []

with open('Food Ingredients and Recipe Dataset with Image Name Mapping.csv', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    for row_i, row in enumerate(csv_reader):
        if row_i == 0: continue
        index, title, ingredients_raw, instructions, image_name, cleaned_ingredients_raw = row
        ingredients = literal_eval(ingredients_raw)
        cleaned_ingredients = literal_eval(cleaned_ingredients_raw)
        data.append({
            'index': index,
            'title': title,
            'ingredients_raw': ingredients_raw,
            'instructions': instructions,
            'image_name': image_name,
            'cleaned_ingredients_raw': cleaned_ingredients_raw,
        })
        # print('\n\n'.join(row)) 

# print(list(data.values())[:10])

if __name__ == '__main__':
    suscakes = [row for row in data if 'cake' in row['title'].lower()]
    cakes = [recipe for recipe in suscakes if not any(bad in recipe['title'].lower() for bad in ['cupcake', 'pancake'])] 
    print(len(cakes))
    print([cake['title'] for cake in cakes])
