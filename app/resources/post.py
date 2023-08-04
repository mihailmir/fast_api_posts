import random
from fastapi import APIRouter, status
from schemas.request.posts import PostCreateRequest
from schemas.response.posts import PostResponse, PostListResponse

router = APIRouter(prefix="/posts")


@router.post(
    "/add-post/",
    status_code=status.HTTP_201_CREATED,
    response_model=PostResponse
)
async def create_post(
    user_data: PostCreateRequest,
):
    # create posts logic here
    return {"id": random.randint(0, 100)}


@router.get(
    "/",
    response_model=PostListResponse,
    status_code=status.HTTP_200_OK,
)
async def posts_list():
    # fetch posts logic here
    # posts
    posts = [{'id': 1, 'text': 'First Post'}, {'id': 2, 'text': 'Second post'}]
    print(posts)
    return {"posts": posts}

