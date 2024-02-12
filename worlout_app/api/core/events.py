from typing import Callable

# from buberdinner.app.db.events import close_db_connection, connect_to_db
from fastapi import FastAPI
from loguru import logger

from .settings.app import AppSettings


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    # TODO: connect to db
    return None


async def close_db_connection(app: FastAPI) -> None:
    # TODO: close db connection
    return None


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    async def start_app() -> None:
        await connect_to_db(app, settings)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
