from declarative_database import init_db, db_session
from linechart_model import LineChart

init_db()

# insert query
# insert into linechart(_idLine, dogs, cats) values(9, 1, 1);
# l = LineChart(9,1,1)
# db_session.add(l)
# db_session.commit()

# select * from linechart order by _idLine;
for instance in db_session.query(LineChart).order_by(LineChart._idLine):
    print(instance)

# select * from linechart where _idLine = 1;
for instance in db_session.query(LineChart).filter(LineChart._idLine==1):
    print(instance)