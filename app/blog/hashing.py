from passlib.context import CryptContext

pass_ctx = CryptContext(schemes =["bcrypt"],deprecated ="auto")

class Hash():
    def bcrypt(password: str):
     return pass_ctx.hash(password)

    def verify(hashed_password,plain_password):
     return pass_ctx.verify(plain_password,hashed_password)