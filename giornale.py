import feedparser
import translate
import yaml
from db.models import Translation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)
ENGLISH_RSS = "https://voxeurop.eu/en/feed/rss/all.xml"
ITALIAN_RSS = "https://voxeurop.eu/it/feed/rss/all.xml"

engine = create_engine(CREDENTIALS['database']['db_url'])
Session = sessionmaker(bind=engine)

en_feed = feedparser.parse(ENGLISH_RSS)
it_feed = feedparser.parse(ITALIAN_RSS)


def get_image_link(list_of_json):
    # used as imperfect key of same article cross-language
    return [json_element['href']
            for json_element in list_of_json
            if json_element['type'] == 'image/jpeg'][0]


it_pairs = {get_image_link(row['links']): row['title'] for row in it_feed['entries']}
en_pairs = {get_image_link(row['links']): row['title'] for row in en_feed['entries']}

for key, original_text in it_pairs.items():
    session = Session()

    try:
        translated_text = en_pairs[key]
    except KeyError:
        continue

    headline = Translation(language="italian",
                           original_text=original_text,
                           translated_text=translated_text)
    session.add(headline)
    session.commit()
