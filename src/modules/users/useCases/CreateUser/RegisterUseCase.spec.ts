/* eslint-disable no-param-reassign */
/* eslint-disable max-classes-per-file */
import { cpf } from 'cpf-cnpj-validator';

import { AppError } from '../../../../shared/errors/AppError';
import { ICpfValidatorProvider } from '../../../../shared/providers/CpfValidator/protocol/ICpfValidatorProvider';
import { IHashProvider } from '../../../../shared/providers/HashProvider/protocol/IHashProvider';
import { IRegisterAccountDTO } from '../../dtos/IRegisterAccountDTO';
import { IRegisterAccountRepository } from '../../infra/typeorm/repositories/protocol/IRegisterAccountRepository';
import { Account } from '../../infra/typeorm/schema/Account';
import { RegisterUseCase } from './RegisterUseCase';

interface ISutTypes {
  sut: RegisterUseCase;
  registerAccountRepositoryStub: IRegisterAccountRepository;
  cpfValidatorStub: ICpfValidatorProvider;
  bcrypHashProviderStub: IHashProvider;
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

const makeRegisterAccountRepository = (): IRegisterAccountRepository => {
  class RegisterAccountStub {
    async findByCpf(cpf: string): Promise<Account> {
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

    async create(account: IRegisterAccountDTO): Promise<Account> {
      const fakeRegister = {
        id: 'valid_id',
        name: 'valid_name',
        email: 'any_email@mail.com',
        cpf: '123456',
        cellPhone: 999999,
        score: 550,
        negative: false,
      };

      return fakeRegister;
    }

    async findByEmail(email: string): Promise<Account | undefined> {
      return new Promise(resolve => resolve(undefined));
    }
  }
  return new RegisterAccountStub();
};

const makeSut = (): ISutTypes => {
  const cpfValidatorStub = makeCpfValidator();
  const bcrypHashProviderStub = makeHash();

  const registerAccountRepositoryStub = makeRegisterAccountRepository();
  const sut = new RegisterUseCase(
    registerAccountRepositoryStub,
    cpfValidatorStub,
    bcrypHashProviderStub,
  );

  return {
    sut,
    registerAccountRepositoryStub,
    cpfValidatorStub,
    bcrypHashProviderStub,
  };
};

describe('Create User', () => {
  it('Should be able to register with valid values', async () => {
    const { sut, cpfValidatorStub, registerAccountRepositoryStub } = makeSut();

    const fakeRegister = {
      name: 'valid_name',
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 999999,
    };

    const isValidCpfSpy = jest.spyOn(cpfValidatorStub, 'isValid');
    const repositorySpy = jest.spyOn(registerAccountRepositoryStub, 'create');

    await sut.execute(fakeRegister);

    expect(isValidCpfSpy).toHaveBeenCalledWith('123456');
    expect(repositorySpy).toHaveBeenCalledWith({
      name: 'valid_name',
      email: 'any_email@mail.com',
      cpf: 'hashed_value',
      cellPhone: 999999,
      negative: false,
      score: 550,
    });
  });

  it('Should not be able to register with invalid cpf', async () => {
    const { sut, cpfValidatorStub } = makeSut();

    const fakeRegister = {
      name: 'valid_name',
      email: 'any_email@mail.com',
      cpf: '123456',
      cellPhone: 999999,
      score: 500,
      negative: false,
    };

    const cpfValidator = cpf.isValid(fakeRegister.cpf);

    jest.spyOn(cpfValidatorStub, 'isValid').mockReturnValueOnce(false);

    const register = sut.execute(fakeRegister);

    expect(cpfValidator).toBe(false);
    await expect(register).rejects.toBeInstanceOf(AppError);
  });

  it('Should not be able to register with a email that already exists', async () => {
    const { sut, registerAccountRepositoryStub } = makeSut();

    const fakeAccount = {
      id: 'valid_id',
      name: 'valid_name',
      email: 'any_email@mail.com',
      cpf: '1234567',
      cellPhone: 999999,
      score: 500,
      negative: false,
    };

    jest
      .spyOn(registerAccountRepositoryStub, 'findByEmail')
      .mockReturnValueOnce(new Promise(resolve => resolve(fakeAccount)));

    const duplicateRegister = sut.execute(fakeAccount);

    await expect(duplicateRegister).rejects.toBeInstanceOf(AppError);
  });
});
