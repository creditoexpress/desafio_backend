import { ICreateInstallmentsDTO } from '../../../../dtos/ICreateInstallmentsDTO';
import { InterestRateDTO } from '../../../../dtos/InterestRateDTO';
import { Rate } from '../../schema/Rate';

export interface IInterestRateRepository {
  create({ type, installments, rate }: ICreateInstallmentsDTO): Promise<Rate>;
  findRateLowScore({
    type,
    installments,
  }: InterestRateDTO): Promise<Rate | undefined>;
  findRateHightScore({
    type,
    installments,
  }: InterestRateDTO): Promise<Rate | undefined>;
  findRate({
    type,
    installments,
    rate,
  }: InterestRateDTO): Promise<Rate | undefined>;
}
