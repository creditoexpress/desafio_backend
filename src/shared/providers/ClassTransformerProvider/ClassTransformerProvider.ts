/* eslint-disable @typescript-eslint/no-empty-interface */
import { ClassTransformOptions, ClassTransformer } from 'class-transformer';

import { ITransformerProvider } from './model/ITransformerProvider';

export interface IClassTransformOption extends ClassTransformOptions {}

export class Transformer implements ITransformerProvider {
  private transformer = new ClassTransformer();

  internalTransform<T>(object: T, options?: IClassTransformOption): T {
    const restOfTheObject = this.transformer.classToClass(object);

    return restOfTheObject;
  }
}
