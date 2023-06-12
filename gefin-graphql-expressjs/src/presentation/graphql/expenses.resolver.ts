import expensesService from "../../application/expenses.service"

export const resolvers = {
    Query: {
        expenses: async (_, args, ctx, info) => {
            return await expensesService.list(args.skip, args.take)
        }
    },
    Expense: {
        description: (parent) => parent.description.toUpperCase()
    }
}