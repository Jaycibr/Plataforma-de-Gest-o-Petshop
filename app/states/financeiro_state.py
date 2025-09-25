import reflex as rx
from typing import TypedDict
from collections import defaultdict


class Transacao(TypedDict):
    descricao: str
    valor: float
    data: str


class FinanceiroState(rx.State):
    valores_recebidos: list[Transacao] = [
        {"descricao": "Serviço de Banho e Tosa", "valor": 120.0, "data": "2024-07-20"},
        {"descricao": "Venda de Ração Premium", "valor": 250.0, "data": "2024-07-20"},
    ]
    valores_gastos: list[Transacao] = [
        {"descricao": "Aluguel", "valor": 50.0, "data": "2024-07-19"},
        {"descricao": "Compra de Shampoos", "valor": 80.0, "data": "2024-07-18"},
    ]

    @rx.var
    def lucro(self) -> list[Transacao]:
        total_recebido = sum((t["valor"] for t in self.valores_recebidos))
        total_gasto = sum((t["valor"] for t in self.valores_gastos))
        lucro_total = total_recebido - total_gasto
        return [
            {"descricao": "Lucro Total do Período", "valor": lucro_total, "data": "--"}
        ]

    @rx.var
    def chart_data(self) -> list[dict]:
        daily_totals = defaultdict(lambda: {"recebidos": 0, "gastos": 0})
        for transacao in self.valores_recebidos:
            daily_totals[transacao["data"]]["recebidos"] += transacao["valor"]
        for transacao in self.valores_gastos:
            daily_totals[transacao["data"]]["gastos"] += transacao["valor"]
        sorted_dates = sorted(daily_totals.keys())
        chart_data = []
        for date in sorted_dates:
            chart_data.append(
                {
                    "data": date,
                    "recebidos": daily_totals[date]["recebidos"],
                    "gastos": daily_totals[date]["gastos"],
                }
            )
        return chart_data