from fastapi import HTTPException, status, Body, Request
from fastapi.responses import JSONResponse

from ....core.exceptions import FeeNotFound
from ....core.models import Simulation
from ....core.values import SimulationRequest
from ....core.services import get_fee
from ...middlewares.auth import app
from ...external_apis.simulations_api import get_simulation


@app.post(
    '/',
    tags=['simulation'],
    responses={
        422: {'description': 'cpf or portions fields are missing'},
        404: {'description': 'fee for such portions not found'},
    },
    status_code=status.HTTP_200_OK
)
async def simulate(request: Request, simulation: Simulation = Body(...)):
    try:
        cpf = request['client_cpf']
        fees_repository = request.app.ctx.ioc.get('fees_repository')
        clients_repository = request.app.ctx.ioc.get('clients_repository')

        fee = await get_fee(
                cpf=cpf,
                portions=simulation.portions,
                fees_repository=fees_repository, 
                clients_repository=clients_repository
            )

        simulation_request = SimulationRequest(
                                fee=fee,
                                value=simulation.value,
                                portions=simulation.portions
                            )
        simulation = await get_simulation(simulation_request)

        if not simulation:
            return JSONResponse(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                    content='Third Party Not Responding'
                )

        return JSONResponse(status_code=status.HTTP_200_OK, content=simulation)
    except FeeNotFound as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='fee amount not found')
    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='Internal Server Error'
        )
