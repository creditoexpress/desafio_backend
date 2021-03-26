import { AppError } from '../../../../shared/errors/AppError';
import { ClientRequestError } from '../../../../shared/errors/ClientRequestError';
import { InternalError } from '../../../../shared/errors/InternalError';
import { IRequestProvider } from '../../../../shared/providers/AxiosProvider/protocol/IRequestProvider';
import { IInterestRateRepository } from '../../infra/typeorm/repositories/protocol/IInterestRateRepository';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { IRequest } from '../CreateUser/RegisterUseCase';
import { ILoanSimulationUseCase } from './model/ILoanSimulationUseCase';

enum TypeScore {
  SCORE_BAIXO = 'SCORE_BAIXO',
  SCORE_ALTO = 'SCORE_ALTO',
}

export interface ILoanSimulationSource
  extends Omit<IRequest, 'name' | 'cellPhone' | 'cpf'> {
  score: number;
  installments: number;
  value: number;
}

export interface IResponseSource {
  readonly numeroParcelas: number;
  readonly outrasTaxas: number;
  readonly total: number;
  readonly valorJuros: number;
  readonly valorParcela: number;
  readonly valorSolicitado: number;
}

interface IExpressCreditSource {
  installments: number;
  value: number;
  findInterestRate: number;
}

export class LoanSimulationUseCase implements ILoanSimulationUseCase {
  constructor(
    private registerAccountRepository: IRegisterAccountRepository,

    private interestRateRepository: IInterestRateRepository,

    private requestProvider: IRequestProvider,
  ) {}

  public async execute({
    email,
    score,
    installments,
    value,
  }: ILoanSimulationSource): Promise<IResponseSource> {
    const user = await this.registerAccountRepository.findByEmail(email);

    if (score < 0) {
      throw new AppError('Low Score. Try again later!');
    }

    if (!user) {
      const type = TypeScore.SCORE_BAIXO;
      const findInterestRate = await this.returnFeeToLowScore(
        type,
        installments,
      );

      if (!findInterestRate) {
        throw new InternalError('Internal Error', 500);
      }

      const responseApi = await this.callApiCreditExpress({
        installments,
        value,
        findInterestRate,
      });

      return responseApi;
    }

    if (user.score <= 500) {
      const type = TypeScore.SCORE_BAIXO;
      const findInterestRate = await this.returnFeeToLowScore(
        type,
        installments,
      );

      if (!findInterestRate) {
        throw new InternalError('Internal Error', 500);
      }

      const responseApi = await this.callApiCreditExpress({
        installments,
        value,
        findInterestRate,
      });

      return responseApi;
    }

    const type = TypeScore.SCORE_ALTO;

    const findInterestRate = await this.interestRateRepository.findRateHightScore(
      { type, installments },
    );

    if (!findInterestRate) {
      throw new InternalError('Internal Error', 500);
    }

    const response = await this.callApiCreditExpress({
      installments,
      value,
      findInterestRate: findInterestRate.rate,
    });

    return response;
  }

  private async returnFeeToLowScore(
    type: string,
    installments: number,
  ): Promise<number | undefined> {
    const findInterestRate = await this.interestRateRepository.findRateLowScore(
      { type, installments },
    );

    return findInterestRate?.rate;
  }

  private async callApiCreditExpress({
    installments,
    value,
    findInterestRate,
  }: IExpressCreditSource): Promise<IResponseSource> {
    try {
      const response = await this.requestProvider.post<IResponseSource>(
        'https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend',
        {
          numeroParcelas: installments,
          valor: value,
          taxaJuros: findInterestRate,
        },
      );
      const responseApi = response.data;

      return responseApi;
    } catch (err) {
      if (err.response && err.response.status) {
        await this.returnErrorInvalidInstallments(err, installments);

        await this.returnErrorInvalidParameters(err, {
          installments,
          value,
          findInterestRate,
        });
      }

      throw new ClientRequestError(err.message);
    }
  }

  private async returnErrorInvalidInstallments(
    err: any,
    installments: number,
  ): Promise<void> {
    const installmentsMap = new Map([
      [6, 6],
      [12, 12],
      [18, 18],
      [24, 24],
      [36, 36],
    ]);
    if (!installmentsMap.has(installments)) {
      throw new AppError(`${err.response.data}`, err.response.status);
    }
  }

  private async returnErrorInvalidParameters(
    err: any,
    { installments, value, findInterestRate }: IExpressCreditSource,
  ): Promise<void> {
    if (!installments || !value || !findInterestRate) {
      throw new AppError(`${err.response.data}`, err.response.status);
    }
  }
}
