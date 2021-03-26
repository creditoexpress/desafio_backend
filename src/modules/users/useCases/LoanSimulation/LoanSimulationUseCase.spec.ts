/* eslint-disable max-classes-per-file */

import { AppError } from '../../../../shared/errors/AppError';
import { ClientRequestError } from '../../../../shared/errors/ClientRequestError';
import { IRequestProvider } from '../../../../shared/providers/AxiosProvider/protocol/IRequestProvider';
import {
  IRequestConfig,
  IResponse,
} from '../../../../shared/providers/AxiosProvider/RequestProvider';
import { ICreateInstallmentsDTO } from '../../dtos/ICreateInstallmentsDTO';
import { InterestRateDTO } from '../../dtos/InterestRateDTO';
import { IRegisterAccountDTO } from '../../dtos/IRegisterAccountDTO';
import { IInterestRateRepository } from '../../infra/typeorm/repositories/protocol/IInterestRateRepository';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { Account } from '../../infra/typeorm/schema/Account';
import { Rate } from '../../infra/typeorm/schema/Rate';
import { LoanSimulationUseCase } from './LoanSimulationUseCase';

interface ISutTypes {
  sut: LoanSimulationUseCase;
  registerAccountRepositoryStub: IRegisterAccountRepository;
  interestRateRepositoryStub: IInterestRateRepository;
  requestProviderStub: IRequestProvider;
}

const makeRequestProvider = (): IRequestProvider => {
  class RequestProviderStub implements IRequestProvider {
    post<IResponseSource>(
      url: string,
      data?: any,
      config?: IRequestConfig,
    ): Promise<IResponse<IResponseSource>> {
      const mockedReturnValueAxios = {
        numeroParcelas: 12,
        outrasTaxas: 85,
        total: 1125.0,
        valorJuros: 40.0,
        valorParcela: 93.75,
        valorSolicitado: 1000,
      };
      return new Promise(resolve =>
        resolve({ data: mockedReturnValueAxios } as IResponse),
      );
    }
  }

  return new RequestProviderStub();
};

const makeRegisterAccountRepository = (): IRegisterAccountRepository => {
  class RegisterAccountStub implements IRegisterAccountRepository {
    findByCpf(cpf: string): Promise<Account> {
      const fakeAccount = {
        id: 'valid_id',
        name: 'John Doe',
        email: 'any_email@mail.com',
        cpf: 'hashed_cpf',
        cellPhone: 555555,
        score: 0,
        negative: false,
        installments: 6,
        value: 1000,
      };

      return new Promise(resolve => resolve(fakeAccount));
    }
    create(account: IRegisterAccountDTO): Promise<Account> {
      return new Promise(resolve => resolve({ ...account, id: 'valid_id' }));
    }
    findByEmail(email: string): Promise<Account | undefined> {
      return new Promise(resolve => resolve(undefined));
    }
  }

  return new RegisterAccountStub();
};

const makeInterestRateRepository = (): IInterestRateRepository => {
  class InterestRateRepositoryStub implements IInterestRateRepository {
    create(data: ICreateInstallmentsDTO): Promise<Rate> {
      return new Promise(resolve => resolve({} as Rate));
    }
    findRateLowScore({ type, installments }: InterestRateDTO): Promise<Rate> {
      return new Promise(resolve =>
        resolve({
          type: 'valid_type',
          installments: 6,
          rate: 0.04,
        } as Rate),
      );
    }
    findRateHightScore({ type, installments }: InterestRateDTO): Promise<Rate> {
      return new Promise(resolve =>
        resolve({
          type: 'valid_type',
          installments: 6,
          rate: 0.03,
        } as Rate),
      );
    }

    findRate({
      type,
      installments,
      rate,
    }: InterestRateDTO): Promise<Rate | undefined> {
      return new Promise(resolve => resolve({} as Rate));
    }
  }

  return new InterestRateRepositoryStub();
};

const makeSut = (): ISutTypes => {
  const registerAccountRepositoryStub = makeRegisterAccountRepository();
  const interestRateRepositoryStub = makeInterestRateRepository();
  const requestProviderStub = makeRequestProvider();

  const sut = new LoanSimulationUseCase(
    registerAccountRepositoryStub,
    interestRateRepositoryStub,
    requestProviderStub,
  );

  return {
    sut,
    registerAccountRepositoryStub,
    interestRateRepositoryStub,
    requestProviderStub,
  };
};

describe('Loan Simulation', () => {
  const mockedReturnValueAxios = {
    numeroParcelas: 12,
    outrasTaxas: 85,
    total: 1125.0,
    valorJuros: 40.0,
    valorParcela: 93.75,
    valorSolicitado: 1000,
  };

  it('Should throw if user is negative', async () => {
    const { sut } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: '123456',
      score: -1,
      installments: 6,
      value: 1000,
    };

    const loanSimulation = sut.execute(fakeAccount);

    await expect(loanSimulation).rejects.toBeInstanceOf(AppError);
  });

  it('Should returns fees from api for an unregistered user', async () => {
    const { sut } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 0,
      negative: false,
      installments: 6,
      rate: 0.04,
      value: 1000,
    };

    const loanSimulation = await sut.execute(fakeAccount);

    expect(loanSimulation).toEqual(mockedReturnValueAxios);
  });

  it('Should returns fees from external api for an registered user with low score', async () => {
    const { sut, registerAccountRepositoryStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 500,
      negative: false,
      installments: 6,
      value: 1000,
    };

    jest
      .spyOn(registerAccountRepositoryStub, 'findByEmail')
      .mockReturnValueOnce(
        new Promise(resolve =>
          resolve({
            ...fakeAccount,
            id: 'valid_id',
            name: 'any_name',
            cellPhone: 9999,
          }),
        ),
      );

    const loanSimulation = await sut.execute(fakeAccount);

    expect(loanSimulation).toEqual(mockedReturnValueAxios);
  });

  it('Should returns fees from external api for an registered user with hight score', async () => {
    const { sut, registerAccountRepositoryStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 550,
      negative: false,
      installments: 6,
      value: 1000,
    };

    jest
      .spyOn(registerAccountRepositoryStub, 'findByEmail')
      .mockReturnValueOnce(
        new Promise(resolve =>
          resolve({
            ...fakeAccount,
            id: 'valid_id',
            name: 'any_name',
            cellPhone: 9999,
          }),
        ),
      );

    const loanSimulation = await sut.execute(fakeAccount);

    expect(loanSimulation).toEqual(mockedReturnValueAxios);
  });

  it('Should return a generic error from LoanSimulationUseCase service when the request fail before reaching the service', async () => {
    const { sut, requestProviderStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 550,
      negative: false,
      installments: 6,
      value: 1000,
    };

    jest
      .spyOn(requestProviderStub, 'post')
      .mockRejectedValue({ message: 'Network Error' });

    const loanSimulation = sut.execute(fakeAccount);

    await expect(loanSimulation).rejects.toThrow(
      'Unexpected error when trying to communicate to Credito Express: Network Error',
    );
  });

  it('Should return a message error from LoanSimulationUseCase service when the invalid installments number', async () => {
    const { sut, requestProviderStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 550,
      negative: false,
      installments: 16,
      value: 1000,
    };

    jest.spyOn(requestProviderStub, 'post').mockRejectedValue({
      response: {
        data: 'Número de parecelas é inválida',
        status: 400,
      },
    });

    const loanSimulation = sut.execute(fakeAccount);

    await expect(loanSimulation).rejects.toBeInstanceOf(AppError);
  });

  it('Should return a message error from LoanSimulationUseCase service if any parameters are not informed', async () => {
    const { sut, requestProviderStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 550,
      negative: false,
      installments: 12,
      value: 0,
    };

    jest.spyOn(requestProviderStub, 'post').mockRejectedValue({
      response: {
        data: 'Todos os parâmetros devem ser informados',
        status: 400,
      },
    });

    const loanSimulation = sut.execute(fakeAccount);

    await expect(loanSimulation).rejects.toBeInstanceOf(AppError);
  });

  it('Should return a message error from LoanSimulationUseCase service if findInterestRate parameter are not returned', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeAccount = {
      email: 'any_email@mail.com',
      cpf: 'hashed_cpf',
      score: 550,
      negative: false,
      installments: 12,
      value: 0,
    };

    jest
      .spyOn(interestRateRepositoryStub, 'findRateHightScore')
      .mockReturnValueOnce(new Promise(resolve => resolve(undefined)));

    jest
      .spyOn(interestRateRepositoryStub, 'findRateLowScore')
      .mockReturnValueOnce(new Promise(resolve => resolve(undefined)));

    const loanSimulation = sut.execute(fakeAccount);

    await expect(loanSimulation).rejects.toThrow('Internal Error');
  });
});
