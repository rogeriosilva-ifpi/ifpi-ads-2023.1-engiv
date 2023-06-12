import { Field, Float, ObjectType } from "type-graphql"

@ObjectType()
export class Expense {

    @Field(() => String)
    id: string

    @Field(() => String, { nullable: false })
    description: string

    @Field(() => Float, { nullable: false })
    amount: number

    date?: Date

    category: string

    @Field(() => [String])
    comments: string[]

    // API - Cuidar dos invariants
}