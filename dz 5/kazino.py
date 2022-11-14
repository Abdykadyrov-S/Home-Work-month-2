from decouple import config

many = config("MY_MONEY", cast=int)
print(many)