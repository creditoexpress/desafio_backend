export interface ICpfValidatorProvider {
  isValid(cpf: string): boolean;
}
