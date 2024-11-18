from pydantic import BaseModel

class SigninUser(BaseModel):
  email: str
  pw: str
