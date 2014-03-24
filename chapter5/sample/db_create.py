# db_create.py


from app import db
from app.models import FTasks
from datetime import date

# create the database and the db table
db.create_all()

# insert data
db.session.add(FTasks("Finish this tutorial", date(2013, 3, 13), 10, 1))
db.session.add(FTasks("Finish my book", date(2013, 3, 13), 10, 1))

# commit the changes
db.session.commit()