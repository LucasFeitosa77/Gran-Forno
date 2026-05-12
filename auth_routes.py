from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def auth():
    return {'Mensagem': 'Olá! Bem vindo à área de autenticação', 'Autenticado': False}