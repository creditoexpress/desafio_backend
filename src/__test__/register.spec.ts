/* eslint-disable import/no-extraneous-dependencies */
import request from 'supertest';
import { getConnection } from 'typeorm';

import { openConnection, disconnect } from '../modules/users/infra/typeorm';
import app from '../shared/infra/http/config/app';

describe('Register User', () => {
  beforeAll(async () => {
    await openConnection();
  });

  afterAll(async () => {
    const connection = getConnection('mongo');
    await connection.dropDatabase();
    await disconnect();
  });

  it('Should be able to register a user with valid cpf and unused email', async () => {
    const response = await request(app).post('/register').send({
      name: 'John Doe',
      email: 'johndoe@mail.com',
      cpf: '81166815080',
      cellPhone: 999999,
    });

    expect(response.status).toBe(201);
  });

  it('Should return 400 when there is a validation error', async () => {
    const response = await request(app).post('/register').send({
      name: 'John Doe',
      email: 'johndoes@mail.com',
      cpf: '8116681508',
      cellPhone: 999999,
    });

    expect(response.status).toBe(400);
    expect(response.body).toEqual({
      statusCode: 400,
      message: 'Invalid CPF',
    });
  });

  it('should return 400 when the email already exists', async () => {
    const response = await request(app).post('/register').send({
      name: 'John Doe',
      email: 'johndoe@mail.com',
      cpf: '81166815080',
      cellPhone: 999999,
    });

    expect(response.status).toBe(400);
    expect(response.body).toEqual({
      statusCode: 400,
      message: 'Email already in use!',
    });
  });
});
