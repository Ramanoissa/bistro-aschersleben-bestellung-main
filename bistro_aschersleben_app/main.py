import flet as ft
from screens.home import home_screen
from screens.menu import menu_screen
from screens.cart import cart_screen
from screens.profile import profile_screen
from screens.checkout import checkout_screen
from screens.order_status import order_status_screen
from screens.login import login_screen

def main(page: ft.Page):
    # Theme und Design
    page.title = "Bistro Aschersleben"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0
    page.bgcolor = "#f5f5f5"
    
    # Theme-Farben
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#FF4B2B",
            secondary="#FF416C",
            surface="#FFFFFF",
            background="#f5f5f5",
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(size=16, color="#333333"),
            body_medium=ft.TextStyle(size=14, color="#666666"),
            title_large=ft.TextStyle(size=24, weight="bold", color="#333333"),
            title_medium=ft.TextStyle(size=20, weight="bold", color="#333333"),
        )
    )

    # Aktuelle Seite
    current = {"screen": "home"}

    def show_screen(screen_name, **kwargs):
        page.drawer.open = False
        current["screen"] = screen_name
        page.clean()
        
        # Container für den Hauptinhalt mit Padding und Hintergrund
        main_container = ft.Container(
            content=None,
            padding=20,
            bgcolor="#FFFFFF",
            border_radius=10,
            margin=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLACK12,
            )
        )
        
        if screen_name == "home":
            main_container.content = home_screen(page)
        elif screen_name == "menu":
            main_container.content = menu_screen(page)
        elif screen_name == "cart":
            main_container.content = cart_screen(page)
        elif screen_name == "profile":
            main_container.content = profile_screen(page)
        elif screen_name == "checkout":
            main_container.content = checkout_screen(page)
        elif screen_name == "order_status":
            main_container.content = order_status_screen(page, **kwargs)
        elif screen_name == "login":
            main_container.content = login_screen(page)
            
        page.add(main_container)

    # Make show_screen available to all screens
    page.show_screen = show_screen

    # Drawer-Menü mit verbessertem Design
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Image(
                            src="/assets/logo.png",
                            width=120,
                            height=120,
                            fit=ft.ImageFit.COVER,
                        ),
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.BLACK12,
                        ),
                        margin=ft.Margin(0, 0, 0, 20),  # left, top, right, bottom
                    ),
                    ft.Text("Bistro Aschersleben", size=22, weight="bold", color="#333333"),
                    ft.Divider(height=20),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.HOME, color="#FF4B2B"),
                        title=ft.Text("Home", color="#333333"),
                        on_click=lambda e: show_screen("home")
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.MENU_BOOK, color="#FF4B2B"),
                        title=ft.Text("Menü", color="#333333"),
                        on_click=lambda e: show_screen("menu")
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.SHOPPING_CART, color="#FF4B2B"),
                        title=ft.Text("Warenkorb", color="#333333"),
                        on_click=lambda e: show_screen("cart")
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON, color="#FF4B2B"),
                        title=ft.Text("Profil", color="#333333"),
                        on_click=lambda e: show_screen("profile")
                    ),
                ], expand=True),
                padding=20,
                bgcolor="#FFFFFF"
            )
        ],
        bgcolor="#FFFFFF"
    )

    # AppBar mit verbessertem Design
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.MENU,
            icon_color="#FF4B2B",
            on_click=lambda e: setattr(page.drawer, 'open', True)
        ),
        title=ft.Text(
            "Bistro Aschersleben",
            color="#333333",
            weight="bold"
        ),
        bgcolor="#FFFFFF",
        elevation=0,
        center_title=True
    )

    # Startseite anzeigen
    show_screen("home")

ft.app(target=main)
