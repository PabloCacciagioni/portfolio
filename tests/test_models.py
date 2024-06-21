from sqlmodel import Session, create_engine
from todo_app.models import Todo

engine = create_engine('postgresql://todouser:todopass@localhost:5432/tododb')

def test_saving_todo():
    with Session(engine) as session:
        todo = Todo(title="Sample Book")
        session.add(todo)
        session.commit()