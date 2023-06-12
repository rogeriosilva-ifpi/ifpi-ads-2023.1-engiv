export const schema = `#graphql
    type Expense{
        id: String
        description: String
        amount: Float
        comments: [String]
        owner: User
    }

    type User{
        id: String
        email: String!
        name: String!
    }

    type Query{
        expenses(skip: Int, take: Int): [Expense]
        ping: String
        hello: String
        goodbye: String
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
