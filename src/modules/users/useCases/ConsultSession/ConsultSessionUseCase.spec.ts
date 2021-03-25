/* eslint-disable @typescript-eslint/ban-types */
/* eslint-disable no-param-reassign */
/* eslint-disable max-classes-per-file */
import { AppError } from '../../../../shared/errors/AppError';
import { ICpfValidatorProvider } from '../../../../shared/providers/CpfValidator/protocol/ICpfValidatorProvider';
import { IHashProvider } from '../../../../shared/providers/HashProvider/protocol/IHashProvider';
import {
  ISignOptions,
  ITokenManagerProvider,
} from '../../../../shared/providers/TokenManager/protocol/ITokenManagerProvider';
import { IRegisterAccountDTO } from '../../dtos/IRegisterAccountDTO';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { Account } from '../../infra/typeorm/schema/Account';
import { ConsultSessionUseCase } from './ConsultSessionUseCase';

interface ISutTypes {
  sut: ConsultSessionUseCase;
  cpfValidatorStub: ICpfValidatorProvider;
  registerAccountRepositoryStub: IRegisterAccountRepository;
  hashProviderStub: IHashProvider;
  tokenManager: ITokenManagerProvider;
}

const makeCpfValidator = (): ICpfValidatorProvider => {
  class CpfValidatorStub implements ICpfValidatorProvider {
    isValid(cpf: string): boolean {
      return true;
    }
  }

  return new CpfValidatorStub();
};

const makeHash = (): IHashProvider => {
  class BCrypHashProviderStub implements IHashProvider {
    generateHash(payload: string): Promise<string> {
      payload = 'hashed_value';

      return new Promise(resolve => resolve(payload));
    }
    compareHash(payload: string, hashed: string): Promise<boolean> {
      return new Promise(resolve => resolve(true));
    }
  }

  return new BCrypHashProviderStub();
};

const makeTokenManager = (): ITokenManagerProvider => {
  class TokenManagerStub implements ITokenManagerProvider {
    sign(
      payload: string | object,
      secret: string,
      options?: ISignOptions,
    ): string {
      return 'generateToken';
    }
    verify(token: string, secret: string): string | object {
      return token;
    }
  }

  return new TokenManagerStub();
};

const makeRegisterAccountRepository = (): IRegisterAccountRepository => {
  class RegisterAccountStub implements IRegisterAccountRepository {
    create(account: IRegisterAccountDTO): Promise<Account> {
      return new Promise(resolve => resolve({ ...account, id: 'valid_id' }));
    }
    findByEmail(email: string): Promise<Account | undefined> {
      return new Promise(resolve => resolve(undefined));
    }

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
  }

  return new RegisterAccountStub();
};

const makeSut = (): ISutTypes => {
  const cpfValidatorStub = makeCpfValidator();
  const registerAccountRepositoryStub = makeRegisterAccountRepository();
  const hashProviderStub = makeHash();
  const tokenManager = makeTokenManager();

  const sut = new ConsultSessionUseCase(
    registerAccountRepositoryStub,
    cpfValidatorStub,
    hashProviderStub,
    tokenManager,
  );

  return {
    sut,
    cpfValidatorStub,
    registerAccountRepositoryStub,
    hashProviderStub,
    tokenManager,
  };
};

describe('CunsultUseCase', () => {
  it('Should throw if is invalid cpf', async () => {
    const { sut, cpfValidatorStub } = makeSut();

    const fakeSession = {
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 99999,
      score: 0,
      negative: false,
    };

    jest.spyOn(cpfValidatorStub, 'isValid').mockReturnValueOnce(false);

    const session = sut.execute(fakeSession);

    await expect(session).rejects.toBeInstanceOf(AppError);
  });

  it('Should throw if is invalid compare hash cpf', async () => {
    const { sut, hashProviderStub } = makeSut();

    const fakeSession = {
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 99999,
      score: 0,
      negative: false,
    };

    jest
      .spyOn(hashProviderStub, 'compareHash')
      .mockReturnValueOnce(new Promise(resolve => resolve(false)));

    const session = sut.execute(fakeSession);

    await expect(session).rejects.toBeInstanceOf(AppError);
  });

  it('Should be able to create a session for an unregistered user', async () => {
    const { sut } = makeSut();

    const unregistered = {
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 99999,
      score: 0,
      negative: false,
    };

    const unregisteredUserSession = await sut.execute(unregistered);

    expect(unregisteredUserSession).toEqual({
      token: 'generateToken',
      user: {
        email: 'any_email@mail.com',
        cpf: 'hashed_value',
        cellPhone: 99999,
        score: 0,
        negative: false,
      },
    });
  });

  it('Should be able to create a session for an registered user', async () => {
    const { sut, registerAccountRepositoryStub } = makeSut();

    const registered = {
      id: 'valid_id',
      name: 'valid_name',
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 999999,
      score: 500,
      negative: false,
    };

    jest
      .spyOn(registerAccountRepositoryStub, 'findByEmail')
      .mockReturnValueOnce(new Promise(resolve => resolve(registered)));

    const registeredUserSession = await sut.execute(registered);

    expect(registeredUserSession).toEqual({
      token: 'generateToken',
      user: {
        id: 'valid_id',
        name: 'valid_name',
        email: 'any_email@mail.com',
        cpf: '123456',
        cellPhone: 999999,
        score: 500,
        negative: false,
      },
    });
  });
});
