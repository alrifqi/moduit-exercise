from typing import List, Union, Optional
from pydantic import Field, BaseModel


class ModuitQuestionOneSchema(BaseModel):
    id: Optional[Union[int, str]]
    category: Optional[Union[int, str]]
    title: Optional[str]
    description: Optional[str]
    footer: Optional[str]


class ModuitQuestionOneWithTagsSchema(ModuitQuestionOneSchema):
    tags: Optional[List[str]]
    createdAt: Optional[str]

