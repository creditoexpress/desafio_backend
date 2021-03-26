import { AppError } from '../../../../shared/errors/AppError';
import { ICpfValidatorProvider } from '../../../../shared/providers/CpfValidator/protocol/ICpfValidatorProvider';
import { IHashProvider } from '../../../../shared/providers/HashProvider/protocol/IHashProvider';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { Account } from '../../infra/typeorm/schema/Account';
import { IRegisterUseCase } from './model/IRegisterUseCase';

export interface IRequest {
  name: string;
  email: string;
  cpf: string;
  cellPhone: number;
}

export class RegisterUseCase implements IRegisterUseCase {
  constructor(
    private registerAccountRepository: IRegisterAccountRepository,

    private cpfValidatorProvider: ICpfValidatorProvider,

    private hashProvider: IHashProvider,
  ) {}

  async execute({ name, email, cpf, cellPhone }: IRequest): Promise<Account> {
    const cpfValidator = this.cpfValidatorProvider.isValid(cpf);

    if (!cpfValidator) {
      throw new AppError('Invalid CPF');
    }

    const user = await this.registerAccountRepository.findByEmail(email);

    if (user) {
      throw new AppError('Email already in use!');
    }

    const hashedCpf = await this.hashProvider.generateHash(cpf);

    const createAccount = await this.registerAccountRepository.create({
      name,
      email,
      cpf: hashedCpf,
      cellPhone,
      score: 550,
      negative: false,
    });

    return createAccount;
  }
}
