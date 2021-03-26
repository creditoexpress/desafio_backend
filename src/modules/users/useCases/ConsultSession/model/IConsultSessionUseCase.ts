import { IUserSessionSource, IResponse } from '../ConsultSessionUseCase';

export interface IConsultSessionUseCase {
  execute({
    email,
    cpf,
    cellPhone,
  }: Omit<IUserSessionSource, 'score'>): Promise<IResponse>;
}
