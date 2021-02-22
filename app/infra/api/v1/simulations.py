from ...middlewares.auth import app
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

@app.post(
    '/',
    tags=['simulation'],
    responses={
        422: {'description': 'cpf or cellphone fields are missing'},
        404: {'description': 'client not found'},
        401: {'description': 'user info does not match'}
    },
    status_code=status.HTTP_200_OK
)
async def simulate():
    try:
        return JSONResponse(status_code=200, content={ 'success': True })
    except Exception as ex:
        raise HTTPException(status_code=500, detail='Internal Server Error')
