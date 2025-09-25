import reflex as rx
from typing import TypedDict
import datetime
from app.states.cliente_state import ClienteState, Cliente


class Appointment(TypedDict):
    date: str
    time: str
    client_cpf: str
    client_name: str


class AgendamentoState(rx.State):
    appointments: list[Appointment] = []
    current_date: datetime.date = datetime.date.today()
    selected_day: int = 0
    selected_time: str = ""
    selected_client_cpf: str = ""
    search_cpf: str = ""
    time_slots: list[str] = [
        "09:00",
        "10:00",
        "11:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
    ]

    @rx.var
    def current_year(self) -> int:
        return self.current_date.year

    @rx.var
    def current_month(self) -> int:
        return self.current_date.month

    @rx.var
    def current_month_str(self) -> str:
        return self.current_date.strftime("%B").capitalize()

    @rx.var
    def week_days(self) -> list[str]:
        return ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

    @rx.var
    def calendar_days(self) -> list[dict]:
        first_day = self.current_date.replace(day=1)
        last_day_of_prev_month = first_day - datetime.timedelta(days=1)
        days = []
        for i in range(first_day.weekday()):
            day = last_day_of_prev_month.day - (first_day.weekday() - 1 - i)
            days.append({"day": day, "is_current_month": False})
        days_in_month = (
            first_day.replace(month=first_day.month % 12 + 1, day=1)
            - datetime.timedelta(days=1)
        ).day
        for day in range(1, days_in_month + 1):
            days.append({"day": day, "is_current_month": True})
        last_day_of_month = first_day.replace(day=days_in_month)
        days_from_next = 6 - last_day_of_month.weekday()
        for i in range(1, days_from_next + 1):
            days.append({"day": i, "is_current_month": False})
        first_day_weekday_sunday_start = (first_day.weekday() + 1) % 7
        days = []
        for i in range(first_day_weekday_sunday_start):
            day = last_day_of_prev_month.day - (first_day_weekday_sunday_start - 1 - i)
            days.append({"day": day, "is_current_month": False})
        for day in range(1, days_in_month + 1):
            days.append({"day": day, "is_current_month": True})
        last_day_of_month_sunday_start = (last_day_of_month.weekday() + 1) % 7
        days_from_next = 6 - last_day_of_month_sunday_start
        for i in range(1, days_from_next + 1):
            days.append({"day": i, "is_current_month": False})
        return days

    @rx.var
    def selected_day_str(self) -> str:
        if self.selected_day > 0:
            return (
                f"{self.selected_day:02d}/{self.current_month:02d}/{self.current_year}"
            )
        return ""

    @rx.var
    async def filtered_clients(self) -> list[Cliente]:
        cliente_state = await self.get_state(ClienteState)
        if not self.search_cpf:
            return cliente_state.clientes
        return [
            c
            for c in cliente_state.clientes
            if self.search_cpf.lower() in c["cpf"].lower()
        ]

    @rx.event
    def next_month(self):
        self.selected_day = 0
        self.current_date = (
            self.current_date.replace(day=1) + datetime.timedelta(days=32)
        ).replace(day=1)

    @rx.event
    def prev_month(self):
        self.selected_day = 0
        self.current_date = (
            self.current_date.replace(day=1) - datetime.timedelta(days=1)
        ).replace(day=1)

    @rx.event
    def select_day(self, day: int):
        self.selected_day = day

    @rx.event
    async def create_appointment(self):
        if (
            not self.selected_day
            or not self.selected_time
            or (not self.selected_client_cpf)
        ):
            return rx.toast.error("Por favor, preencha todos os campos.")
        cliente_state = await self.get_state(ClienteState)
        client_name = "Cliente não encontrado"
        for c in cliente_state.clientes:
            if c["cpf"] == self.selected_client_cpf:
                client_name = c["nome_completo"]
                break
        new_appointment: Appointment = {
            "date": self.selected_day_str,
            "time": self.selected_time,
            "client_cpf": self.selected_client_cpf,
            "client_name": client_name,
        }
        self.appointments.append(new_appointment)
        self.selected_day = 0
        self.selected_time = ""
        self.selected_client_cpf = ""
        self.search_cpf = ""
        return rx.toast.success("Agendamento criado com sucesso!")