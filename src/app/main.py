from fastapi import FastAPI, HTTPException

from .config import get_settings
from di_container import get_uc
from .models.dto import TronInfo

cfg = get_settings()
uc = get_uc()

app = FastAPI(title=cfg.app_name,
              openapi_url="/tron/openapi.json",
              docs_url="/tron/swgga",
              redoc_url=None,
              )


@app.get("/requests")
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


@app.post("/request")
async def create_request(address: str) -> TronInfo:
    try:
        res = await uc.create_request(address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return res
