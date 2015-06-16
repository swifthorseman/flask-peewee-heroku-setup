from peewee import *

db = SqliteDatabase('tellytubbies.db')

class TellyTubby(Model):
    name = CharField(max_length=20, unique=True)
    colour = CharField(max_length=20)

    class Meta:
        database = db

tellytubbies = [
    {'name': 'Tinky Winky', 'colour': 'Purple'},
    {'name': 'Dipsy', 'colour': 'Green'},
    {'name': 'Laa-Laa', 'colour': 'Yellow'},
    {'name': 'Po', 'colour': 'Red'}
]

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

if __name__ == '__main__':
    db.connect()
    db.create_tables([TellyTubby], safe=True)
    add_tellytubbies()
    retrieved_tellytubbies = retrieve_all()
    for tellytubby in retrieved_tellytubbies:
        print(tellytubby.name)
