# pydantic model to validate incoming data
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from city import t1, t2

# pydantic model for user class
class UserInput(BaseModel):
    age : Annotated[int, Field(..., description = "The user age must be a positive value", title = "Age", examples = [23, 60], gt = 0)]
    weight :  Annotated[float, Field(..., description = "The weight of the user in Kg", title = "Weight(kg)", examples = [34, 55], gt = 1)]
    height :  Annotated[float, Field(..., description = "The height of the userd must be in meter", title = "Height(meter)", examples = [1.2, 1.7], gt = 1)]
    income_lpa :  Annotated[float, Field(..., description = "The income must in annual", title = "Annual Income", examples = [1.3, 33], gt = 0)]
    smoker :  Annotated[bool, Field(description = "It must have boolean value", title = "Smoker", default = False)]
    city :  Annotated[str, Field(..., description = "The city is divided into 3 parts", title = "City", examples = ["Jaipur", "Mumbai"])]
    occupation :  Annotated[Literal["Manager", "Engineer", "Doctor", "Teacher", "Businessman",
                                 "Accountant", "Lawyer", "Scientist", "Designer", "Developer"], Field(..., description = "The occupation of the person must be specified", title = "Occupation", examples = ["Manager", "Teacher"])]
    
    @field_validator("city")
    @classmethod
    def City(cls, val):
        return val.strip().title()
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/self.height ** 2, 1)

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.City in t1:
            return 1
        elif self.City in t2:
            return 2
        else:
            return 3

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.age > 80:
            return "high"
        elif self.age > 60 and self.smoker:
            return "high"
        elif self.age > 60 and self.smoker == False:
            return "medium"
        elif self.bmi >= 30 and self.smoker:
            return "high"
        elif self.bmi >= 30 and self.smoker == False:
            return "medium"
        elif self.bmi >= 35:
            return "high"
        elif self.bmi >= 25 and self.smoker:
            return "medium"
        elif self.bmi >= 25 and self.smoker == False:
            return "low"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 20:
            return "teenage"
        elif 46 <= self.age <= 60:
            return "middle_aged"
        elif 20 <= self.age <= 45:
            return "adult"
        else:
            return "senior"