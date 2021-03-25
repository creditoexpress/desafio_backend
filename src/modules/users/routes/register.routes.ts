import { celebrate, Segments, Joi } from 'celebrate';

import {
  IRequest,
  IResponse,
  Route,
} from '../../../shared/providers/ExpressProvider/HttpRequest';
import { makeRegisterController } from '../useCases/CreateUser';

const registerRouter = Route();

registerRouter.post(
  '/',
  celebrate({
    [Segments.BODY]: {
      name: Joi.string().required(),
      email: Joi.string().email().required(),
      cpf: Joi.string().required(),
      cellPhone: Joi.number().required(),
    },
  }),
  async (request: IRequest, response: IResponse) => {
    await makeRegisterController().handle(request, response);
  },
);

export { registerRouter };
