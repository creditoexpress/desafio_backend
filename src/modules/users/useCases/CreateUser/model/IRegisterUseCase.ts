import { Account } from '../../../infra/typeorm/schema/Account';
import { IRequest } from '../RegisterUseCase';

export interface IRegisterUseCase {
  execute({ name, email, cpf, cellPhone }: IRequest): Promise<Account>;
}
