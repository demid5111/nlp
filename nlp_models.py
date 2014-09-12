from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:pass@localhost/nlp')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class HseArticle(Base):
	__tablename__ = 'hse_article'

	id = Column(Integer, primary_key=True)
	uri = Column(String(512),default="",nullable = False)
	interest = Column(String(512),default="",nullable = False)
	elib = Column(String(512),default="",nullable = False)
	keyword = Column(String(512),default="",nullable = False)
	title = Column(String(512),default="",nullable = False)
	abstr = Column(String(512),default="",nullable = False)

	def __repr__(self):
		return "<HseArticle title='{}'>".format(self.title)

class HseAuthor(Base):
	__tablename__ = 'hse_author'

	id = Column(Integer, primary_key=True)
	author_name = Column(String(512),default="",nullable = False)
	article_id = Column(Integer,ForeignKey('hse_article.id'))
	

	def __repr__(self):
		return "<HseAuthor author_name='{}'>".format(self.author_name)