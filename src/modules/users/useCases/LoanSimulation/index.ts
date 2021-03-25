import { RequestProvider } from '../../../../shared/providers/AxiosProvider/RequestProvider';
import { LoanSimulationController } from '../../infra/http/controllers/LoanSimulationController';
import { InterestRateRepository } from '../../infra/typeorm/repositories/implementations/InterestRateRepository';
import { RegisterAccountRepository } from '../../infra/typeorm/repositories/implementations/RegisterAccountRepository';
import { LoanSimulationUseCase } from './LoanSimulationUseCase';

const makeLoanSimulationController = (): LoanSimulationController => {
  const registerAccountRepository = RegisterAccountRepository.getInstance();
  const interestRateRepository = new InterestRateRepository();
  const requestProvider = new RequestProvider();

  const loanSimulationUseCase = new LoanSimulationUseCase(
    registerAccountRepository,
    interestRateRepository,
    requestProvider,
  );

  return new LoanSimulationController(loanSimulationUseCase);
};

export { makeLoanSimulationController };
