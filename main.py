import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora TAP"
    page.window_width = 270
    page.window_height = 480
    page.padding = 20

    # Display
    display_text = ft.Text("0", size=30)

    display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=230,
        height=70
    )

    # Variables de control
    current_value = ""
    operator = ""
    first_value = None

    def actualizar_display(valor):
        display_text.value = valor
        page.update()

    def presionar_numero(e):
        nonlocal current_value
        current_value += e.control.data
        actualizar_display(current_value)

    def presionar_operador(e):
        nonlocal first_value, operator, current_value
        if current_value != "":
            first_value = float(current_value)
            operator = e.control.data
            current_value = ""

    def calcular(e):
        nonlocal first_value, operator, current_value
        if current_value != "" and operator != "":
            second_value = float(current_value)

            if operator == "+":
                result = first_value + second_value
            elif operator == "-":
                result = first_value - second_value
            elif operator == "*":
                result = first_value * second_value
            elif operator == "/":
                result = first_value / second_value if second_value != 0 else 0

            current_value = str(result)
            actualizar_display(current_value)
            operator = ""

    def limpiar(e):
        nonlocal first_value, operator, current_value
        first_value = None
        operator = ""
        current_value = ""
        actualizar_display("0")

    # Grid
    grid = ft.GridView(
        runs_count=4,
        spacing=10,
        run_spacing=10,
        width=230,
        height=300,
        expand=False
    )

    botones = [
        ("7", ft.Colors.BLUE, presionar_numero),
        ("8", ft.Colors.GREY, presionar_numero),
        ("9", ft.Colors.PURPLE, presionar_numero),
        ("/", ft.Colors.RED, presionar_operador),

        ("4", ft.Colors.BLUE, presionar_numero),
        ("5", ft.Colors.GREY, presionar_numero),
        ("6", ft.Colors.PURPLE, presionar_numero),
        ("*", ft.Colors.RED, presionar_operador),

        ("1", ft.Colors.BLUE, presionar_numero),
        ("2", ft.Colors.GREY, presionar_numero),
        ("3", ft.Colors.PURPLE, presionar_numero),
        ("-", ft.Colors.RED, presionar_operador),

        ("0", ft.Colors.BLUE, presionar_numero),
        ("C", ft.Colors.GREY, limpiar),
        ("=", ft.Colors.PURPLE, calcular),
        ("+", ft.Colors.RED, presionar_operador),
    ]

    for texto, color, accion in botones:
        grid.controls.append(
            ft.Container(
                content=ft.Text(texto, size=20, color=ft.Colors.WHITE),
                bgcolor=color,
                border_radius=8,
                alignment=ft.alignment.Alignment(0, 0),
                height=55,
                data=texto,
                on_click=accion
            )
        )

    page.add(
        ft.Column(
            controls=[display, grid],
            tight=True
        )
    )

ft.app(target=main)