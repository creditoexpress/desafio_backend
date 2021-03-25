import { IRegisterAccountDTO } from '../../../../dtos/IRegisterAccountDTO';
import { Account } from '../../schema/Account';

export interface IRegisterAccountRepository {
  create(account: IRegisterAccountDTO): Promise<Account>;
  findByEmail(email: string): Promise<Account | undefined>;
}
