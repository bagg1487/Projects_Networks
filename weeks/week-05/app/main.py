from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional

@strawberry.type
class Ticket:
    id: int
    name: str
    status: str

tickets_db = []
counter = 1

@strawberry.type
class Query:
    @strawberry.field
    def tickets(self) -> List[Ticket]:
        return tickets_db
    
    @strawberry.field
    def ticket(self, id: int) -> Optional[Ticket]:
        for ticket in tickets_db:
            if ticket.id == id:
                return ticket
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createTicket(self, name: str, status: str) -> Ticket:
        global counter
        new_ticket = Ticket(id=counter, name=name, status=status)
        tickets_db.append(new_ticket)
        counter += 1
        return new_ticket

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")