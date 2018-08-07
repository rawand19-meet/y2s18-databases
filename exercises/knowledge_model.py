from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Animal(Base):
    __tablename__='animal'
    id= Column(Integer,primary_key = True)
    information= Column(String)
    actions_with_humans = Column(String)
    types = Column(String)
    def __repr__(self):
            return("Information:{}\n"
	 		   "Animal actions_with_humans:{}\n"
	 		   "Animal Types:{}\n"	).format(
	 		   self.information , self.actions_with_humans,self.types)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the articlet