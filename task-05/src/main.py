from user_profile import UserProfile
from quiz_engine import QuizEngine
from utils import get_categories
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    console.print("[bold blue]Welcome to TimeTickQuiz Pro! 📚[/bold blue]\n")

    username = input("Enter your username: ")
    profile = UserProfile(username)

    while True:
        try:
            num_questions = int(input("How many questions (1–20)? "))
            if 1 <= num_questions <= 20:
                break
            console.print("[red]Please enter a number between 1 and 20.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Enter a number.[/red]")

    while True:
        try:
            time_limit = int(input("Time limit per question (10–30 seconds)? "))
            if 10 <= time_limit <= 30:
                break
            console.print("[red]Please enter a number between 10 and 30.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Enter a number.[/red]")

    categories = get_categories()
    table = Table(title="Available Categories")
    table.add_column("ID", style="cyan")
    table.add_column("Category", style="magenta")
    for i, cat in enumerate(categories, 1):
        table.add_row(str(i), cat["name"])
    console.print(table)
    while True:
        try:
            cat_choice = int(input(f"Select category (1–{len(categories)}): "))
            if 1 <= cat_choice <= len(categories):
                category_id = categories[cat_choice-1]["id"]
                break
            console.print(f"[red]Please enter a number between 1 and {len(categories)}.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Enter a number.[/red]")

    while True:
        difficulty = input("Difficulty (easy/medium/hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        console.print("[red]Please enter easy, medium, or hard.[/red]")

    quiz = QuizEngine(profile, num_questions, difficulty, time_limit, category_id)
    quiz.run()

if __name__ == "__main__":
    main()