export class InternalError extends Error {
  constructor(public message: string, public statusCode = 500) {
    super(message);
  }
}
