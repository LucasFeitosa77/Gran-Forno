from fastapi import APIRouter

order_router = APIRouter(prefix='/orders', tags=['orders'])

@order_router.get('/')
async def orders():
    return {'Mensagem': 'Olá! Bem vindo à lista de pedidos.'}
