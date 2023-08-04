from fastapi import APIRouter

from resources import auth, post

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(post.router)
