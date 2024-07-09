# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.mechanism_enum import MechanismEnum

class SeededWebsite(BaseModel):
    """
    This is the minimum information required to create a website for a specific asset.  you can optionally add an asset, or person id to attach this website directly to it  TODO consider updating these asset,format to referenced Models  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    asset: Optional[StrictStr] = Field(default=None, description="This is the specific asset that this website is going to get attached to!!")
    conversation: Optional[StrictStr] = Field(default=None, description="This is the specific conversation that this website is going to get attached to!!")
    url: StrictStr = Field(default=..., description="this is the url of the website.")
    name: StrictStr = Field(default=..., description="name of the website.(customizable and updateable as well.)")
    mechanism: Optional[MechanismEnum] = None
    person: Optional[StrictStr] = Field(default=None, description="this is a uuid of a person that we are going to add the website too.")
    __properties = ["schema", "asset", "conversation", "url", "name", "mechanism", "person"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SeededWebsite:
        """Create an instance of SeededWebsite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededWebsite:
        """Create an instance of SeededWebsite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededWebsite.parse_obj(obj)

        _obj = SeededWebsite.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "asset": obj.get("asset"),
            "conversation": obj.get("conversation"),
            "url": obj.get("url"),
            "name": obj.get("name"),
            "mechanism": obj.get("mechanism"),
            "person": obj.get("person")
        })
        return _obj


