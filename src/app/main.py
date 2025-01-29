from fastapi import FastAPI
import psycopg2
import uvicorn

from .config import get_settings

cfg = get_settings()

app = FastAPI(title=cfg.app_name,
              openapi_url="/tron/openapi.json",
              docs_url="/tron/swgga",
              redoc_url=None,
              )


@app.get("/")
async def get_last_requests():
    # conn = psycopg2.connect(
    #     host=cfg.db_host,
    #     database=cfg.db_name,
    #     user=cfg.db_user,
    #     password=cfg.db_pass,
    #     port=cfg.db_port,
    # )
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM users")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)
    # cur.close()
    # conn.close()
    return {"message": "Hello World"}

#
# if __name__ == '__main__':
#     uvicorn.run('main:app', host='localhost', port=800, reload=True)
