import reflex as rx
from app.states.state import State
from app.styles import SIDEBAR_STYLES, MENU_ITEM_INACTIVE_STYLE, MENU_ITEM_ACTIVE_STYLE


def sidebar_menu_item(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=item["icon"], class_name="mr-3 h-5 w-5"),
        rx.el.span(item["name"]),
        class_name=rx.cond(
            State.active_page == item["page"],
            MENU_ITEM_ACTIVE_STYLE,
            MENU_ITEM_INACTIVE_STYLE,
        ),
        on_click=lambda: State.set_active_page(item["page"]),
        cursor="pointer",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("paw-print", class_name="h-8 w-8 text-blue-500"),
            rx.el.h1("PetPlat", class_name="text-2xl font-bold ml-2 text-gray-900"),
            class_name="flex items-center mb-10",
        ),
        rx.el.div(
            rx.foreach(State.menu_items, sidebar_menu_item),
            class_name="flex flex-col space-y-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed=Admin",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p("Admin", class_name="text-sm font-semibold text-gray-800"),
                    rx.el.p("admin@petplat.com", class_name="text-xs text-gray-500"),
                    class_name="ml-3",
                ),
                class_name="flex items-center",
            ),
            rx.icon(
                "log-out",
                class_name="h-5 w-5 text-gray-500 hover:text-red-500 cursor-pointer",
            ),
            class_name="flex items-center justify-between mt-auto pt-6 border-t border-gray-200",
        ),
        style=SIDEBAR_STYLES,
        class_name="flex flex-col",
    )