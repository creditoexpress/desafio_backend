import { IClassTransformOption } from '../ClassTransformerProvider';

export interface ITransformerProvider {
  internalTransform<T>(object: T, options?: IClassTransformOption): T;
}
