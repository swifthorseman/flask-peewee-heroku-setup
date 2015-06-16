import os
from peewee import *

db_proxy = Proxy()

tellytubbies = [
    {'name': 'Tinky Winky', 'colour': 'Purple'},
    {'name': 'Dipsy', 'colour': 'Green'},
    {'name': 'Laa-Laa', 'colour': 'Yellow'},
    {'name': 'Po', 'colour': 'Red'}
]

class TellyTubby(Model):
    name = CharField(max_length=20, unique=True)
    colour = CharField(max_length=20)

    class Meta:
        database = db_proxy

def add_tellytubbies():
    for tellytubby in tellytubbies:
        try:
            TellyTubby.create(name=tellytubby['name'],
                          colour=tellytubby['colour'])
        except IntegrityError:
            existing_tellytubby = TellyTubby.get(name=tellytubby['name'])
            existing_tellytubby.colour = tellytubby['colour']
            existing_tellytubby.save() 

def retrieve_all():
    results = []
    for tellytubby in TellyTubby.select().order_by(TellyTubby.name):
        results.append(tellytubby)
    return results

# Import modules based on the environment.
# The HEROKU value first needs to be set on Heroku
# either through the web front-end or through the command
# line (if you have Heroku Toolbelt installed, type the following:
# heroku config:set HEROKU=1).
if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('tellytubbies.db')
    db_proxy.initialize(db)


if __name__ == '__main__':
    db_proxy.connect()
    db_proxy.create_tables([TellyTubby], safe=True)
    add_tellytubbies()
    retrieved_tellytubbies = retrieve_all()
    for tellytubby in retrieved_tellytubbies:
        print(tellytubby.name)
