from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder, Button, DataTable, Input
from textual.containers import Horizontal

ROWS = [
    ("ID", "Nombre"),
    (1, "Yoel"),
    (4, "Samuel"),
    (7, "Amaro"),
]

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Horizontal(
            Button("Nuevo", id="bNuevo"),
            Button("Editar", id="bEditar"),
            Button("Borrar", id="bBorrar")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        id = event.button.id
        
        if id == "bEditar":
            self.app.switch_to_edit()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

class EditScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")
        yield Horizontal(
                Button("Aceptar"),
                Button("Cancelar"),
        )
        yield Button("Principal")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.switch_to_main()


class ModesApp(App):
    BINDINGS = [
        ("m", "switch_mode('main')", "Principal"),  
        ("e", "switch_mode('edit')", "Edición"),
    ]
    MODES = {
        "main": MainScreen,  
        "edit": EditScreen,
    }

    def on_mount(self) -> None:    
        self.switch_mode("main")

    def switch_to_edit(self) -> None:
        self.switch_mode("edit")

    def switch_to_main(self) -> None:
        self.switch_mode("main")


if __name__ == "__main__":
    app = ModesApp()
    app.run()