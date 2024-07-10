from fastapi import HTTPException, Request


def get_customer_from_state(request: Request):
    customer = getattr(request.state, 'customer', None)
    if not customer:
        raise HTTPException(status_code=400, detail="Customer parameter is required")
    return customer
