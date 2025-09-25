import reflex as rx
from app.states.cliente_state import ClienteState
from app.styles import PAGE_CARD_STYLE, PAGE_HEADER_STYLE, PAGE_SUBHEADER_STYLE


def editable_cell(text: rx.Var, index: int, field: str) -> rx.Component:
    return rx.cond(
        ClienteState.editing_index == index,
        rx.el.input(
            default_value=text,
            on_change=lambda value: ClienteState.handle_edit_change(field, value),
            class_name="bg-transparent border border-blue-500 rounded px-2 py-1 w-full text-sm",
            on_blur=ClienteState.save_edit,
        ),
        rx.el.p(text, class_name="text-sm text-gray-700"),
    )


def table_header(text: str) -> rx.Component:
    return rx.el.th(
        text,
        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
    )


def action_buttons(index: int) -> rx.Component:
    return rx.cond(
        ClienteState.editing_index == index,
        rx.el.div(
            rx.el.button(
                rx.icon(tag="check", class_name="h-4 w-4"),
                on_click=ClienteState.save_edit,
                class_name="text-green-600 hover:text-green-900",
            ),
            rx.el.button(
                rx.icon(tag="x", class_name="h-4 w-4"),
                on_click=ClienteState.cancel_edit,
                class_name="text-red-600 hover:text-red-900 ml-2",
            ),
            class_name="flex items-center",
        ),
        rx.el.button(
            rx.icon(tag="pencil", class_name="h-4 w-4"),
            on_click=lambda: ClienteState.start_editing(index),
            class_name="text-blue-600 hover:text-blue-900",
        ),
    )


def client_row(client: dict, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.p(
                client["nome_completo"], class_name="text-sm font-medium text-gray-900"
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            editable_cell(client["email"], index, "email"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            editable_cell(client["telefone"], index, "telefone"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            editable_cell(client["endereco"], index, "endereco"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.p(client["cpf"], class_name="text-sm text-gray-700"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.p(client["nome_pet"], class_name="text-sm text-gray-700"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.p(client["idade_pet"], class_name="text-sm text-gray-700"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.p(client["raca_pet"], class_name="text-sm text-gray-700"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            action_buttons(index),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name=rx.cond(index % 2 == 0, "bg-white", "bg-gray-50"),
    )


def clientes_page() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Gestão de Clientes", style=PAGE_HEADER_STYLE),
        rx.el.p(
            "Adicione, visualize e edite informações dos seus clientes.",
            style=PAGE_SUBHEADER_STYLE,
        ),
        rx.el.div(
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            table_header("Nome Completo"),
                            table_header("E-mail"),
                            table_header("Telefone"),
                            table_header("Endereço"),
                            table_header("CPF"),
                            table_header("Nome do Pet"),
                            table_header("Idade do Pet"),
                            table_header("Raça do Pet"),
                            rx.el.th(scope="col", class_name="relative px-6 py-3"),
                        ),
                        class_name="bg-gray-50",
                    ),
                    rx.el.tbody(
                        rx.foreach(ClienteState.clientes, client_row),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200",
                ),
                class_name="overflow-x-auto",
            ),
            class_name="shadow border-b border-gray-200 sm:rounded-lg mt-8",
        ),
        rx.el.div(
            rx.el.button(
                "Editar Dados",
                class_name="mt-4 inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
            ),
            class_name="flex justify-end w-full",
        ),
        style=PAGE_CARD_STYLE,
    )