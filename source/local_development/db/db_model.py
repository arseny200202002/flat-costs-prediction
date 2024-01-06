from peewee import *
from .db_conf import DB

db = PostgresqlDatabase(
    DB.NAME,
    user=DB.USER,
    password=DB.PASSWORD,
    host=DB.HOST,
    port=DB.PORT
)

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database=db
        order='id'

class Cities(BaseModel):
    name = CharField(max_length=20)

    class Meta:
        db_table = 'cities'

class Metro(BaseModel):
    name = CharField(max_length=20)

    class Meta:
        db_table = 'metro'

class Districts(BaseModel):
    name = CharField(max_length=20)

    class Meta:
        db_table = 'districts'


class RentFlat(BaseModel):
    date =          DateField(null=False)
    
    city_id =       ForeignKeyField(Cities)
    district_id =   ForeignKeyField(Districts)
    metro_id =      ForeignKeyField(Metro)

    rent_price =    IntegerField(null=False)
    street =        CharField(max_length=50)
    building =      CharField(max_length=20)
    floor =         IntegerField(null=False)
    max_floor =     IntegerField(null=False)
    area =        IntegerField(null=False)
    rooms =         IntegerField(null=False)

    class Meta:
        db_table = 'rentflat'