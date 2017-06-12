from peewee import *
import datetime

user = 'root'
password = 'root'
db_name = 'peewee_demo'

dbhandle = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)


class BaseModel(Model):
    class Meta:
        database = dbhandle


class Category(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "categories"
        order_by = ('created_at',)


class Product(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    price = FloatField(default=None)
    category = ForeignKeyField(Category, related_name='fk_cat_prod', to_field='id', on_delete='cascade',
                               on_update='cascade')
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "products"
        order_by = ('created_at',)
