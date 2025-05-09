
import flet as ft
from views.intro import IntroView
from views.login import LoginView
from views.signup import SignupView
from views.menu import MenuView
from views.product_detail import ProductDetailView
from views.cart import CartView
from views.delivery_options import DeliveryOptionsView
from views.payment import PaymentView
from views.order_tracking import OrderTrackingView
from views.profile import ProfileView
from views.offers import OffersView
from utils.app_state import AppState
from utils.theme import app_theme, BISTRO_PRIMARY, BISTRO_SECONDARY

def main(page: ft.Page):
    # Initialize app state
    app_state = AppState()
    
    # Configure the page
    page.title = "Bistro Aschersleben"
    page.theme = app_theme
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Set up responsive design
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    # App bar setup
    def handle_nav_bar_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            router.go("/menu")
        elif selected_index == 1:
            router.go("/cart")
        elif selected_index == 2:
            router.go("/offers")
        elif selected_index == 3:
            router.go("/profile")
            
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.MENU_BOOK, 
                label="القائمة"
            ),
            ft.NavigationDestination(
                icon=ft.icons.SHOPPING_CART,
                label="السلة"
            ),
            ft.NavigationDestination(
                icon=ft.icons.LOCAL_OFFER,
                label="العروض"
            ),
            ft.NavigationDestination(
                icon=ft.icons.PERSON,
                label="الحساب"
            ),
        ],
        on_change=handle_nav_bar_change,
    )

    # Container to hold the current view
    content_container = ft.Container(
        expand=True,
        content=ft.Text("جاري التحميل..."),
    )

    # Set up router
    def route_change(e):
        route = e.route
        content_container.content = ft.Text("جاري التحميل...")

        # Show nav bar by default
        page.overlay.append(navigation_bar)

        # Route handling
        if route == "/":
            navigation_bar.selected_index = None
            content_container.content = IntroView(page, router, app_state)
        elif route == "/login":
            navigation_bar.selected_index = None
            content_container.content = LoginView(page, router, app_state)
        elif route == "/signup":
            navigation_bar.selected_index = None
            content_container.content = SignupView(page, router, app_state)
        elif route == "/menu":
            navigation_bar.selected_index = 0
            content_container.content = MenuView(page, router, app_state)
        elif route.startswith("/product/"):
            navigation_bar.selected_index = 0
            product_id = route.split("/")[-1]
            content_container.content = ProductDetailView(page, router, app_state, product_id)
        elif route == "/cart":
            navigation_bar.selected_index = 1
            content_container.content = CartView(page, router, app_state)
        elif route == "/delivery-options":
            navigation_bar.selected_index = None
            content_container.content = DeliveryOptionsView(page, router, app_state)
        elif route == "/payment":
            navigation_bar.selected_index = None
            content_container.content = PaymentView(page, router, app_state)
        elif route.startswith("/order-tracking/"):
            navigation_bar.selected_index = None
            order_id = route.split("/")[-1]
            content_container.content = OrderTrackingView(page, router, app_state, order_id)
        elif route == "/profile":
            navigation_bar.selected_index = 3
            content_container.content = ProfileView(page, router, app_state)
        elif route == "/offers":
            navigation_bar.selected_index = 2
            content_container.content = OffersView(page, router, app_state)
        else:
            content_container.content = ft.Text("404 - الصفحة غير موجودة!")

        page.update()

    def view_pop(e):
        page.go(page.route)
        page.update()

    router = ft.RouterControl(route_change, view_pop)
    page.on_route_change = router.route_change
    page.on_view_pop = router.view_pop

    # Main content layout
    page.add(
        ft.Column([
            content_container
        ], expand=True)
    )

    # Initialize with intro page
    page.go("/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
