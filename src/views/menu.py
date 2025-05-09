
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body
from utils.data_provider import DataProvider

class MenuView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # Data
        self.categories = DataProvider.get_categories()
        self.menu_items = DataProvider.get_menu_items()
        self.selected_category = None
        
        self.content = self.build()
    
    def build(self):
        # Create category tabs
        category_tabs = []
        for i, category in enumerate(self.categories):
            category_tabs.append(
                ft.Tab(
                    text=category["name"],
                    content=self.build_menu_items_grid(category["id"]),
                    icon=ft.icons.RESTAURANT_MENU
                )
            )
        
        # Search field
        search_field = ft.TextField(
            hint_text="ابحث في القائمة...",
            prefix_icon=ft.icons.SEARCH,
            border_radius=20,
            filled=True,
            expand=True,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
            on_change=self.search_menu,
        )
        
        # Cart button with badge
        cart_badge = ft.Badge(
            content=ft.Icon(ft.icons.SHOPPING_CART, color=ft.colors.WHITE),
            text=str(self.app_state.cart_item_count) if self.app_state.cart_item_count > 0 else "",
            bgcolor=BISTRO_PRIMARY if self.app_state.cart_item_count > 0 else ft.colors.GREY,
            offset=ft.Offset(0.5, -0.5),
            visible=self.app_state.cart_item_count > 0,
        )
        
        cart_button = ft.IconButton(
            icon=ft.icons.SHOPPING_CART,
            tooltip="عربة التسوق",
            on_click=lambda _: self.router.go("/cart"),
            content=cart_badge,
        )
        
        # Build main layout
        return ft.Column(
            spacing=0,
            controls=[
                # Top bar
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            cart_button,
                            ft.Text(
                                "قائمة الطعام",
                                style=text_style_heading(size=20),
                            ),
                            # Profile icon if logged in, otherwise login button
                            ft.IconButton(
                                icon=ft.icons.PERSON if self.app_state.is_authenticated() else ft.icons.LOGIN,
                                tooltip="الملف الشخصي" if self.app_state.is_authenticated() else "تسجيل الدخول",
                                on_click=lambda _: self.router.go("/profile" if self.app_state.is_authenticated() else "/login"),
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Search bar
                ft.Container(
                    content=search_field,
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Menu tabs
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=category_tabs,
                    expand=True,
                ),
            ],
        )
    
    def build_menu_items_grid(self, category_id):
        filtered_items = [item for item in self.menu_items if item["category_id"] == category_id]
        
        menu_item_cards = []
        for item in filtered_items:
            menu_item_cards.append(self.create_menu_item_card(item))
        
        return ft.Container(
            content=ft.GridView(
                runs_count=2,
                max_extent=180,
                child_aspect_ratio=0.7,
                spacing=10,
                run_spacing=10,
                padding=15,
                controls=menu_item_cards,
            ),
            expand=True,
        )
    
    def create_menu_item_card(self, item):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    spacing=5,
                    controls=[
                        # Image
                        ft.Container(
                            content=ft.Image(
                                src=f"/assets/menu/{item['image']}",
                                width=float("inf"),
                                height=100,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.only(
                                    top_left=8, top_right=8
                                ),
                            ),
                            width=float("inf"),
                            height=100,
                            border_radius=ft.border_radius.only(
                                top_left=8, top_right=8
                            ),
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        ),
                        
                        # Name and price
                        ft.Container(
                            content=ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        item["name"],
                                        style=text_style_body(size=14, weight=ft.FontWeight.BOLD),
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                    ft.Text(
                                        item["description"],
                                        style=text_style_body(size=12, color=ft.colors.GREY),
                                        max_lines=2,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                    ft.Container(height=5),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Text(
                                                f"{item['price']} €",
                                                style=text_style_body(
                                                    size=14,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=BISTRO_PRIMARY,
                                                ),
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.ADD_CIRCLE,
                                                icon_color=BISTRO_PRIMARY,
                                                icon_size=20,
                                                tooltip="أضف إلى السلة",
                                                on_click=lambda e, id=item["id"]: self.router.go(f"/product/{id}"),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            padding=ft.padding.all(8),
                        ),
                    ],
                ),
                border_radius=8,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            ),
            elevation=2,
            on_click=lambda e, id=item["id"]: self.router.go(f"/product/{id}"),
        )
    
    def search_menu(self, e):
        search_text = e.control.value.lower()
        # This would update the displayed menu items based on the search
        # For this demo, we'll just show a message
        if search_text:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"البحث عن: {search_text}"),
                action="إلغاء"
            )
            self.page.snack_bar.open = True
            self.page.update()
