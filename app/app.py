import reflex as rx
from app.states.state import State
from app.components.sidebar import sidebar
from app.pages.cadastro import cadastro_page
from app.pages.clientes import clientes_page
from app.pages.financeiro import financeiro_page
from app.pages.servicos import servicos_page
from app.pages.agendamento import agendamento_page
from app.styles import BASE_STYLES, MAIN_CONTENT_STYLES


def index() -> rx.Component:
    return rx.el.main(
        sidebar(),
        rx.el.div(
            rx.match(
                State.active_page,
                ("Cadastro", cadastro_page()),
                ("Clientes", clientes_page()),
                ("Financeiro", financeiro_page()),
                ("Serviços", servicos_page()),
                ("Agendamento", agendamento_page()),
                cadastro_page(),
            ),
            style=MAIN_CONTENT_STYLES,
        ),
        style=BASE_STYLES,
        class_name="flex",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")