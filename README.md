## Super Shop Management System

This is a super shop management system with basic functionalities, like managing products and orders. For this project Python is used with Django framework and for database management used SQLite.

# Installation

For installing this project, Virtual Environment is recommended. So lets setup the virtual environment,
Open your Terminal and run this command:
```
    mkdir Django_Project
    cd Django_Project
    sudo apt-get install python3-venv
    python3 -m venv myvenv
    source myvenv/bin/activate
```
Now virtual environment is activated, its time for cloneing the project. for this run this command bellow,
```
    git clone https://github.com/RubelBiswasCS/shop-management
```

Now cd into the project directory
```
    cd shop-management
```
Install dependencies,
```
    pip install --upgrade pip
    pip install -r requirements.txt
```
at this point the requirment up-to-date.lets do the migrations by runnning those command
```
    python manage.py makemigrations
    python manage.py migrate
```
As migration done, lets create a superuser for this application. For doing so run the commend down bellow and give proper credentials as required.
```
    python manage.py createsuperuser
```    
Now you can run this application by running
```
    python manage.py runserver
```
Now the site is running on localhost at port 8000, port no may be varied on user. in my case its 8000. In you browser the site is live on http://127.0.0.1:8000/.

# How to Use

While running this application on you browser, you will find the home page having 3 div/column. in the left div you will 2 options, one for Product Management and other is Order Management. On the right div/side there is sub option of each of the Option(Management/Order Management). On the center of the website data tabel or input form will be displayed.

## Product Management

For product management,
1. click on the 'Product Management' button

on the Right side of the browser all available option for product management will displayed.
For adding product

1. click on "Add Product" Button

a form will be displayed. There are field for your product information, after entering data in the form click "Submit" and data will be saved on database. For viewing the products you have added.

3. click on "All Product" Button

Information about you product will be displayed on a table as you clicked "All Product" Button

4. click on "Update Product" Button

for updating you product information click on "Update Product" Button. Information about you all product will be displayed in a tabel with a Button named "Update" on the very right column for each product. click on the button("Update"). You will find a form your selected product information. Edit as required. Then click "Submit" at the very bottom of the form. You data will be upodated and you will be redireact to update product page.

5. click on "Delete Product" Button

for deleting your product click on "Delete Product" Button. a table will be displayed as before but now with "Red button". Click on the button if you wish to delete the product. as you click "Delete" button it will ask you for comfirmation of the delete. Click "Yes" button for delete.

## Order Management

6. click on "Order Management" Button

click on the "Order Management" on the Right side of the browser. you will find 2 option on the left side named "Create Order" and "Order History".

7. click on "Create Order" button 

for creating a new order. a form will be appeared , it will ask for Customer information, fill them and click on "Add Item". You will get youself on the next page. Where you can pick available product form the dropdown manu, select the product and fill the quantity field the click "Add item". Your item will be saved and displayed just bellow. after adding required products click "Get Invoice" for a PDF invoice. All information about your product will be on the invoice and information about the customer and other will also be on it as Bar Code.

8. click on "Order History" button

for information about all existing orders click "Order History" button. All order history will be displayed on a tabel. There will be another button "Details" for viewing order details Click it if you want. You can also get invoice from here.









