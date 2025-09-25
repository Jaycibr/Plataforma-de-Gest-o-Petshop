import reflex as rx
from typing import TypedDict, Optional


class Cliente(TypedDict):
    nome_completo: str
    email: str
    data_nascimento: str
    cpf: str
    telefone: str
    endereco: str
    nome_pet: str
    idade_pet: str
    raca_pet: str


class ClienteState(rx.State):
    clientes: list[Cliente] = [
        {
            "nome_completo": "João da Silva",
            "email": "joao.silva@email.com",
            "data_nascimento": "1990-05-15",
            "cpf": "123.456.789-00",
            "telefone": "(11) 98765-4321",
            "endereco": "Rua das Flores, 123",
            "nome_pet": "Rex",
            "idade_pet": "5",
            "raca_pet": "Labrador",
        },
        {
            "nome_completo": "Maria Oliveira",
            "email": "maria.o@email.com",
            "data_nascimento": "1985-11-20",
            "cpf": "098.765.432-11",
            "telefone": "(21) 91234-5678",
            "endereco": "Avenida Principal, 456",
            "nome_pet": "Mimi",
            "idade_pet": "3",
            "raca_pet": "Siamês",
        },
    ]
    editing_index: int = -1
    edited_cliente_data: Cliente = {
        "nome_completo": "",
        "email": "",
        "data_nascimento": "",
        "cpf": "",
        "telefone": "",
        "endereco": "",
        "nome_pet": "",
        "idade_pet": "",
        "raca_pet": "",
    }

    @rx.event
    def add_cliente(self, form_data: dict):
        new_cliente: Cliente = {
            "nome_completo": form_data.get("nome_completo", ""),
            "email": form_data.get("email", ""),
            "data_nascimento": form_data.get("data_nascimento", ""),
            "cpf": form_data.get("cpf", ""),
            "telefone": form_data.get("telefone", ""),
            "endereco": form_data.get("endereco", ""),
            "nome_pet": form_data.get("nome_pet", ""),
            "idade_pet": form_data.get("idade_pet", ""),
            "raca_pet": form_data.get("raca_pet", ""),
        }
        self.clientes.append(new_cliente)
        yield rx.toast.success("Cliente cadastrado com sucesso!")

    @rx.event
    def start_editing(self, index: int):
        self.editing_index = index
        self.edited_cliente_data = self.clientes[index].copy()

    @rx.event
    def handle_edit_change(self, field: str, value: str):
        self.edited_cliente_data[field] = value

    @rx.event
    def save_edit(self):
        if self.editing_index != -1:
            self.clientes[self.editing_index] = self.edited_cliente_data.copy()
            self.editing_index = -1

    @rx.event
    def cancel_edit(self):
        self.editing_index = -1