import feedparser
import translate
import yaml
from db.models import Headline
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)
ITALIAN_NEWS_RSS = "https://www.ansa.it/sito/ansait_rss.xml"

engine = create_engine(CREDENTIALS['database']['db_url'])
Session = sessionmaker(bind=engine)

feed = feedparser.parse(ITALIAN_NEWS_RSS)
entries = feed['entries']

for entry in entries:
    session = Session()
    headline = Headline(language="italian",
                        original_text=entry['summary'],
                        translated_text=translate.translate_text(entry['summary']))
    session.add(headline)
    session.commit()
