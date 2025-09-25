import reflex as rx

BASE_STYLES = {"font_family": "Lato", "background_color": "#F4F4F5"}
SIDEBAR_STYLES = {
    "width": "250px",
    "height": "100vh",
    "padding": "1.5rem",
    "background_color": "#FFFFFF",
    "border_right": "1px solid #E4E4E7",
}
MENU_ITEM_BASE_STYLE = "flex items-center w-full px-4 py-2.5 rounded-lg text-sm font-medium text-gray-700 transition-colors duration-150"
MENU_ITEM_INACTIVE_STYLE = f"{MENU_ITEM_BASE_STYLE} hover:bg-gray-100"
MENU_ITEM_ACTIVE_STYLE = f"{MENU_ITEM_BASE_STYLE} bg-blue-500 text-white"
MAIN_CONTENT_STYLES = {
    "padding": "2rem",
    "width": "calc(100% - 250px)",
    "height": "100vh",
    "overflow_y": "auto",
}
PAGE_CARD_STYLE = {
    "background_color": "#FFFFFF",
    "border_radius": "12px",
    "padding": "2rem",
    "border": "1px solid #E4E4E7",
    "box_shadow": "0 4px 8px -1px rgba(0,0,0,0.05)",
}
PAGE_HEADER_STYLE = {
    "font_size": "2rem",
    "font_weight": "bold",
    "color": "#18181B",
    "margin_bottom": "1rem",
}
PAGE_SUBHEADER_STYLE = {
    "font_size": "1rem",
    "color": "#71717A",
    "margin_bottom": "2rem",
}