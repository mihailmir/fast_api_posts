from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.routes import api_router


app = FastAPI(
    title="Fast Api test",
    redoc_url=None,
    docs_url=None,  # we customize this ourselves
)

app.include_router(api_router)

# set up CORS
cors_list = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

