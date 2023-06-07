import expensesService from "../../application/expenses.service"

export const resolvers = {
    Query: {
        expenses: async (parent, args, ctx, info) => {
            return await expensesService.list(args.skip, args.take)
        }
    },
    Expense: {
        description: (parent) => parent.description.toUpperCase()
    }
}