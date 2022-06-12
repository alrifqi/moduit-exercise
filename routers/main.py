import fastapi
from typing import Union, List
from fastapi_utils.inferring_router import InferringRouter

from core.cbv import cbv
from routers._base import BaseApi
from services import main_service
from schema import moduit_schema


main_router = InferringRouter(prefix="/question")


@cbv(main_router)
class MainRouter(BaseApi):
    @main_router.get("/one", response_model=Union[
        moduit_schema.ModuitQuestionOneWithTagsSchema, moduit_schema.ModuitQuestionOneSchema])
    async def get_one(self):
        try:
            data = await main_service.get_endpoint_one()
            return data
        except Exception as err:
            print(err)

    @main_router.get("/two", response_model=Union[
        List[moduit_schema.ModuitQuestionOneWithTagsSchema], List[moduit_schema.ModuitQuestionOneSchema]])
    async def get_two(self):
        try:
            data = await main_service.get_endpoint_two()
            return data
        except Exception as err:
            print(err)

    @main_router.get("/three", response_model=Union[
        List[moduit_schema.ModuitQuestionOneWithTagsSchema], List[moduit_schema.ModuitQuestionOneSchema]])
    async def get_three(self):
        try:
            data = await main_service.get_endpoint_three()
            return data
        except Exception as err:
            print(err)
