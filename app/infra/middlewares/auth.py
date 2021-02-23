from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError, DecodeError

from ..app_factory import create_app
from ...auth.services import authenticate


FIRST = 0

app = create_app()



def extract_token(authorization: str) -> str:
    values = authorization.split(' ')
    values.pop(FIRST)
    return values[FIRST] if values else ''


@app.middleware('http')
async def authenticate_user(request: Request, call_next):
    try:
        token = extract_token(authorization=request.headers.get('authorization'))
        if not token:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content='Auth token is required')

        jwt_secret = request.app.ctx.ioc.get('jwt_secret')
        cpf = await authenticate(token=token, jwt_secret=jwt_secret)

        request.scope['client_cpf'] = cpf
        response = await call_next(request)
        return response
    except (InvalidSignatureError, DecodeError) as ex:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content='Invalid auth token')
    except ExpiredSignatureError as ex:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content='Auth token is expired. Please, execute the login again and generate a new token'
        )