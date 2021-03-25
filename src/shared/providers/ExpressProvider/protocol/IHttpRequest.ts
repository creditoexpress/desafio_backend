import { IRequest, IResponse } from '../HttpRequest';

export interface IHttpRequest {
  create(request: IRequest, response: IResponse): Promise<IRequest | IResponse>;
}
