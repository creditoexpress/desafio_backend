import { hash, compare } from 'bcrypt';

import { IHashProvider } from './protocol/IHashProvider';

export class BCryptHashProvider implements IHashProvider {
  generateHash(payload: string): Promise<string> {
    return hash(payload, 10);
  }
  compareHash(payload: string, hashed: string): Promise<boolean> {
    return compare(payload, hashed);
  }
}
