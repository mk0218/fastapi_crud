# fastapi_crud
A simple CRUD example with FastAPI, SQLAlchemy, and PostgreSQL.

## Reference
Followed the official fastapi document.  
https://fastapi.tiangolo.com/tutorial/sql-databases/

## How to demo
Using seperate environment from your host machine is recommended, of course.  
e.g., venv, which is provided by python itself.
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Now, install dependencies and run server.
```
(venv) $ pip install -r requirements.txt
...
(venv) $ uvicorn --reload app.main:app
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
