import authConfig from '../../../../config/auth';
import { AppError } from '../../../../shared/errors/AppError';
import { ICpfValidatorProvider } from '../../../../shared/providers/CpfValidator/protocol/ICpfValidatorProvider';
import { IHashProvider } from '../../../../shared/providers/HashProvider/protocol/IHashProvider';
import { ITokenManagerProvider } from '../../../../shared/providers/TokenManager/protocol/ITokenManagerProvider';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { IConsultSessionUseCase } from './model/IConsultSessionUseCase';

export interface IUserSessionSource {
  email: string;
  cpf: string;
  cellPhone: number;
  score: number;
}

interface ITokenGeneration extends Omit<IUserSessionSource, 'cellPhone'> {
  userCpf: string;
  negative: boolean;
}

export interface IResponse {
  user: IUserSessionSource;
  token: string;
}

export class ConsultSessionUseCase implements IConsultSessionUseCase {
  constructor(
    private registerAccountRepository: IRegisterAccountRepository,

    private cpfValidatorProvider: ICpfValidatorProvider,

    private hashProvider: IHashProvider,

    private tokenManagerProvider: ITokenManagerProvider,
  ) {}

  async execute({
    email,
    cpf,
    cellPhone,
  }: IUserSessionSource): Promise<IResponse> {
    const isValidCpf = this.cpfValidatorProvider.isValid(cpf);

    if (!isValidCpf) {
      throw new AppError('Invalid CPF');
    }

    const user = await this.registerAccountRepository.findByEmail(email);

    if (!user) {
      const hashedCpf = await this.hashProvider.generateHash(cpf);

      const tempAccount = {
        email,
        cpf: hashedCpf,
        cellPhone,
        score: 0,
        negative: false,
      };

      const token = await this.generateToken({
        cpf,
        email: tempAccount.email,
        userCpf: tempAccount.cpf,
        score: tempAccount.score,
        negative: tempAccount.negative,
      });

      return { token, user: tempAccount };
    }

    const token = await this.generateToken({
      cpf,
      email: user.email,
      userCpf: user.cpf,
      score: user.score,
      negative: user.negative,
    });

    return { token, user };
  }

  private async generateToken({
    cpf,
    email,
    userCpf,
    score,
    negative,
  }: ITokenGeneration): Promise<string> {
    const compareHashedCpf = await this.hashProvider.compareHash(cpf, userCpf);

    if (!compareHashedCpf) {
      throw new AppError('Invalid CPF. Try again!');
    }

    const { secret, expiresIn } = authConfig.jwt;

    const token = this.tokenManagerProvider.sign(
      { score, negative, email },
      secret,
      {
        subject: userCpf,
        expiresIn,
      },
    );

    return token;
  }
}
