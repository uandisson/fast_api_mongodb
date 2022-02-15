from fastapi import APIRouter

from logger import log
from model.user_model import User
from service import user_servicer as service

crud_router = APIRouter(
    prefix="/api/v1",
)


@crud_router.get("/")
def index():
    log().info("Welcome!!")
    return {"Welcome!!": "It's alive S2"}


@crud_router.post("/create_user")
def create_user(user_data: User):
    result = service.create_user(user_data=user_data)
    return f"User created: {result}"


@crud_router.put("/update_user")
def create_user(user_data: User):
    service.update_user(user_data=user_data)
    return f"User updated: {user_data}"


@crud_router.delete("/delete_user/{user_id}")
def delete_user(user_id: str):
    service.delete_by_id(user_id)
    return f"User deleted: {user_id}"


@crud_router.get("/list_users")
def get_list_users():
    result = service.get_list_users()
    return {"users list: ": result}


@crud_router.get("/get_user_by_id/{user_id}")
def get_user_by_id(user_id: str):
    result = service.get_user_by_id(user_id)
    return result


@crud_router.get("/get_user_by_name/{user_name}")
def get_user_by_name(user_name: str):
    result = service.get_user_by_name(user_name)
    return result
