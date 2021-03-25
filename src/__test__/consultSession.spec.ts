/* eslint-disable import/no-extraneous-dependencies */
import request from 'supertest';
import { getConnection } from 'typeorm';

import { openConnection, disconnect } from '../modules/users/infra/typeorm';
import { RegisterAccountRepository } from '../modules/users/infra/typeorm/repositories/implementations/RegisterAccountRepository';
import app from '../shared/infra/http/config/app';
import { BCryptHashProvider } from '../shared/providers/HashProvider/BCryptHashProvider';

describe('Create Session for a User', () => {
  beforeAll(async () => {
    await openConnection();
  });

  afterAll(async () => {
    const connection = getConnection('mongo');
    await connection.dropDatabase();
    await disconnect();
  });

  it('Should be able to return a session for an unregister user', async () => {
    const response = await request(app).post('/session').send({
      email: 'johndoe@mail.com',
      cpf: '81166815080',
      cellPhone: 999999,
    });

    expect(response.body).toHaveProperty('token');
    expect(response.body).toHaveProperty('user');
  });

  it('Should be able to return a session for an register user', async () => {
    const mockRegisterUserRepository = new RegisterAccountRepository();
    const mockHashProvider = new BCryptHashProvider();

    const fakeUser = {
      email: 'johndoe@mail.com',
      cpf: '81166815080',
      cellPhone: 999999,
    };

    const hashCpf = await mockHashProvider.generateHash(fakeUser.cpf);

    await mockRegisterUserRepository.create({
      email: 'johndoe@mail.com',
      cellPhone: 999999,
      cpf: hashCpf,
      name: 'John Doe',
      score: 550,
      negative: false,
    });

    const response = await request(app).post('/session').send(fakeUser);

    expect(response.body).toEqual(
      expect.objectContaining({ token: expect.any(String) }),
    );
  });
});
