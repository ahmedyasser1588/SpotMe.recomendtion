from fastapi import FastAPI
from app.api.player import router as player_router
from app.api.club import router as club_router
from app.api.recommendation import router as recommendation_router

app = FastAPI(
    title="AI Service",
    description="Sports Recommendation & CV Generation API",
    version="1.0.0",
    debug=True
)
app.include_router(player_router)
app.include_router(club_router)
app.include_router(recommendation_router)


players = [
    {
        "id": 1,
        "name": "Ahmed",
        "overall": 91,
        "physical": 88,
        "attacking": 90
    },
    {
        "id": 2,
        "name": "Ali",
        "overall": 85,
        "physical": 82,
        "attacking": 87
    }
]


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI Service is working successfully 🚀"
    }


@app.get("/players")
def get_players():
    return players