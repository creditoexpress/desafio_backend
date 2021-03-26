import { cpf as cpfValidator } from 'cpf-cnpj-validator';

import { ICpfValidatorProvider } from './protocol/ICpfValidatorProvider';

export class CpfValidatorProvider implements ICpfValidatorProvider {
  isValid(cpf: string): boolean {
    const isValid = cpfValidator.isValid(cpf);

    return isValid;
  }
}
