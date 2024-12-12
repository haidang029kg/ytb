from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.auth.routes import auth_routes
from src.api.studio.routes import studio_routes
from src.db import async_engine, init_db
from src.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
	# Startup: create engine and connect
	logger.info("Starting up and connecting to the database...")
	await init_db()

	yield

	# Shutdown: dispose of the engine
	logger.info("Shutting down and disconnecting from the database...")
	await async_engine.dispose()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
	CORSMiddleware,
	# TODO: Change this to the frontend URL
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/health")
async def health():
	return {"status": "OK"}


app.include_router(auth_routes, tags=["auth"])
app.include_router(studio_routes, tags=["studio"])
