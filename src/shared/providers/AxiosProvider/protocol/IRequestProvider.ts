/* eslint-disable @typescript-eslint/no-explicit-any */
import { IRequestConfig, IResponse } from '../RequestProvider';

export interface IRequestProvider {
  post<T>(
    url: string,
    data?: any,
    config?: IRequestConfig,
  ): Promise<IResponse<T>>;
}
