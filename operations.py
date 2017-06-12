import peewee
from models import *


def add_category(name):
    row = Category(
        name=name.lower().strip(),
    )
    row.save()


def update_category(id, new_name):
    category = Category.get(Category.id == id)
    category.name = new_name
    category.save()


def delete_category(name):
    category = Category.get(Category.name == name.lower().strip())
    category.delete_instance()


def add_product(name, price, category_name):
    cat_exist = True
    try:
        category = Category.select().where(Category.name == category_name.strip()).get()
    except DoesNotExist as de:
        cat_exist = False

    if cat_exist:
        row = Product(
            name=name.lower().strip(),
            price=price,
            category=category
        )
        row.save()


def update_product(id):
    pass


def find_product(name):
    return Product.get(Product.name == name.lower().strip())


def find_all_products():
    prod = Product.select()
    return prod


def find_all_categories():
    return Category.select()


if __name__ == '__main__':

    dbhandle.connect()
    try:
        Category.create_table()
    except peewee.InternalError as px:
        print(str(px))
    try:
        Product.create_table()
    except peewee.InternalError as px:
        print(str(px))

    try:
        add_category('Books')
        add_category('Electronic Appliances')

        # Fetching categories
        categories = find_all_categories()
        for category in categories:
            print(category.name)

        # Adding Products
        add_product('C++ Premier', 24.5, 'books')
        add_product('Juicer', 224.25, 'Electronic Appliances')

        # Retrieve Products
        products = find_all_products()
        product_data = []
        for product in products:
            product_data.append({'title': product.name, 'price': product.price, 'category': product.category.name})

        # Find single Product
        p = find_product('c++ premier')
        print(p.category.name)

        # Update Single Category
        update_category(2, 'Kindle Books')

        # Delete Category
        delete_category('Kindle Books')

    except peewee.InternalError as px:
        print(str(px))
