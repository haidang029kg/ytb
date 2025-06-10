from fastapi import APIRouter

studio_routes = APIRouter(prefix="/studio")


@studio_routes.get("/info")
async def get_studio_info():
	pass
