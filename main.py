from fastapi import FastAPI

app = FastAPI(title='Gran Forno', version='1.0')

# Importar rotas deve ser após a instância do FastAPI
# Isso é importante para evitar erros de importação ciclica

from auth_routes import auth_router
from order_routes import order_router

# Incluindo rotas criadas nos outros arquivos
app.include_router(auth_router)
app.include_router(order_router)
