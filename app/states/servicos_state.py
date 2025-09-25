import reflex as rx
from typing import TypedDict
import datetime
from app.states.financeiro_state import FinanceiroState, Transacao


class Servico(TypedDict):
    nome: str
    valor: float


class ServicosState(rx.State):
    servicos: list[Servico] = [
        {"nome": "Banho e Tosa", "valor": 80.0},
        {"nome": "Banho, Tosa e Corte de Unha", "valor": 100.0},
        {"nome": "Banho, Tosa, Unha e Dentes", "valor": 120.0},
        {"nome": "Banho", "valor": 50.0},
        {"nome": "Tosa", "valor": 40.0},
        {"nome": "Corte de Unhas", "valor": 20.0},
        {"nome": "Escovação de Dentes", "valor": 25.0},
    ]

    async def add_servico_transacao(self, servico: Servico):
        financeiro_state = await self.get_state(FinanceiroState)
        nova_transacao: Transacao = {
            "descricao": f"Serviço: {servico['nome']}",
            "valor": servico["valor"],
            "data": datetime.date.today().isoformat(),
        }
        financeiro_state.valores_recebidos.append(nova_transacao)
        return rx.toast.success(
            f"""Serviço "{servico['nome']}" adicionado aos recebidos!"""
        )