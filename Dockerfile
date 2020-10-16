FROM python:3

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install psycopg2 Flask-SQLAlchemy Flask-Migrate
RUN pip install Flask-Alembic


ENTRYPOINT [ "python", "./api.py" ]
