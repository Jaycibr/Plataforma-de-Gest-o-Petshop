import reflex as rx
from typing import TypedDict, Literal


class MenuItem(TypedDict):
    name: str
    icon: str
    page: str


class State(rx.State):
    active_page: str = "Cadastro"
    menu_items: list[MenuItem] = [
        {"name": "Cadastro", "icon": "layout-dashboard", "page": "Cadastro"},
        {"name": "Clientes", "icon": "users", "page": "Clientes"},
        {"name": "Financeiro", "icon": "dollar-sign", "page": "Financeiro"},
        {"name": "Serviços", "icon": "wrench", "page": "Serviços"},
        {"name": "Agendamento", "icon": "calendar", "page": "Agendamento"},
    ]

    def set_active_page(self, page: str):
        self.active_page = page