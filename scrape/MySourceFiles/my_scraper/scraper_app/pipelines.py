from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table

class LivingSocialPipeline(object):
    """
    LivingSocial pipeline that will take the scraped data and store it
    in the database we built.

    """

    def __init__(self):
        """
        Initializes the database connection and sessionmaker and creates
        the deals table

        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save deals in the database -- this method will be called for every
        item that is returned through out pipeline component. 

        """
        session = self.Session()
        deal = Deals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
