import pytest 
from httpx import AsyncClient
from todo_app.api import app
from todo_app.database import engine, SQLModel
import random
import string

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
        
def random_title(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@pytest.mark.asyncio
async def test_create_todo_with_random_title(client: AsyncClient):
    random_todo_title = random_title()
    response = await client.post("/todos/", json={"title": random_todo_title})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == random_todo_title
    assert "id" in data