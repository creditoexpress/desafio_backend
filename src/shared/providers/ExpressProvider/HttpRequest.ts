/* eslint-disable @typescript-eslint/no-empty-interface */
import express, { Request, Response, NextFunction, Router } from 'express';

import { IHttpRequest } from './protocol/IHttpRequest';

export interface IRequest extends Request {
  user: {
    cpf: string;
    email: string;
    score: number;
  };
}

export interface IResponse extends Response {}

export interface INextFunction extends NextFunction {}

export interface IRouter extends Router {}

export const Route = (): IRouter => {
  const router = express.Router();

  return router;
};

export class HttpRequest implements IHttpRequest {
  async create(
    request: IRequest,
    response: IResponse,
  ): Promise<IRequest | IResponse> {
    return request && response;
  }
}
