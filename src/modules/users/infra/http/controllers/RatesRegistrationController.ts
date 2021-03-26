import {
  IRequest,
  IResponse,
} from '../../../../../shared/providers/ExpressProvider/HttpRequest';
import { RatesRegistrationUseCase } from '../../../useCases/RatesRegistration/RatesRegistrationUseCase';

export class RatesRegistrationController {
  constructor(private ratesRegistrationUseCase: RatesRegistrationUseCase) {}

  async handle(request: IRequest, response: IResponse): Promise<IResponse> {
    const { type, installments, rate } = request.body;

    const rates = await this.ratesRegistrationUseCase.execute({
      type,
      installments,
      rate,
    });

    return response.status(201).json(rates);
  }
}
