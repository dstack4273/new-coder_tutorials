BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['sraper_app.spiders']

ITEM_PIPELINES = ['scarper_app.pipelines.LivingSocialPipeline']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localahost',
    'port': 5432,
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'database': 'scrape'
}
