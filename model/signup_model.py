from pydantic import BaseModel

class SignupUser(BaseModel):
  id: int
  email: str
  pw: str
  name: str
  age: int
  gender: str
  phone: str
  address: str
  birth: str
  calendar_id: str
  review_id: str