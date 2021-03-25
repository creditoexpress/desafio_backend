import { ITransformerProvider } from '../../../../../shared/providers/ClassTransformerProvider/model/ITransformerProvider';
import {
  IRequest,
  IResponse,
} from '../../../../../shared/providers/ExpressProvider/HttpRequest';
import { IConsultSessionUseCase } from '../../../useCases/ConsultSession/model/IConsultSessionUseCase';

export class ConsultSessionController {
  constructor(
    private consultSessionUseCase: IConsultSessionUseCase,

    private transformerProvider: ITransformerProvider,
  ) {}

  async handle(request: IRequest, response: IResponse): Promise<IResponse> {
    const { cpf, email, cellPhone } = request.body;

    const session = await this.consultSessionUseCase.execute({
      cpf,
      email,
      cellPhone,
    });

    return response
      .status(201)
      .json(this.transformerProvider.internalTransform(session));
  }
}
