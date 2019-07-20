from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker


class School(object):
    pass

db = create_engine('sqlite:///schools.db', echo=False)

metadata = MetaData(db)

SchoolTable = Table('schools', metadata, autoload=True)
accountsmapper = mapper(School, SchoolTable)
Table()
Session = sessionmaker(autoflush=True, autocommit=True)
session = Session()
firstSchool = session.query(School).first()
print(firstSchool.fullname, firstSchool.country)
firstSchool.country = 'U.S.'                        # changed the country attribute
session.flush()                                     # persisted the data
session.close()

session = Session()
school = session.query(School).first()
print(school.fullname, school.country)
session.close()

session = Session()
firstSchool = session.query(School).first()
firstSchool.country = 'USA'
print(firstSchool.fullname, firstSchool.country)
session.flush()
session.close()
