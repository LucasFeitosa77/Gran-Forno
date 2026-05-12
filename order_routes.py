from fastapi import APIRouter

order_router = APIRouter(prefix='/orders', tags=['orders'])

@order_router.get('/')
async def orders():
    return {'Mensagem': 'Olá! Bem vindo à lista de pedidos.'}

# TODO: LEMBRE DE DOCUMENTAR SOBRE DECORATORS E A DEFINIÇÃO DE ASSÍNCRONO (ASYNC) E SÍNCRONO (SYNC) E COMO O FASTAPI LIDA COM ISSO TUDO.
# TODO: LEMBRE DE DOCUMENTAR SOBRE O MODELO DE RESPOSTAS DO FASTAPI.