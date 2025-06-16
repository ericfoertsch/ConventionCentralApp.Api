from pydantic import BaseModel

class ConventionSeries(BaseModel):
    id_convention_series: int

    class Config:
        from_attributes = True