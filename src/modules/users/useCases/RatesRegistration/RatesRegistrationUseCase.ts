import { AppError } from '../../../../shared/errors/AppError';
import { ICreateInstallmentsDTO } from '../../dtos/ICreateInstallmentsDTO';
import { IInterestRateRepository } from '../../infra/typeorm/repositories/protocol/IInterestRateRepository';
import { Rate } from '../../infra/typeorm/schema/Rate';
import { IRatesRegistrationUseCase } from './model/IRatesRegistrationUseCase';

enum TypeScore {
  SCORE_BAIXO = 'SCORE_BAIXO',
  SCORE_ALTO = 'SCORE_ALTO',
}

export class RatesRegistrationUseCase implements IRatesRegistrationUseCase {
  constructor(private interasteRateRepository: IInterestRateRepository) {}

  async execute({
    type,
    installments,
    rate,
  }: ICreateInstallmentsDTO): Promise<Rate> {
    const typeMap = new Map([
      ['SCORE_BAIXO', TypeScore.SCORE_BAIXO],
      ['SCORE_ALTO', TypeScore.SCORE_ALTO],
    ]);

    if (!typeMap.has(type)) {
      throw new AppError('Invalid Type Description!');
    }

    const installmentsMap = new Map([
      [6, 6],
      [12, 12],
      [18, 18],
      [24, 24],
      [36, 36],
    ]);

    const findRate = await this.interasteRateRepository.findRate({
      type,
      installments,
      rate,
    });

    if (!findRate) {
      throw new AppError('Not found! Register a new data!', 401);
    }

    const responseInstallments = findRate.installments;
    const responseType = findRate.type;
    const responseRate = findRate.rate;

    if (
      installmentsMap.has(responseInstallments) &&
      typeMap.has(responseType) &&
      responseRate === rate
    ) {
      throw new AppError('Register already exists!');
    }

    if (
      installmentsMap.has(responseInstallments) &&
      typeMap.has(responseType)
    ) {
      throw new AppError('Installments and Type already register!');
    }

    const rates = await this.interasteRateRepository.create({
      type,
      installments,
      rate,
    });

    return rates;
  }
}
