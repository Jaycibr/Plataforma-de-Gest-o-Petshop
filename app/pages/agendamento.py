import reflex as rx
from app.states.agendamento_state import AgendamentoState
from app.styles import PAGE_CARD_STYLE, PAGE_HEADER_STYLE, PAGE_SUBHEADER_STYLE


def calendar_header() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("chevron-left"),
            on_click=AgendamentoState.prev_month,
            class_name="p-2 rounded-md hover:bg-gray-100",
        ),
        rx.el.h3(
            f"{AgendamentoState.current_month_str} {AgendamentoState.current_year}",
            class_name="text-lg font-semibold w-40 text-center",
        ),
        rx.el.button(
            rx.icon("chevron-right"),
            on_click=AgendamentoState.next_month,
            class_name="p-2 rounded-md hover:bg-gray-100",
        ),
        class_name="flex items-center justify-between mb-4",
    )


def calendar_grid() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            AgendamentoState.week_days,
            lambda day: rx.el.div(
                day, class_name="text-center font-medium text-sm text-gray-500"
            ),
        ),
        rx.foreach(
            AgendamentoState.calendar_days,
            lambda day_info: rx.el.button(
                day_info["day"],
                on_click=lambda: AgendamentoState.select_day(day_info["day"]),
                class_name=rx.cond(
                    day_info["is_current_month"],
                    rx.cond(
                        AgendamentoState.selected_day == day_info["day"],
                        "p-2 text-center rounded-full bg-blue-500 text-white w-10 h-10",
                        "p-2 text-center rounded-full hover:bg-gray-100 w-10 h-10",
                    ),
                    "p-2 text-center text-gray-400 w-10 h-10",
                ),
                disabled=~day_info["is_current_month"],
            ),
        ),
        class_name="grid grid-cols-7 gap-2",
    )


def appointment_form() -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            f"Agendar para {AgendamentoState.selected_day_str}",
            class_name="text-md font-semibold mb-4",
        ),
        rx.el.div(
            rx.el.label("Horário", class_name="text-sm font-medium"),
            rx.el.select(
                rx.foreach(
                    AgendamentoState.time_slots,
                    lambda time: rx.el.option(time, value=time),
                ),
                on_change=AgendamentoState.set_selected_time,
                placeholder="Selecione um horário",
                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label("Buscar Cliente por CPF", class_name="text-sm font-medium"),
            rx.el.input(
                placeholder="Digite o CPF do cliente",
                on_change=AgendamentoState.set_search_cpf,
                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label("Cliente", class_name="text-sm font-medium"),
            rx.el.select(
                rx.foreach(
                    AgendamentoState.filtered_clients,
                    lambda client: rx.el.option(
                        client["nome_completo"], value=client["cpf"]
                    ),
                ),
                on_change=AgendamentoState.set_selected_client_cpf,
                placeholder="Selecione um cliente",
                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            ),
            class_name="mb-4",
        ),
        rx.el.button(
            "Agendar Serviço",
            on_click=AgendamentoState.create_appointment,
            class_name="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700",
        ),
        class_name="p-4 border-t mt-4",
    )


def agendamento_page() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Agenda de Serviços", style=PAGE_HEADER_STYLE),
        rx.el.p(
            "Visualize e gerencie os agendamentos de serviços.",
            style=PAGE_SUBHEADER_STYLE,
        ),
        rx.el.div(
            rx.el.div(
                calendar_header(),
                calendar_grid(),
                rx.cond(
                    AgendamentoState.selected_day > 0, appointment_form(), rx.el.div()
                ),
                class_name="p-4",
            ),
            rx.el.div(
                rx.el.h3("Agendamentos", class_name="text-lg font-semibold mb-4"),
                rx.cond(
                    AgendamentoState.appointments.length() > 0,
                    rx.el.ul(
                        rx.foreach(
                            AgendamentoState.appointments,
                            lambda apt: rx.el.li(
                                f"{apt['date']} às {apt['time']} - {apt['client_name']}",
                                class_name="p-2 border-b",
                            ),
                        ),
                        class_name="divide-y",
                    ),
                    rx.el.p(
                        "Nenhum agendamento para este mês.", class_name="text-gray-500"
                    ),
                ),
                class_name="p-4 border-t",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
        ),
        style=PAGE_CARD_STYLE,
    )