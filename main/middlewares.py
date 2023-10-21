from fastapi.middleware.cors import CORSMiddleware

def add_middlwares(app):
    app.add_middleware(CORSMiddleware,)