from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# .env 파일에 DB 정보 넣어두기
from dotenv import dotenv_values
config = dotenv_values(".env")

# config는 딕셔너리 타입임 {DB_ID:DB_ID, DB_PW:DB_PW} 이런 상태여서
# 아래와 같이 value 추출
DB_ID = config["DB_ID"]
DB_PW = config["DB_PW"]
DB_END_POINT = config["DB_END_POINT"]
DB = config["DB"]

# 선언적 접근
# mysql사용시
engine = create_engine(
    f'mysql+mysqldb://{DB_ID}:{DB_PW}@{DB_END_POINT}/{DB}', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # import yourapplication.models
    Base.metadata.create_all(bind=engine)
