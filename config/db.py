from sqlalchemy import create_engine, MetaData


DATABASE_URL = 'mysql+pymysql://root:@localhost:3306/sale_orders'

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()




