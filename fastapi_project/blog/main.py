from fastapi import FastAPI
from blog.database import engine
from blog.routers import blog, user, authentication
from blog import models

app = FastAPI()

# this line will finally create a table in my db
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
