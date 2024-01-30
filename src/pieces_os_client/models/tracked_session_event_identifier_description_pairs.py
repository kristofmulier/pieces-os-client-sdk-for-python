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
from pydantic import BaseModel, Field, StrictStr, validator
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class TrackedSessionEventIdentifierDescriptionPairs(BaseModel):
    """
    These are all of the available event types that are permitted in an object pair notation.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    session_initialized: Optional[StrictStr] = Field(None, description="The key value pair for an application being opened.")
    session_local_connection_succeeded: Optional[StrictStr] = Field(None, description="There was a successful connection locally")
    session_local_connection_failed: Optional[StrictStr] = Field(None, description="There was a failed connection locally")
    session_inactive: Optional[StrictStr] = Field(None, description="If the current application is in the background or not, could also be minimized.")
    session_active: Optional[StrictStr] = Field(None, description="If the application has been brought to the forground.")
    session_terminated: Optional[StrictStr] = Field(None, description="If the user has closed the application, thus ending the session.")
    session_authenticated_with_sign_in: Optional[StrictStr] = Field(None, description="A user has signed into this session with a an external account")
    session_unauthenticated_with_sign_out: Optional[StrictStr] = Field(None, description="A user has signed out of this session")
    session_unauthenticated_with_dismiss: Optional[StrictStr] = Field(None, description="A user did not sign into the session with a dismissal")
    session_unauthenticated_with_remind: Optional[StrictStr] = Field(None, description="A user did not sign into the session with a reminder")
    session_onboarding_initialized: Optional[StrictStr] = Field(None, description="Onboarding has been initialized for this session")
    session_onboarding_completed: Optional[StrictStr] = Field(None, description="Onboarding has been completed for this session")
    __properties = ["schema", "session_initialized", "session_local_connection_succeeded", "session_local_connection_failed", "session_inactive", "session_active", "session_terminated", "session_authenticated_with_sign_in", "session_unauthenticated_with_sign_out", "session_unauthenticated_with_dismiss", "session_unauthenticated_with_remind", "session_onboarding_initialized", "session_onboarding_completed"]

    @validator('session_initialized')
    def session_initialized_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_session_has_been_initialized_and_the_application_has_been_opened'):
            raise ValueError("must be one of enum values ('a_session_has_been_initialized_and_the_application_has_been_opened')")
        return value

    @validator('session_local_connection_succeeded')
    def session_local_connection_succeeded_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('one_or_more_applications_has_successfully_connected'):
            raise ValueError("must be one of enum values ('one_or_more_applications_has_successfully_connected')")
        return value

    @validator('session_local_connection_failed')
    def session_local_connection_failed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('one_or_more_applications_has_failed_to_connect_locally'):
            raise ValueError("must be one of enum values ('one_or_more_applications_has_failed_to_connect_locally')")
        return value

    @validator('session_inactive')
    def session_inactive_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_session_is_inactive_because_the_application_is_not_in_the_foreground'):
            raise ValueError("must be one of enum values ('a_session_is_inactive_because_the_application_is_not_in_the_foreground')")
        return value

    @validator('session_active')
    def session_active_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_session_is_active_because_the_application_is_in_the_foreground'):
            raise ValueError("must be one of enum values ('a_session_is_active_because_the_application_is_in_the_foreground')")
        return value

    @validator('session_terminated')
    def session_terminated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_session_has_been_ended_and_the_application_has_been_closed'):
            raise ValueError("must be one of enum values ('a_session_has_been_ended_and_the_application_has_been_closed')")
        return value

    @validator('session_authenticated_with_sign_in')
    def session_authenticated_with_sign_in_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_user_has_signed_into_this_session_with_a_an_external_account'):
            raise ValueError("must be one of enum values ('a_user_has_signed_into_this_session_with_a_an_external_account')")
        return value

    @validator('session_unauthenticated_with_sign_out')
    def session_unauthenticated_with_sign_out_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_user_has_signed_out_of_this_session'):
            raise ValueError("must be one of enum values ('a_user_has_signed_out_of_this_session')")
        return value

    @validator('session_unauthenticated_with_dismiss')
    def session_unauthenticated_with_dismiss_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_user_did_not_sign_into_the_session_with_a_dismissal'):
            raise ValueError("must be one of enum values ('a_user_did_not_sign_into_the_session_with_a_dismissal')")
        return value

    @validator('session_unauthenticated_with_remind')
    def session_unauthenticated_with_remind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_user_did_not_sign_into_the_session_with_a_reminder'):
            raise ValueError("must be one of enum values ('a_user_did_not_sign_into_the_session_with_a_reminder')")
        return value

    @validator('session_onboarding_initialized')
    def session_onboarding_initialized_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('onboarding_has_been_initialized_for_this_session'):
            raise ValueError("must be one of enum values ('onboarding_has_been_initialized_for_this_session')")
        return value

    @validator('session_onboarding_completed')
    def session_onboarding_completed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('onboarding_has_been_completed_for_this_session'):
            raise ValueError("must be one of enum values ('onboarding_has_been_completed_for_this_session')")
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
    def from_json(cls, json_str: str) -> TrackedSessionEventIdentifierDescriptionPairs:
        """Create an instance of TrackedSessionEventIdentifierDescriptionPairs from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TrackedSessionEventIdentifierDescriptionPairs:
        """Create an instance of TrackedSessionEventIdentifierDescriptionPairs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackedSessionEventIdentifierDescriptionPairs.parse_obj(obj)

        _obj = TrackedSessionEventIdentifierDescriptionPairs.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "session_initialized": obj.get("session_initialized"),
            "session_local_connection_succeeded": obj.get("session_local_connection_succeeded"),
            "session_local_connection_failed": obj.get("session_local_connection_failed"),
            "session_inactive": obj.get("session_inactive"),
            "session_active": obj.get("session_active"),
            "session_terminated": obj.get("session_terminated"),
            "session_authenticated_with_sign_in": obj.get("session_authenticated_with_sign_in"),
            "session_unauthenticated_with_sign_out": obj.get("session_unauthenticated_with_sign_out"),
            "session_unauthenticated_with_dismiss": obj.get("session_unauthenticated_with_dismiss"),
            "session_unauthenticated_with_remind": obj.get("session_unauthenticated_with_remind"),
            "session_onboarding_initialized": obj.get("session_onboarding_initialized"),
            "session_onboarding_completed": obj.get("session_onboarding_completed")
        })
        return _obj


