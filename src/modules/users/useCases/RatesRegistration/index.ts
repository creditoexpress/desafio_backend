import { RatesRegistrationController } from '../../infra/http/controllers/RatesRegistrationController';
import { InterestRateRepository } from '../../infra/typeorm/repositories/implementations/InterestRateRepository';
import { RatesRegistrationUseCase } from './RatesRegistrationUseCase';

const makeRatesRegistrationController = (): RatesRegistrationController => {
  const interasteRateRepository = new InterestRateRepository();
  const ratesRegistrationUseCase = new RatesRegistrationUseCase(
    interasteRateRepository,
  );

  return new RatesRegistrationController(ratesRegistrationUseCase);
};

export { makeRatesRegistrationController };
