import pandas as pd
import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'restaurant_project.settings'
)

django.setup()

from apps.menu.models import Meal, Category

df = pd.read_csv('meals.csv')

for row in df.itertuples():

    category, created = Category.objects.get_or_create(
        name=row.category
    )

    Meal.objects.create(
        name=row.name,
        price=row.price,
        description=row.description,
        image=row.image,
        category=category
    )

print("Data Imported Successfully")