# webProgrammingHW2

name: CharField with a maximum length of 255 characters.
description: TextField for a longer description of the product.
price: DecimalField with a maximum of 10 digits and 2 decimal places, representing the price of the product.
image: ImageField for uploading product images. It is set to be stored in the 'product_images/' directory and allows null values (null=True) and blank values (blank=True).
category: CharField with a maximum length of 255 characters to store the category of the product.
Based on this model, some assumptions about your project include:

Product Information:

Products have a name, description, price, image, and category.
The name and description provide information about the product.
The price is stored as a decimal value, which is common for handling currency.
Image Handling:

Products can have associated images, which are stored in the 'product_images/' directory.
The null=True, blank=True for the image field suggests that a product may not necessarily have an associated image.
Categorization:

Products are categorized, and the category is stored as a string.

!!!! I tried every solution on youtube and every solutions on internet but ı still had error while ı tried to deploy to python anywhere,because of that ı dont have deployment
And since github pages are only for static pages we cant deploy django app to the github pages.
