import requests

import json



API_KEY = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2TmpFeU16ZzNMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuX3B5RFJhM05yUk5CbHRnVDVvM1huVjdQV2dxd2p1cXhlX1A0V3hJZVR1cXE2NFhBa1BRcHRIYVVmVHNRUHEybU93V1BMaXJOLWZIdnEzZWFudGtzTnc="

intgration_id = 3033362

order_id = 252530


amount = 45060

payment_method = "PAYMOB_TEST"

headers0 = {"Content-Type": "application/json"}


def print_response(response, stage="step"):
   

    print(
        "=" * 50
        + f"{stage} started"
        + json.dumps(response, indent=2)
        + "\n"
        + f"{stage} finished"
        + "=" * 100
        + "\n"
    )


def first_step(api_key=API_KEY):
    
    data = {"api_key": api_key}
    headers = headers0
    response = requests.post(
        "https://accept.paymob.com/api/auth/tokens", headers=headers, json=data
    )
    token = response.json().get("token")
    # debug
    return token


# second step
def secound_step(token, headers=headers0, amount=amount):
    data = {
        "auth_token": token,
        "delivery_needed": "false",
        "amount_cents": amount*100,
        "currency": "EGP",
        "items": [
            {
                "name": "ASC1515",
                "amount_cents": "500000",
                "description": "Smart Watch",
                "quantity": "1",
            }
        ]
    }

    headers = headers0
    request = requests.post(
        "https://accept.paymob.com/api/ecommerce/orders", headers=headers, json=data
    )
    response = request.json()
    return response.get("id"), token





def third_Step(integration_id, order_id, token, headers=headers0, amount=amount):
    integration_id = intgration_id
    data = {
        "auth_token": token,
        "amount_cents": amount*100,
        "expiration": 3600,
        "order_id": order_id,
        "billing_data": {
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+86(8)9135210487",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah",
        },
        "currency": "EGP",
        "integration_id": integration_id,
    }

    headers = headers0

    request = requests.post(
        "https://accept.paymob.com/api/acceptance/payment_keys",
        headers=headers,
        json=data,
    )

    response = request.json()

    return response.get("token")


