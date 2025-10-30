from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[red]You stand still, unsure what to do. The forest swallows you.[/red]"

def left_path(event):
    return "[yellow]You walk left. " + event + "[/yellow]"

def right_path(event):
    return "[green]You walk right. " + event + "[/green]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Welcome panel with styled text
    console.print(Panel.fit(
        "[bold cyan]🌲 Dark Forest Adventure 🌲[/bold cyan]",
        border_style="green",
        padding=(1, 2)
    ))
    
    console.print("[bold blue]You wake up in a dark forest. You can go left or right.[/bold blue]")
    
    while True:
        # Use rich Prompt for styled input
        choice = Prompt.ask(
            "[bold yellow]Which direction do you choose?[/bold yellow]",
            choices=["left", "right", "exit"],
            default="left"
        )
        choice = choice.strip().lower()
        
        if choice == 'exit':
            # Enhanced goodbye message with rich formatting
            console.print(Panel.fit(
                "[bold magenta]🌟 Thank you for playing Dark Forest Adventure! 🌟\n\n"
                "Your journey through the enchanted forest was brave and memorable.\n"
                "May your paths always lead to new adventures! 🏹✨[/bold magenta]",
                border_style="magenta",
                padding=(1, 2)
            ))
            console.print("\n[italic cyan]We hope to see you again soon in your next adventure![/italic cyan]")
            break
        
        # Get the result and display in a panel
        result = step(choice, events)
        console.print(Panel(
            result,
            title="[bold]Adventure Update[/bold]",
            border_style="blue" if choice == "left" else "green"
        ))