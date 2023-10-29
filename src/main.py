from fastapi import FastAPI

from src.api.v1 import app_v1
from src.api.v2 import app_v2

app = FastAPI()

# Mount version v1 as sub-application
app.mount('/v1/', app_v1)

# Mount version v2 as sub-application
app.mount('/v2/', app_v2)


# This method is triggered at the startup event of the application.
@app.on_event('startup')
async def server_startup():
    print('Started pokemon server...')


# This method is triggered at the shutdown event of the application
@app.on_event('shutdown')
async def server_shutdown():
    print('Pokemon server shutting down...')
