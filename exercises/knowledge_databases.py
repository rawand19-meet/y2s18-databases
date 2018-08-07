from knowledge_model import Base, Animal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(information,actions_with_humans, types):
	animal_object = Animal(
	information = information,
	actions_with_humans = actions_with_humans,
	types = types)
	session.add(animal_object)
	session.commit()


add_article("""Giraffes feed on seeds
, fruits and a wide variety of vegetation
However, their favorite food is the Acacia,
a tree that has dangerous thorns which giraffes are 
adapted to manage with their thick saliva and prehensile tongue.
	""","""	Giraffes and Humans
Humans have been in contact with giraffes for centuries, 
since the Egyptian civilization to the Roman Empire, were considered exotic gifts to lure foreign diplomats. However
, giraffes have not gotten the best retribution from humans in return.""" ,"""Masai Giraffe,Rothschild Giraffe,
	Reticulated Giraffe,West African Giraffe""")




def query_all_articles():
	animal = session.query(Animal).first()
	return animal
print(query_all_articles())
for i in query_all_articles():
	print (i)

query_article_by_topic()
		

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
