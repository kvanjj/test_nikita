from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(None, min_length=0, max_length=1000)
    due_date: str = Field(None)

class TaskUpdate(BaseModel):
    title: str = Field(None, min_length=1, max_length=255)
    description: str = Field(None, min_length=0, max_length=1000)
    due_date: str = Field(None)

class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    due_date: str
    completed: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str