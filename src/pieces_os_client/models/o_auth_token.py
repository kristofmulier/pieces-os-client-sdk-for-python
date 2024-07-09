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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class OAuthToken(BaseModel):
    """
    A model representing a returnable response for a OAuthGroup Token  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    access_token: StrictStr = Field(default=..., description="The Access Token")
    token_type: StrictStr = Field(...)
    expires_in: StrictInt = Field(...)
    scope: StrictStr = Field(...)
    refresh_token: Optional[StrictStr] = None
    id_token: Optional[StrictStr] = None
    __properties = ["schema", "access_token", "token_type", "expires_in", "scope", "refresh_token", "id_token"]

    @validator('token_type')
    def token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Bearer'):
            raise ValueError("must be one of enum values ('Bearer')")
        return value

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
    def from_json(cls, json_str: str) -> OAuthToken:
        """Create an instance of OAuthToken from a JSON string"""
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
    def from_dict(cls, obj: dict) -> OAuthToken:
        """Create an instance of OAuthToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthToken.parse_obj(obj)

        _obj = OAuthToken.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "access_token": obj.get("access_token"),
            "token_type": obj.get("token_type"),
            "expires_in": obj.get("expires_in"),
            "scope": obj.get("scope"),
            "refresh_token": obj.get("refresh_token"),
            "id_token": obj.get("id_token")
        })
        return _obj


