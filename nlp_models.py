from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Unicode
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:pass@localhost/nlp', encoding='utf8')
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
	authors = Column(String(1024),default="",nullable=False)
	def __repr__(self):
		return "<HseArticle title='{}'>".format(self.title)

