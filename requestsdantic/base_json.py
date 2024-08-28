from abc import ABC

from pydantic import BaseModel, ConfigDict

class BaseJSON(BaseModel, ABC):
    model_config = ConfigDict(extra="forbid")
