from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    button1 = Button("Saludar")
    button2 = Button.error("Salir")

    def compose(self) -> ComposeResult:
        
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                self.button1,
                self.button2
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if Button.label == "Salir":
            self.exit(str(event.button))
        else:
            self.notify(
                "Desde el IES Haría"
                "[b]El 1º del Ciclo Superior[/b] saluda al mundo!",
                title="Saludo",
                severity="warning",
            )


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())