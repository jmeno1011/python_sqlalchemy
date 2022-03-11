from sqlalchemy import Column, Integer
from declarative_database import Base

class LineChart(Base):
    __tablename__ = 'linechart'
    _idLine = Column(Integer, primary_key=True)
    dogs = Column(Integer, primary_key=True)
    cats = Column(Integer)

    def __init__(self,_idLine, dogs,  cats ):
        self._idLine = _idLine
        self.dogs = dogs
        self.cats = cats

# 객체를 문자열로 반환한다.
    def __repr__(self):
        # 문자열 포맷팅
        # %s : String
        # %c : charactre
        # %d : integer
        # %f : float
        return "_idLine : %d, dogs: %d, cats %d"% (self._idLine, self.dogs, self.cats)

