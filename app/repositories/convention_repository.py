# from sqlalchemy.orm import Session
# from app.models.vendor import ConventionRequest

def get_all_conventions():#db: Session):
    return [
        {
            "id": 1,
            "name": "JAFAX",
            "description": "JAFAX is Cool",
            "logo": "../assets/react.svg"
        },
        {
            "id": 2,
            "name": "Kogancon",
            "description": "Kogancon is Cool",
            "logo": "../assets/react.svg"
        }
    ]
