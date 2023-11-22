import datetime

import jwt

import settings

payload = {
    "my_name": "Timur",
    "age": 16,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=60),
}


def encode_jwt(cargo: dict) -> str:
    return jwt.encode(
        payload=cargo,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )


def decoded_jwt(raw_jwt: str) -> dict:
    try:
        result = jwt.decode(
            raw_jwt,
            settings.JWT_SECRET,
            algorithms=["HS256"],
            options={
                'verify_signature': False,
            }
        )
        return result
    except jwt.exceptions.ExpiredSignatureError:
        return {}
    except jwt.exceptions.InvalidSignatureError:
        return {}


print(encode_jwt(cargo=payload))
print(decoded_jwt(raw_jwt=encode_jwt(cargo=payload)))
