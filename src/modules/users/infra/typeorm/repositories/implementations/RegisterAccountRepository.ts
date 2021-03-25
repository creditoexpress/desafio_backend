import { MongoRepository, getMongoRepository } from 'typeorm';

import { IRegisterAccountDTO } from '../../../../dtos/IRegisterAccountDTO';
import { Account } from '../../schema/Account';
import { IRegisterAccountRepository } from '../protocol/IRegisterAccountRepository';

export class RegisterAccountRepository implements IRegisterAccountRepository {
  private ormRepository: MongoRepository<Account>;

  private static INSTANCE: RegisterAccountRepository;

  constructor() {
    this.ormRepository = getMongoRepository(Account, 'mongo');
  }

  static getInstance(): RegisterAccountRepository {
    if (!RegisterAccountRepository.INSTANCE) {
      RegisterAccountRepository.INSTANCE = new RegisterAccountRepository();
    }

    return RegisterAccountRepository.INSTANCE;
  }

  async findByEmail(email: string): Promise<Account | undefined> {
    const findEmail = await this.ormRepository.findOne({ where: { email } });

    return findEmail;
  }

  async create({
    name,
    email,
    cpf,
    cellPhone,
    score,
    negative,
  }: IRegisterAccountDTO): Promise<Account> {
    const account = this.ormRepository.create({
      name,
      email,
      cpf,
      cellPhone,
      score,
      negative,
    });

    await this.ormRepository.save(account);

    return account;
  }
}
