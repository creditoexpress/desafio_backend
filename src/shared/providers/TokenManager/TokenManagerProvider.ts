/* eslint-disable @typescript-eslint/ban-types */
import { sign, verify } from 'jsonwebtoken';

import {
  ISignOptions,
  ITokenManagerProvider,
} from './protocol/ITokenManagerProvider';

export class TokenManagerProvider implements ITokenManagerProvider {
  sign(
    payload: string | object,
    secret: string,
    options?: ISignOptions,
  ): string {
    return sign(payload, secret, options);
  }

  verify(token: string, secret: string): string | object {
    return verify(token, secret);
  }
}
