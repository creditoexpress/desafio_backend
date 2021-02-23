from fastapi import APIRouter, HTTPException, status, Request, Body
from fastapi.responses import JSONResponse


from ....auth.models import User
from ....auth.services import login as login_user
from ....auth.exceptions import *


router = APIRouter(prefix='/auth')

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
        jwt_secret = request.app.ctx.ioc.get('jwt_secret')
        clients_repository = request.app.ctx.ioc.get('clients_repository')
        token = await login_user(clients_repository, user=user, jwt_secret=jwt_secret)
        return JSONResponse(status_code=status.HTTP_200_OK, content={ 'token': token })
    except Unauthorized as ex:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Cpf and cellphone pair are invalid')
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal Server Error')
