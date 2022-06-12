from datetime import datetime
from typing import Optional, List, Union
from pydantic import BaseModel
from bson import ObjectId


class BaseCustomModel(BaseModel):
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class BaseCustomMetaResponse(BaseModel):
    page: int
    per_page: int
    total_data: int


class BaseCustomResponse(BaseModel):
    message: str
    meta: Union[BaseCustomMetaResponse, dict]


class BaseLocErrorValidation(BaseModel):
    loc: List[str]
    msg: str
    type: str


class BaseErrorValidation(BaseModel):
    detail: List[BaseLocErrorValidation]


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
