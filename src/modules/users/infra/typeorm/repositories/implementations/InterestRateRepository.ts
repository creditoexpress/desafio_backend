import { MongoRepository, getMongoRepository } from 'typeorm';

import { ICreateInstallmentsDTO } from '../../../../dtos/ICreateInstallmentsDTO';
import { InterestRateDTO } from '../../../../dtos/InterestRateDTO';
import { Rate } from '../../schema/Rate';
import { IInterestRateRepository } from '../protocol/IInterestRateRepository';

export class InterestRateRepository implements IInterestRateRepository {
  private ormRepository: MongoRepository<Rate>;

  constructor() {
    this.ormRepository = getMongoRepository(Rate, 'mongo');
  }

  async findRateLowScore({
    type,
    installments,
  }: InterestRateDTO): Promise<Rate | undefined> {
    const findRates = await this.ormRepository.findOne({
      where: { type, installments },
    });

    return findRates;
  }

  async findRateHightScore({
    type,
    installments,
  }: InterestRateDTO): Promise<Rate | undefined> {
    const findRates = await this.ormRepository.findOne({
      where: { type, installments },
    });

    return findRates;
  }

  async findRate({
    type,
    installments,
    rate,
  }: InterestRateDTO): Promise<Rate | undefined> {
    const findRate = await this.ormRepository.findOne({
      where: { type, installments, rate },
    });

    return findRate;
  }

  async create({
    type,
    installments,
    rate,
  }: ICreateInstallmentsDTO): Promise<Rate> {
    const rates = this.ormRepository.create({
      type,
      installments,
      rate,
    });

    await this.ormRepository.save(rates);

    return rates;
  }
}
