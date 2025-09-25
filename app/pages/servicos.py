import reflex as rx
from app.states.servicos_state import ServicosState
from app.styles import PAGE_CARD_STYLE, PAGE_HEADER_STYLE, PAGE_SUBHEADER_STYLE


def servico_card(servico: dict) -> rx.Component:
    return rx.el.div(
        rx.el.h3(servico["nome"], class_name="font-semibold text-lg text-gray-800"),
        rx.el.p(f"R$ {servico['valor'].to_string()}", class_name="text-gray-600 my-2"),
        rx.el.button(
            "Selecionar",
            on_click=lambda: ServicosState.add_servico_transacao(servico),
            class_name="mt-4 w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition-colors",
        ),
        class_name="bg-white p-6 rounded-lg shadow-md border border-gray-200 hover:shadow-lg transition-shadow cursor-pointer",
    )


def servicos_page() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Gestão de Serviços", style=PAGE_HEADER_STYLE),
        rx.el.p(
            "Cadastre e gerencie os serviços oferecidos pelo petshop.",
            style=PAGE_SUBHEADER_STYLE,
        ),
        rx.el.div(
            rx.foreach(ServicosState.servicos, servico_card),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
        ),
        style=PAGE_CARD_STYLE,
    )