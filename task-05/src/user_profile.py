from utils import get_profile, update_profile

class UserProfile:
    def __init__(self, username):
        self.username = username
        profile = get_profile(username)
        self.score = 0  # Start fresh each session
        self.high_score = profile.get("high_score", 0) if profile else 0
        self.difficulty = profile.get("difficulty", "easy") if profile else "easy"

    def update_score(self, points=10):
        self.score += points
        self.high_score = max(self.score, self.high_score)
        self.difficulty = "hard" if self.score > 50 else "medium" if self.score > 20 else "easy"
        self.save()

    def save(self):
        update_profile({
            "username": self.username,
            "score": self.score,
            "high_score": self.high_score,
            "difficulty": self.difficulty
        })