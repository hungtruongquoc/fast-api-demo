from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import Optional


# Step 3: Define Pydantic Model for `customer` Parameter
class CustomerQueryParam(BaseModel):
    customer: Optional[str] = Field(None, description="Customer query parameter")


# Custom dependency to extract `customer` from query parameters
def customer_dependency(customer: CustomerQueryParam = Depends()):
    return customer


# Step 1 & 2: Subclass APIRouter and modify add_api_route
class AppAPIRouter(APIRouter):
    def add_api_route(self, path: str, endpoint: callable, **kwargs):
        if "dependencies" not in kwargs:
            kwargs["dependencies"] = []
        # Automatically add customer_dependency to all routes
        kwargs["dependencies"].append(Depends(customer_dependency))
        super().add_api_route(path, endpoint, **kwargs)
