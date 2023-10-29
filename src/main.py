from fastapi import FastAPI

app = FastAPI()


@app.on_event('startup')
async def server_startup():
    print('Started pokemon server...')


@app.on_event('shutdown')
async def server_shutdown():
    print('Pokemon server shutting down...')