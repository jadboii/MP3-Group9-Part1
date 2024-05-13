# Inserts a new entry into the database
from app import Pet, db
snowball = Pet(name='Snowball', species='Cat')
_________
db.session.commit()
snowball.id