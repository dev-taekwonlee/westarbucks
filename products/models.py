from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length=40)

	class Meta:
		db_table = 'menus'


class Category(models.Model):
	name = models.CharField(max_length=40)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

	class Meta:
		db_table = 'categories'


class Product(models.Model):
	korean_name		= models.CharField(max_length=100)
	english_name	= models.CharField(max_length=100)
	description		= models.TextField(max_length=300)
	category		= models.ForeignKey('Category', on_delete=models.CASCADE)
	allergy			= models.ManyToManyField('Allergy', through='AllergyProduct')

	class Meta:
		db_table = 'products'


class AllergyProduct(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergies_products'


class Allergy(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'allergies'


class Nutrition(models.Model):
	calories_kcal 		= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	saturated_fats_g	= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	protein_g			= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	sodium_mg			= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	sugars_g			= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	caffeine_mg			= models.DecimalField(max_digits=6, decimal_places=2, null=True)
	product				= models.ForeignKey('Product', on_delete=models.CASCADE)
	size				= models.ForeignKey('Size', on_delete=models.CASCADE, null=True)

	class Meta:
		db_table = 'nutritions'


class Image(models.Model):
	image_url	= models.CharField(max_length=2000)
	product		= models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'images'


class Size(models.Model):
	name				= models.CharField(max_length=40)
	size_ml				= models.CharField(max_length=40, null=True)
	size_fluid_ounce	= models.CharField(max_length=40, null=True)

	class Meta:
		db_table = 'sizes'
