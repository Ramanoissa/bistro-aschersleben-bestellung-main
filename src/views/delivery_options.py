
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body, primary_button_style, secondary_button_style

class DeliveryOptionsView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # If cart is empty, redirect to menu
        if not self.app_state.cart_items:
            self.router.go("/menu")
            return
        
        # State
        self.delivery_method = self.app_state.delivery_method  # "delivery" or "pickup"
        self.selected_address = self.app_state.selected_address
        
        # Form fields
        self.address_fields = {
            "name": ft.TextField(
                label="الاسم على الجرس",
                text_direction=ft.TextDirection.RTL,
                text_align=ft.TextAlign.RIGHT,
            ),
            "street": ft.TextField(
                label="الشارع ورقم المنزل",
                text_direction=ft.TextDirection.RTL,
                text_align=ft.TextAlign.RIGHT,
            ),
            "city": ft.TextField(
                label="المدينة",
                text_direction=ft.TextDirection.RTL,
                text_align=ft.TextAlign.RIGHT,
                value="Aschersleben",
            ),
            "postcode": ft.TextField(
                label="الرمز البريدي",
                text_direction=ft.TextDirection.RTL,
                text_align=ft.TextAlign.RIGHT,
                value="06449",
            ),
            "instructions": ft.TextField(
                label="تعليمات إضافية (اختياري)",
                hint_text="مثال: الطابق الثاني",
                multiline=True,
                min_lines=1,
                max_lines=3,
                text_direction=ft.TextDirection.RTL,
                text_align=ft.TextAlign.RIGHT,
            ),
        }
        
        # Pre-fill address fields if user has selected an address
        if self.selected_address:
            for field, value in self.selected_address.items():
                if field in self.address_fields:
                    self.address_fields[field].value = value
        
        self.content = self.build()
    
    def build(self):
        # Build saved addresses list if user is logged in
        saved_addresses_view = None
        if self.app_state.is_authenticated() and hasattr(self.app_state.user, "addresses") and self.app_state.user.addresses:
            address_items = []
            for address in self.app_state.user.addresses:
                address_items.append(self.build_address_item(address))
            
            saved_addresses_view = ft.Column(
                spacing=10,
                controls=[
                    ft.Text(
                        "العناوين المحفوظة",
                        style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                        text_align=ft.TextAlign.RIGHT,
                    ),
                    ft.Column(controls=address_items),
                ],
            )
        
        # Delivery options tab
        tabs = ft.Tabs(
            selected_index=0 if self.delivery_method == "delivery" else 1,
            on_change=self.change_delivery_method,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="توصيل للمنزل",
                    icon=ft.icons.DELIVERY_DINING,
                    content=ft.Container(
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                # Saved addresses (if available)
                                saved_addresses_view if saved_addresses_view else ft.Container(),
                                
                                ft.Text(
                                    "عنوان التوصيل",
                                    style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                
                                # Address form
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        self.address_fields["name"],
                                        self.address_fields["street"],
                                        ft.Row(
                                            controls=[
                                                self.address_fields["postcode"],
                                                self.address_fields["city"],
                                            ],
                                            spacing=10,
                                        ),
                                        self.address_fields["instructions"],
                                        
                                        # Save address checkbox (if logged in)
                                        ft.Checkbox(
                                            label="حفظ هذا العنوان للطلبات المستقبلية",
                                            value=False,
                                            visible=self.app_state.is_authenticated(),
                                        ),
                                    ],
                                ),
                                
                                # Delivery info
                                ft.Container(
                                    content=ft.Column(
                                        spacing=5,
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(ft.icons.ACCESS_TIME),
                                                    ft.Text("وقت التوصيل: 30-45 دقيقة"),
                                                ],
                                            ),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(ft.icons.EURO),
                                                    ft.Text("رسوم التوصيل: 2.00 €"),
                                                ],
                                            ),
                                        ],
                                    ),
                                    padding=10,
                                    border_radius=8,
                                    bgcolor=ft.colors.GREY_100,
                                ),
                            ],
                        ),
                        padding=ft.padding.only(top=20),
                    ),
                ),
                ft.Tab(
                    text="استلام من المطعم",
                    icon=ft.icons.STORE,
                    content=ft.Container(
                        content=ft.Column(
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STORE,
                                    size=60,
                                    color=BISTRO_PRIMARY,
                                ),
                                ft.Text(
                                    "استلام من المطعم",
                                    style=text_style_heading(size=20),
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        spacing=5,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                "Bistro Aschersleben",
                                                style=text_style_body(size=18),
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                            ft.Text(
                                                "Herrenbreite 12, 06449 Aschersleben",
                                                style=text_style_body(size=16),
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                            ft.Text(
                                                "وقت التحضير: 15-20 دقيقة",
                                                style=text_style_body(size=14),
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                        ],
                                    ),
                                    padding=20,
                                    bgcolor=ft.colors.GREY_100,
                                    border_radius=8,
                                ),
                                ft.TextButton(
                                    text="عرض الموقع على الخريطة",
                                    icon=ft.icons.MAP,
                                    on_click=self.open_map,
                                ),
                            ],
                        ),
                        padding=ft.padding.only(top=20),
                    ),
                ),
            ],
        )
        
        return ft.Column(
            spacing=0,
            controls=[
                # Top bar
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda _: self.router.go("/cart"),
                            ),
                            ft.Text(
                                "خيارات الاستلام",
                                style=text_style_heading(size=20),
                            ),
                            ft.Container(width=40),  # Spacer for alignment
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Tabs
                ft.Container(
                    content=tabs,
                    padding=ft.padding.symmetric(horizontal=15),
                    expand=True,
                ),
                
                # Bottom bar with continue button
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton(
                                text="العودة إلى السلة",
                                style=secondary_button_style(),
                                on_click=lambda _: self.router.go("/cart"),
                            ),
                            ft.ElevatedButton(
                                text="متابعة للدفع",
                                style=primary_button_style(),
                                on_click=self.continue_to_payment,
                            ),
                        ],
                    ),
                    padding=ft.padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.only(top=ft.border.BorderSide(1, ft.colors.GREY_300)),
                ),
            ],
        )
    
    def build_address_item(self, address):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    spacing=5,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Radio(
                                    value=address["id"],
                                    group="address",
                                    on_change=lambda e, addr=address: self.select_saved_address(addr),
                                ),
                                ft.Text(
                                    address["name"],
                                    style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                ),
                            ],
                        ),
                        ft.Text(
                            address["street"],
                            style=text_style_body(size=14),
                        ),
                        ft.Text(
                            f"{address['postcode']} {address['city']}",
                            style=text_style_body(size=14),
                        ),
                        ft.Text(
                            address.get("instructions", ""),
                            style=text_style_body(size=12, color=ft.colors.GREY),
                        ),
                    ],
                ),
                padding=10,
            ),
        )
    
    def select_saved_address(self, address):
        self.selected_address = address
        
        # Update form fields
        for field, value in address.items():
            if field in self.address_fields:
                self.address_fields[field].value = value
        
        self.page.update()
    
    def change_delivery_method(self, e):
        # Update the delivery method based on tab index
        self.delivery_method = "delivery" if e.control.selected_index == 0 else "pickup"
        self.app_state.delivery_method = self.delivery_method
        self.page.update()
    
    def open_map(self, e):
        # In a real app, this would open a map with the store location
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("سيتم فتح الموقع على الخريطة"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def validate_delivery_form(self):
        if self.delivery_method == "delivery":
            required_fields = ["name", "street"]
            for field_name in required_fields:
                if not self.address_fields[field_name].value:
                    self.page.snack_bar = ft.SnackBar(
                        content=ft.Text(f"يرجى ملء حقل {self.address_fields[field_name].label}"),
                        action="حسناً"
                    )
                    self.page.snack_bar.open = True
                    self.page.update()
                    return False
            
            # Create address object from form
            self.selected_address = {
                "name": self.address_fields["name"].value,
                "street": self.address_fields["street"].value,
                "city": self.address_fields["city"].value,
                "postcode": self.address_fields["postcode"].value,
                "instructions": self.address_fields["instructions"].value,
            }
        
        return True
    
    def continue_to_payment(self, e):
        if self.validate_delivery_form():
            # Save the delivery method and address to app state
            self.app_state.delivery_method = self.delivery_method
            self.app_state.selected_address = self.selected_address
            
            # Navigate to payment page
            self.router.go("/payment")
