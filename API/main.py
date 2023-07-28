from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import BaseModel
from . import db

app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "tweetle-secret-token-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str

class User(BaseModel):
    username: str
    password: str

@app.post("/signup")
async def signup(user: User):
    if db.get_user(username = user):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    db.new_user(
        username = user.username,
        password = user.password
    )
    
    return {"message": "User registered successfully"}

@app.post("/token")
async def login(user: dict):
    if type(user) != dict:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not db.get_user(username = user["username"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    if not db.encrypt(user["password"]) == db.get_user(username = user["username"])["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected_route")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not db.get_user(username = username):
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": f"Hello {username}!"}
