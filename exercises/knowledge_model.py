from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Animal(Base):
    __tablename__'animal'
    ID= Column(Integer,primary_key = True)
    Giraffe_Information= Column(String)
    Giraffes_and_humans = Column(String)
    Types_of_Giraffes = Column(String)
    def __repr__(self):
            return("Animal Giraffe_Information:{}\n"
	 		   "Animal Giraffes_and_humans:{}\n"
	 		   "Animal Types_of_Giraffes:{}\n"	).format(
	 		   self.Giraffe_Information , self.Giraffes_and_humans,self.Giraffes_and_humans)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.