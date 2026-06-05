from fastapi import FastAPI,Depends
from sqlalchemy import create_engine,Column,INTEGER,VARCHAR
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base,Session,sessionmaker
from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app=FastAPI()
MYSQL_user="root"
MYSQL_pass="---"
MYSQL_port="3306"
MYSQL_host="localhost"
MYSQL_database="dairy"
database_url=f"mysql+pymysql://{MYSQL_user}:{MYSQL_pass}@{MYSQL_host}:{MYSQL_port}/{MYSQL_database}"

engine=create_engine(database_url)
sessionlocal=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

class Createuser(Base):
    __tablename__="user_details"
    username=Column(VARCHAR(50),primary_key=True,unique=True)
    password=Column(VARCHAR(550))
class Signup(BaseModel):
    username:str
    password:str
class Rem(BaseModel):
    username:str
@app.post("/signup")
def sign(details:Signup,db:Session=Depends(get_db)):
    hashed_pw = hash_password(details.password)
    new = Createuser(
        username=details.username,
        password=hashed_pw
    )
    db.add(new)
    db.commit()
    return "{Message:user created Successfully}"
Base.metadata.create_all(bind=engine)
@app.post("/login")
def login(details:Signup,db:Session=Depends(get_db)):
    user=db.query(Createuser).filter(Createuser.username==details.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    if not verify_password(details.password, user.password):
        raise HTTPException(status_code=401, detail="invalid password")
    token=jwt.encode({"sub":user.username},"mysecretkey",algorithm="HS256")
    return token
@app.get("/retrive")
def retrive(db:Session=Depends(get_db)):
    return db.query(Createuser).all()
@app.delete("/remove")
def remove_user(details:Rem,db:Session=Depends(get_db)):
    user = db.query(Createuser).filter(Createuser.username == details.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    db.delete(user)
    db.commit()
    return "{Message:User deleted successfully}"
