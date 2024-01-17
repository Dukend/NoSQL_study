import uvicorn
from fastapi import FastAPI
from src.Controller import handle_startup, handle_shutdown
from src.router import router

app = FastAPI()


app.include_router(router, prefix="/main")
app.add_event_handler("startup", handle_startup)
app.add_event_handler("shutdown", handle_shutdown)

print("hello world")
