import { AppError } from '../../../../shared/errors/AppError';
import { ICreateInstallmentsDTO } from '../../dtos/ICreateInstallmentsDTO';
import { InterestRateDTO } from '../../dtos/InterestRateDTO';
import { IInterestRateRepository } from '../../infra/typeorm/repositories/protocol/IInterestRateRepository';
import { Rate } from '../../infra/typeorm/schema/Rate';
import { RatesRegistrationUseCase } from './RatesRegistrationUseCase';

interface ISutTypes {
  sut: RatesRegistrationUseCase;
  interestRateRepositoryStub: IInterestRateRepository;
}

const makeInterestRateRepository = (): IInterestRateRepository => {
  class InterestRateRepositoryStub implements IInterestRateRepository {
    create(data: ICreateInstallmentsDTO): Promise<Rate> {
      return new Promise(resolve => resolve({} as Rate));
    }
    findRateLowScore({ type, installments }: InterestRateDTO): Promise<Rate> {
      return new Promise(resolve => resolve({} as Rate));
    }
    findRateHightScore({ type, installments }: InterestRateDTO): Promise<Rate> {
      return new Promise(resolve => resolve({} as Rate));
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
  const interestRateRepositoryStub = makeInterestRateRepository();

  const sut = new RatesRegistrationUseCase(interestRateRepositoryStub);

  return {
    sut,
    interestRateRepositoryStub,
  };
};

describe('Installments Registration', () => {
  it('Should be able to create rates', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeRates = {
      type: 'SCORE_BAIXO',
      installments: 6,
      rate: 0.04,
    };

    jest.spyOn(interestRateRepositoryStub, 'create').mockReturnValueOnce(
      new Promise(resolve =>
        resolve({
          type: 'SCORE_BAIXO',
          installments: 6,
          rate: 0.04,
        } as Rate),
      ),
    );

    const response = await sut.execute(fakeRates);

    expect(response).toEqual(fakeRates);
  });

  it('Should not be able to create rates with different type than SCORE_BAIXO or SCORE_ALTO', async () => {
    const { sut } = makeSut();

    const fakeRates = {
      id: 'valid_id',
      type: 'fake_type',
      installments: 6,
      rate: 0.04,
    };

    const response = sut.execute(fakeRates);

    await expect(response).rejects.toBeInstanceOf(AppError);
  });

  it('Should not be able to create rates with invalid installments', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeRates = {
      id: 'valid_id',
      type: 'SCORE_BAIXO',
      installments: 10,
      rate: 0.04,
    };

    jest.spyOn(interestRateRepositoryStub, 'create').mockReturnValueOnce(
      new Promise(resolve =>
        resolve({
          type: 'SCORE_BAIXO',
          installments: 10,
          rate: 0.04,
        } as Rate),
      ),
    );

    const response = sut.execute(fakeRates);

    await expect(response).rejects.toBeInstanceOf(AppError);
  });

  it('Should not be able to create an register that already exists', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeRates = {
      id: 'valid_id',
      type: 'SCORE_BAIXO',
      installments: 6,
      rate: 0.04,
    };

    jest.spyOn(interestRateRepositoryStub, 'findRate').mockReturnValueOnce(
      new Promise(resolve =>
        resolve({
          id: 'valid_id',
          type: 'SCORE_BAIXO',
          installments: 6,
          rate: 0.04,
        } as Rate),
      ),
    );

    const response = sut.execute(fakeRates);

    await expect(response).rejects.toBeInstanceOf(AppError);
  });

  it('Should throw if findRate method returns undefined', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeRates = {
      id: 'valid_id',
      type: 'SCORE_BAIXO',
      installments: 6,
      rate: 0.04,
    };

    jest
      .spyOn(interestRateRepositoryStub, 'findRate')
      .mockReturnValueOnce(new Promise(resolve => resolve(undefined)));

    const response = sut.execute(fakeRates);

    await expect(response).rejects.toBeInstanceOf(AppError);
  });

  it('Should throw if duplicate installments and type', async () => {
    const { sut, interestRateRepositoryStub } = makeSut();

    const fakeRates = {
      id: 'valid_id',
      type: 'SCORE_BAIXO',
      installments: 6,
      rate: 0.04,
    };

    jest.spyOn(interestRateRepositoryStub, 'findRate').mockReturnValueOnce(
      new Promise(resolve =>
        resolve({
          id: 'valid_id',
          type: 'SCORE_BAIXO',
          installments: 6,
          rate: 0.06,
        }),
      ),
    );

    const response = sut.execute(fakeRates);

    await expect(response).rejects.toBeInstanceOf(AppError);
  });
});
