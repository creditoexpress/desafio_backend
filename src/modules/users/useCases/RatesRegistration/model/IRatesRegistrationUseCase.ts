import { ICreateInstallmentsDTO } from '../../../dtos/ICreateInstallmentsDTO';
import { Rate } from '../../../infra/typeorm/schema/Rate';

export interface IRatesRegistrationUseCase {
  execute({ type, installments, rate }: ICreateInstallmentsDTO): Promise<Rate>;
}
