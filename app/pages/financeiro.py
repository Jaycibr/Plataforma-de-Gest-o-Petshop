import reflex as rx
from app.states.financeiro_state import FinanceiroState
from app.styles import PAGE_CARD_STYLE, PAGE_HEADER_STYLE, PAGE_SUBHEADER_STYLE


def finance_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Visão Geral Financeira",
            class_name="text-lg font-semibold text-gray-800 mb-4",
        ),
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.x_axis(data_key="data"),
            rx.recharts.y_axis(),
            rx.recharts.tooltip(),
            rx.recharts.legend(),
            rx.recharts.line(type_="monotone", data_key="recebidos", stroke="#3b82f6"),
            rx.recharts.line(type_="monotone", data_key="gastos", stroke="#ef4444"),
            data=FinanceiroState.chart_data,
            height=300,
            class_name="w-full",
        ),
        class_name="mb-8 p-4 bg-white rounded-lg shadow",
    )


def finance_table(title: str, data: rx.Var, columns: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800 mb-4"),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.foreach(
                            columns,
                            lambda col: rx.el.th(
                                col,
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                        ),
                        class_name="bg-gray-50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        data,
                        lambda row, index: rx.el.tr(
                            rx.el.td(
                                row["descricao"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                            ),
                            rx.el.td(
                                f"R$ {row['valor'].to_string()}",
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                            ),
                            rx.el.td(
                                row["data"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                            ),
                            class_name=rx.cond(
                                index % 2 == 0, "bg-white", "bg-gray-50"
                            ),
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
        ),
        class_name="mb-8",
    )


def financeiro_page() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Painel Financeiro", style=PAGE_HEADER_STYLE),
        rx.el.p(
            "Acompanhe as finanças, receitas e despesas.", style=PAGE_SUBHEADER_STYLE
        ),
        finance_chart(),
        finance_table(
            "Valores Recebidos",
            FinanceiroState.valores_recebidos,
            ["Descrição", "Valor", "Data"],
        ),
        finance_table(
            "Valores Gastos",
            FinanceiroState.valores_gastos,
            ["Descrição", "Valor", "Data"],
        ),
        finance_table(
            "Lucro (Recebidos - Gastos)",
            FinanceiroState.lucro,
            ["Descrição", "Valor", "Data"],
        ),
        style=PAGE_CARD_STYLE,
    )