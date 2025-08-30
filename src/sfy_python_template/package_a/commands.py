import emoji
import typer

app = typer.Typer()


@app.command()
def command_a():
    print(f"{emoji.emojize(':check_mark_button:')} package_a command")


if __name__ == "__main__":
    app()
