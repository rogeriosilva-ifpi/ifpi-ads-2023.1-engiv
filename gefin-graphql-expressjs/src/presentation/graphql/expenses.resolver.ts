import expensesService from "../../application/expenses.service"

export const resolvers = {
    Query: {
        ping: () => 'Pong!',
        expenses: async () => {
            return await expensesService.list()
        }
    },
    Mutation: {
        addExpense: async (_, args) => {
            const input = args.input
            return await expensesService.create(input)
        }
    },
    Expense: {
        comments: () => ['Despesa desnecessário viu Loira!']
    }

}