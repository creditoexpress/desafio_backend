import { celebrate, Segments, Joi } from 'celebrate';

import {
  IRequest,
  IResponse,
  Route,
} from '../../../shared/providers/ExpressProvider/HttpRequest';
import { makeRatesRegistrationController } from '../useCases/RatesRegistration';

const ratesRegistrationRouter = Route();

ratesRegistrationRouter.post(
  '/',
  celebrate({
    [Segments.BODY]: {
      type: Joi.string().required(),
      installments: Joi.number().required(),
      rate: Joi.number().required(),
    },
  }),
  async (request: IRequest, response: IResponse) => {
    await makeRatesRegistrationController().handle(request, response);
  },
);

export { ratesRegistrationRouter };
