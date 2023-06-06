export const schema = `#graphql
    type Expense{
        id: String
        description: String
        amount: Float
        comments: [String]
    }

    type Query{
        expenses: [Expense]
        ping: String
    }

    input ExpenseInput{
        description: String!
        amount: Float!
        category: String!
    }

    type Mutation{
        addExpense(input: ExpenseInput!): Expense
    }
`
