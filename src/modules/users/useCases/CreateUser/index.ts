import { Transformer } from '../../../../shared/providers/ClassTransformerProvider/ClassTransformerProvider';
import { CpfValidatorProvider } from '../../../../shared/providers/CpfValidator/CpfValidatorProvider';
import { BCryptHashProvider } from '../../../../shared/providers/HashProvider/BCryptHashProvider';
import { RegisterController } from '../../infra/http/controllers/RegisterController';
import { RegisterAccountRepository } from '../../infra/typeorm/repositories/implementations/RegisterAccountRepository';
import { RegisterUseCase } from './RegisterUseCase';

export const makeRegisterController = (): RegisterController => {
  const registerAccountRepository = RegisterAccountRepository.getInstance();
  const cpfValidatorProvider = new CpfValidatorProvider();
  const hashProvider = new BCryptHashProvider();
  const registerUseCase = new RegisterUseCase(
    registerAccountRepository,
    cpfValidatorProvider,
    hashProvider,
  );

  const transformer = new Transformer();

  return new RegisterController(registerUseCase, transformer);
};
