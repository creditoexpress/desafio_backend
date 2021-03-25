import { IResponse } from '../../../../../shared/providers/AxiosProvider/RequestProvider';
import {
  ILoanSimulationSource,
  IResponseSource,
} from '../LoanSimulationUseCase';

export interface ILoanSimulationUseCase {
  execute({
    email,
    installments,
    value,
    score,
  }: ILoanSimulationSource): Promise<IResponseSource>;
}
