import pytest
from sqlalchemy import create_engine, text


try:
   from config import db_connection_string
except ImportError:
   db_connection_string = "postgresql://username:password@localhost:5432/database"


@pytest.fixture
def db():
   engine = create_engine(db_connection_string)
   connection = engine.connect()
   transaction = connection.begin()


   yield connection


   transaction.rollback()
   engine.dispose()




def test_insert(db):
   db = create_engine(db_connection_string)
   connection = db.connect()
   transaction = connection.begin()


   sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)")
   connection.execute(sql, {"id": 17, "title": "QA Engineering"})


   check_sql = text("SELECT * FROM subject WHERE subject_id = :id")
   result = connection.execute(check_sql, {"id": 17})
   row = result.fetchone()


   assert row is not None
   assert row[1] == "QA Engineering"


   transaction.commit()
   connection.close()


def test_update(db):
   db = create_engine(db_connection_string)
   connection = db.connect()
   transaction = connection.begin()


   sql = text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :id")
   connection.execute(sql, {"new_title": "Alchemy", "id": 17})


   check_sql = text("SELECT subject_title FROM subject WHERE subject_id = :id")
   result = connection.execute(check_sql, {"id": 17})
   updated_title = result.fetchone()[0]


   assert updated_title == "Alchemy"
   assert result.rowcount == 1


   transaction.commit()
   connection.close()


def test_delete(db):
   db = create_engine(db_connection_string)
   connection = db.connect()
   transaction = connection.begin()


   sql = text("DELETE FROM subject WHERE subject_id = :id")
   connection.execute(sql, {"id": 17})


   transaction.commit()
   connection.close()