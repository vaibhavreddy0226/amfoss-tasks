import requests
import html
import threading
import random
from rich.console import Console
from rich.table import Table

console = Console()
QUESTION_URL = "https://opentdb.com/api.php"

class QuizEngine:
    def __init__(self, profile, num_questions, difficulty, time_limit, category_id):
        self.profile = profile
        self.num_questions = num_questions
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.category_id = category_id
        self.questions = []

    def fetch_questions(self):
        params = {
            "amount": self.num_questions,
            "difficulty": self.difficulty,
            "category": self.category_id,
            "type": "multiple"
        }
        try:
            response = requests.get(QUESTION_URL, params=params, timeout=5)
            response.raise_for_status()
            self.questions = response.json().get("results", [])
        except requests.RequestException as e:
            console.print(f"[red]Error fetching questions: {e}[/red]")
            self.questions = []

    def ask_question(self, question_data):
        question = html.unescape(question_data["question"])
        correct = html.unescape(question_data["correct_answer"])
        options = [html.unescape(ans) for ans in question_data.get("incorrect_answers", [])]
        options.append(correct)
        random.shuffle(options)

        console.print(f"\n[bold blue]Q: {question}[/bold blue]")
        for i, option in enumerate(options, 1):
            console.print(f"{i}. {option}")

        answer = {"value": None}
        def timeout():
            if answer["value"] is None:
                console.print("[red]Time’s up![/red]")
                answer["value"] = "timeout"

        timer = threading.Timer(self.time_limit, timeout)
        timer.start()
        try:
            choice = input(f"Enter your answer (1-{len(options)}): ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                answer["value"] = options[int(choice) - 1]
        finally:
            timer.cancel()

        if answer["value"] == correct:
            console.print("[green]Correct![/green]")
            return True
        elif answer["value"] == "timeout":
            return False
        else:
            console.print(f"[red]Wrong! Correct was: {correct}[/red]")
            return False

    def run(self):
        self.fetch_questions()
        if not self.questions:
            console.print("[red]No questions available. Try again later.[/red]")
            return

        for q in self.questions:
            if self.ask_question(q):
                self.profile.update_score()

        table = Table(title="Quiz Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Username", self.profile.username)
        table.add_row("Final Score", str(self.profile.score))
        table.add_row("High Score", str(self.profile.high_score))
        table.add_row("Difficulty", self.difficulty)
        console.print("\n[bold yellow]Quiz Finished![/bold yellow]")
        console.print(table)