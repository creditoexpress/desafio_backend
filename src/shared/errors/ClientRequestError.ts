import { InternalError } from './InternalError';

export class ClientRequestError extends InternalError {
  constructor(message: string, statusCode?: number) {
    const internalMessage =
      'Unexpected error when trying to communicate to Credito Express';
    super(`${internalMessage}: ${message}`, statusCode);
  }
}
