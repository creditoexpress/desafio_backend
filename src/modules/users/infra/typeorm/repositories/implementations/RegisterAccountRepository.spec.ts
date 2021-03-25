import { getConnection } from 'typeorm';

import { disconnect, openConnection } from '../../index';
import { RegisterAccountRepository } from './RegisterAccountRepository';

describe('Register Account on Mongo', () => {
  beforeAll(async () => {
    await openConnection();
  });

  afterAll(async () => {
    const connection = getConnection('mongo');
    await connection.dropDatabase();
    await disconnect();
  });

  it('Should return an account on success', async () => {
    const sut = new RegisterAccountRepository();

    const account = {
      name: 'John Doe',
      email: 'john@mail.com',
      cpf: '123456',
      cellPhone: 999999,
      score: 550,
      negative: false,
    };

    const accountStub = await sut.create(account);

    expect(accountStub).toBeTruthy();
    expect(accountStub.id).toBeTruthy();
    expect(accountStub.name).toBe('John Doe');
    expect(accountStub.email).toBe('john@mail.com');
  });
});
