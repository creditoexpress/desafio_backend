/* eslint-disable @typescript-eslint/ban-types */
export interface ISignOptions {
  subject?: string;
  expiresIn?: string | number;
}

export interface ITokenManagerProvider {
  sign(
    payload: string | object,
    secret: string,
    options?: ISignOptions,
  ): string;

  verify(token: string, secret: string): string | object;
}
