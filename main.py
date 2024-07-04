from fastapi import FastAPI
from router import router as api_router
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine, base


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(api_router, prefix="/vinyl_database_api")

app.title = 'Vinyl Database API'
app.version = '1.0.0'
app.description = 'A Database API of all of the vinyls I have using FastAPI with a SQL Lite with SQL Alchemy ORM'
base.metadata.create_all(bind=engine)


