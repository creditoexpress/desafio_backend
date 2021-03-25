import {
  IRequest,
  IResponse,
} from '../../../../../shared/providers/ExpressProvider/HttpRequest';
import { ILoanSimulationUseCase } from '../../../useCases/LoanSimulation/model/ILoanSimulationUseCase';

export class LoanSimulationController {
  constructor(private loanSimulationUseCase: ILoanSimulationUseCase) {}

  async handle(request: IRequest, response: IResponse): Promise<IResponse> {
    const { email, score } = request.user;
    const { installments, value } = request.body;

    const loanSimulation = await this.loanSimulationUseCase.execute({
      email,
      installments,
      value,
      score,
    });

    return response.status(201).json(loanSimulation);
  }
}
