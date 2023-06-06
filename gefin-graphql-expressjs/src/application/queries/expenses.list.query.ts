import { Expense } from "../../domain/expense.entity"

type ExpenseDTO = Expense

interface ListExpensesRequestModel {
    skip: number
    take: number
}

interface ListExpenseResponseModel {
    expenses: Expense[]
}

class ListExpensesQueryService {

    constructor() {

    }

    public async execute(request: ListExpensesRequestModel): Promise<ListExpenseResponseModel> {
        return { expenses: [] }
    }

}