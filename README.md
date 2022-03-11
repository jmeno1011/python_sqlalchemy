linchart_model.py 코드 설정
선언된 class
```
class LineChart(Base):
    __tablename__ = 'linechart'
    _idLine = Column(Integer, primary_key=True)
    dogs = Column(Integer, primary_key=True)
    cats = Column(Integer)

    def __init__(self,_idLine, dogs,  cats ):
        self._idLine = _idLine
        self.dogs = dogs
        self.cats = cats
```

return ""안에 값이 app.py에서 instance로 출력된다.
```
# 객체를 문자열로 반환한다.
    def __repr__(self):
        return "_idLine : %d, dogs: %d, cats %d"% (self._idLine, self.dogs, self.cats)
```

app.py 코드 설명
```
# select * from linechart order by _idLine;
for instance in db_session.query(LineChart).order_by(LineChart._idLine):
    print(instance)
```
instance로 값을 받아온다
LineChart는 linechart_model.py에 선언된 class를 불러옴 

```
# select * from linechart where _idLine = 1;
for instance in db_session.query(LineChart).filter(LineChart._idLine==1):
    print(instance)
```
filter를 이용해 where절과 같이 사용할 수 있다.