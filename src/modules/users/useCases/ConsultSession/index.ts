import { Transformer } from '../../../../shared/providers/ClassTransformerProvider/ClassTransformerProvider';
import { CpfValidatorProvider } from '../../../../shared/providers/CpfValidator/CpfValidatorProvider';
import { BCryptHashProvider } from '../../../../shared/providers/HashProvider/BCryptHashProvider';
import { TokenManagerProvider } from '../../../../shared/providers/TokenManager/TokenManagerProvider';
import { ConsultSessionController } from '../../infra/http/controllers/ConsultSessionController';
import { RegisterAccountRepository } from '../../infra/typeorm/repositories/implementations/RegisterAccountRepository';
import { ConsultSessionUseCase } from './ConsultSessionUseCase';

export const makeConsultSessionController = (): ConsultSessionController => {
  const registerAccountRepository = RegisterAccountRepository.getInstance();
  const cpfValidatorProvider = new CpfValidatorProvider();
  const bcriptHashProvider = new BCryptHashProvider();
  const tokenManagerProvider = new TokenManagerProvider();

  const consultSessionUseCase = new ConsultSessionUseCase(
    registerAccountRepository,
    cpfValidatorProvider,
    bcriptHashProvider,
    tokenManagerProvider,
  );

  const transformer = new Transformer();

  return new ConsultSessionController(consultSessionUseCase, transformer);
};
