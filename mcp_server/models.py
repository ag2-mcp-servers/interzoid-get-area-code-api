# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:51:17+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class GetareacodeGetResponse(BaseModel):
    Abbreviation: Optional[str] = None
    AreaCode: Optional[str] = None
    Code: Optional[str] = None
    Credits: Optional[str] = None
    Locale: Optional[str] = None
    PrimaryCity: Optional[str] = None
