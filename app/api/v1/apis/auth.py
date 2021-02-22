from fastapi import APIRouter, HTTPException, status, Request, Body
from fastapi.responses import JSONResponse


from ....auth.models import User
from ....auth.services import authenticate
from ....auth.exceptions import *


router = APIRouter()

@router.post(
    '/login',
    tags=['auth'],
    responses={
        422: {'description': 'cpf or cellphone fields are missing'},
        404: {'description': 'client not found'},
        401: {'description': 'user info does not match'}
    },
    status_code=status.HTTP_200_OK
)
async def login(request: Request, user: User = Body(...)):
    try:
        clients_repository = request.app.ctx.get('clients_repository')
        token = await authenticate(clients_repository, user=user)
        print(token)
        return JSONResponse(status_code=200, content={ 'token': token })
    except ClientNotFound as ex:
        raise HTTPException(404, 'Client not found')
    except Unauthorized as ex:
        raise HTTPException(401, 'Cpf and cellphone pair are invalid')
    except Exception as ex:
        print(ex)
        raise HTTPException(500, 'Server internal error')
