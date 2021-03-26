/* eslint-disable @typescript-eslint/naming-convention */
declare namespace Express {
  export interface Request {
    user: {
      cpf: string;
      email: string;
      score: number;
    };
  }
}
