from pydantic import BaseModel


class Cookie(BaseModel):
    color: str = "Yellow"


class CustomCookie:
    def __init__(self, color: str):
        self.color = color


a = Cookie()
print(a.model_dump_json())
a.color = "Black"
print(a.model_dump_json())

b = CustomCookie("Orange")
print(b.color)
b.color = "Red"
print(b.color)
