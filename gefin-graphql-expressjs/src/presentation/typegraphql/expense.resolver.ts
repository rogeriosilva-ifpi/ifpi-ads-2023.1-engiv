import { Query, Resolver } from "type-graphql";
import expensesService from "../../application/expenses.service";
import { Expense } from "../../domain/expense.entity";

@Resolver(of => Expense)
export class ExpenseResolver {


  @Query(returns => [Expense])
  async expenses(): Promise<Expense[]> {
    return expensesService.list()
  }

}