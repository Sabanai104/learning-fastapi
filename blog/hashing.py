from passlib.context import CryptContext

class Hash():
    def bcrypt(password: str):
        pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

        return pwd_ctx.hash(password)
