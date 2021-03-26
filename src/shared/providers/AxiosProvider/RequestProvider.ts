/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/no-empty-interface */
import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';

import { IRequestProvider } from './protocol/IRequestProvider';

export interface IRequestConfig extends AxiosRequestConfig {}

export interface IResponse<T = any> extends AxiosResponse<T> {}

export class RequestProvider implements IRequestProvider {
  constructor(private request = axios) {}

  public post<T>(
    url: string,
    data?: any,
    config?: IRequestConfig,
  ): Promise<IResponse<T>> {
    return this.request.post<T, IResponse<T>>(url, data, config);
  }
}
