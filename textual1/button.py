from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.binding import Binding
from textual.widgets import Button, Static, Footer


class ButtonsApp(App[str]):
    BINDINGS = [
        Binding(key="q", action="quit", description="Salir")
    ]
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        
        yield Footer(),
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                Button("Saludar", id="butSaludar"),
                Button.error("Salir", id="butSalir")
            ),
        )
        

    def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "butSalir":
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