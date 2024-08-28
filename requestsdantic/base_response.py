from typing import TypeVar, Type
from abc import ABC, abstractmethod

from requests import Response
from pydantic import BaseModel, ConfigDict

T_BaseResponse = TypeVar("T_BaseResponse", bound="BaseResponse")

class BaseResponse(BaseModel, ABC):
    model_config = ConfigDict(extra="forbid")

    @property
    @abstractmethod
    def status_code(self) -> int:
        ...

    @classmethod
    def from_response(cls: Type[T_BaseResponse], *, response: Response) -> T_BaseResponse:
        r = cls(data=response.json())
        if r.status_code != response.status_code:
            raise ValueError("Invalid status_code.")
        return r

    # @property
    # @abstractmethod
    # def data(self) -> Any:
    #     ...