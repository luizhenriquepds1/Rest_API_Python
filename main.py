from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# para rodar o código, executar no terminal: uvicorn main:app --reload

'''
Endpoint:
/ordens (path)

Requisições de Rest APIs:
GET -> leitura/pegar
POST -> enviar/criar
PUT/PATCH -> edição
DELETE -> deletar
'''