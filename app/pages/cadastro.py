import reflex as rx
from app.states.cliente_state import ClienteState
from app.styles import PAGE_CARD_STYLE, PAGE_HEADER_STYLE, PAGE_SUBHEADER_STYLE


def form_field(
    label: str, name: str, placeholder: str, type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700"),
        rx.el.input(
            name=name,
            placeholder=placeholder,
            type=type,
            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
        ),
        class_name="w-full",
    )


def cadastro_page() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Cadastro de Clientes e Pets", style=PAGE_HEADER_STYLE),
        rx.el.p(
            "Preencha os campos abaixo para cadastrar um novo cliente e seu pet.",
            style=PAGE_SUBHEADER_STYLE,
        ),
        rx.el.form(
            rx.el.div(
                form_field("Nome Completo", "nome_completo", "Ex: João da Silva"),
                form_field("E-mail", "email", "Ex: joao.silva@email.com", type="email"),
                form_field("Data de Nascimento", "data_nascimento", "", type="date"),
                form_field("CPF", "cpf", "Ex: 123.456.789-00"),
                form_field("Telefone", "telefone", "Ex: (11) 98765-4321", type="tel"),
                form_field("Endereço", "endereco", "Ex: Rua das Flores, 123"),
                form_field("Nome do Pet", "nome_pet", "Ex: Rex"),
                form_field("Idade do Pet", "idade_pet", "Ex: 5", type="number"),
                form_field("Raça do Pet", "raca_pet", "Ex: Labrador"),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            rx.el.button(
                "Cadastrar Cliente",
                type="submit",
                class_name="mt-8 w-full inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
            ),
            on_submit=ClienteState.add_cliente,
            reset_on_submit=True,
            class_name="mt-8",
        ),
        style=PAGE_CARD_STYLE,
    )