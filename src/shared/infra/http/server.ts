import { openConnection } from '../../../modules/users/infra/typeorm';

openConnection()
  .then(async () => {
    const app = (await import('../http/config/app')).default;

    app.listen(process.env.SERVER_PORT, () => {
      console.info(`🚀 Executando na porta ${process.env.SERVER_PORT}`);
    });
  })
  .catch(console.error);
