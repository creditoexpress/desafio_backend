import { ITransformerProvider } from '../../../../../shared/providers/ClassTransformerProvider/model/ITransformerProvider';
import {
  IRequest,
  IResponse,
} from '../../../../../shared/providers/ExpressProvider/HttpRequest';
import { IRegisterUseCase } from '../../../useCases/CreateUser/model/IRegisterUseCase';
import { Account } from '../../typeorm/schema/Account';

export class RegisterController {
  constructor(
    private registerUseCase: IRegisterUseCase,

    private transformerProvider: ITransformerProvider,
  ) {}

  async handle(request: IRequest, response: IResponse): Promise<IResponse> {
    const { name, email, cpf, cellPhone } = request.body;

    const register = await this.registerUseCase.execute({
      name,
      email,
      cpf,
      cellPhone,
    });

    return response.status(201).json({
      register: this.transformerProvider.internalTransform<Account>(register),
    });
  }
}
