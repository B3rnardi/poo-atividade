from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import produto_routes, usuario_routes

from app.routes.produto_routes import router as produto_router

app = FastAPI(title='KiOferta API', version='1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(produto_router)
app.include_router(usuario_routes.router)

@app.get('/')
def raiz():
    return {'api': 'KiOferta', 'docs': '/docs'}
