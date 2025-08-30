import emoji
import typer

app = typer.Typer()


@app.command()
def command_b():
    print(f"{emoji.emojize(':check_mark_button:')} package_b command")


if __name__ == "__main__":
    app()
