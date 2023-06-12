import { ApolloServer } from '@apollo/server';
import { expressMiddleware } from '@apollo/server/express4';
import cors from "cors";
import debug from "debug";
import express, { Request, Response } from "express";
import "express-async-errors";
import 'reflect-metadata';
import { buildSchema } from 'type-graphql';
import { CommomRoutesConfig } from "./common/common.routes.config";
import { my_logger } from "./common/log";
import { errorHandler } from "./presentation/rest/error.middleware";
import { ExpensesRoutes } from "./presentation/rest/expenses.routes";
import { ExpenseResolver } from './presentation/typegraphql/expense.resolver';


const debugLog: debug.IDebugger = debug("app");

async function main() {
  // Express App and others stuffs
  const app: express.Application = express();
  const port = 3000;
  const routes: Array<CommomRoutesConfig> = [];

  // Middlewares
  app.use(express.json());
  app.use(cors());

  // Middleware for winston logger
  app.use(my_logger);

  // Registering routes
  routes.push(new ExpensesRoutes(app));

  // REST Hello Route
  const hello_msg = `Server started and running at http://localhost:${port}`;
  app.get("/", (req: Request, res: Response) => {
    res.status(200).json(hello_msg);
  });

  // Global Error Handling
  app.use(errorHandler);


  // SChema first code
  /*const serverGql = new ApolloServer({
    typeDefs: schema,
    resolvers: resolvers
  })


  await serverGql.start()
  */

  const schema = await buildSchema({
    resolvers: [ExpenseResolver]
  })

  const serverGql = new ApolloServer({
    schema,
  })

  await serverGql.start()


  const graphMiddleware = expressMiddleware(serverGql)

  app.use('/graphql', graphMiddleware)

  // Startup App
  app.listen(port, () => {
    routes.forEach((route: CommomRoutesConfig) => {
      debugLog(`Routes add for ${route.name}`);
    });

    console.log(hello_msg);
  });
}

main().catch((error) => {
  debugLog(error);
  process.exit(1);
});
