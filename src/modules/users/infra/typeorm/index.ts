import { createConnections, Connection } from 'typeorm';

const closeConnection = new Connection({ type: 'mongodb' });

export const openConnection = async (): Promise<Connection[]> =>
  createConnections();

export const disconnect = (): Promise<void> => closeConnection.close();
