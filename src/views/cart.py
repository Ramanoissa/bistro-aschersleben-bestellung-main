
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body, primary_button_style
from utils.data_provider import DataProvider

class CartView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        self.coupon_code = ""
        self.coupon_field = ft.TextField(
            label="كود الخصم",
            hint_text="أدخل كود الخصم هنا",
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
            on_change=self.update_coupon_code,
            suffix=ft.TextButton("تطبيق", on_click=self.apply_coupon),
        )
        
        self.content = self.build()
    
    def build(self):
        if not self.app_state.cart_items:
            # Empty cart view
            return ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Icon(
                        name=ft.icons.SHOPPING_CART_OUTLINED,
                        size=80,
                        color=ft.colors.GREY_400,
                    ),
                    ft.Text(
                        "سلة التسوق فارغة",
                        style=text_style_heading(size=20),
                    ),
                    ft.Text(
                        "أضف بعض المنتجات من قائمة الطعام",
                        style=text_style_body(size=16, color=ft.colors.GREY),
                    ),
                    ft.ElevatedButton(
                        text="استعرض القائمة",
                        style=primary_button_style(),
                        on_click=lambda _: self.router.go("/menu"),
                    ),
                ],
            )
        
        # Cart items list
        cart_items_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        )
        
        for item in self.app_state.cart_items:
            cart_items_list.controls.append(self.build_cart_item(item))
        
        # Order summary
        subtotal = self.app_state.cart_total
        discount = self.app_state.discount_amount
        total = self.app_state.final_total
        
        order_summary = ft.Container(
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("المجموع الفرعي:"),
                            ft.Text(f"{subtotal:.2f} €"),
                        ],
                    ),
                    ft.Divider(height=1),
                    
                    # Coupon field
                    self.coupon_field,
                    
                    # Discount row (visible only if discount is applied)
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("الخصم:"),
                            ft.Text(f"- {discount:.2f} €", color=ft.colors.GREEN),
                        ],
                        visible=discount > 0,
                    ),
                    
                    # Total row
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    "الإجمالي:",
                                    style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                                ),
                                ft.Text(
                                    f"{total:.2f} €",
                                    style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                                ),
                            ],
                        ),
                        padding=ft.padding.symmetric(vertical=10),
                    ),
                    
                    # Checkout button
                    ft.ElevatedButton(
                        text="متابعة الطلب",
                        style=primary_button_style(),
                        width=float("inf"),
                        on_click=lambda _: self.router.go("/delivery-options"),
                    ),
                ],
            ),
            padding=ft.padding.all(15),
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
                                icon=ft.icons.DELETE_OUTLINE,
                                tooltip="إفراغ السلة",
                                on_click=self.show_clear_cart_dialog,
                            ),
                            ft.Text(
                                "سلة التسوق",
                                style=text_style_heading(size=20),
                            ),
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda _: self.router.go("/menu"),
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Cart items (scrollable)
                ft.Container(
                    content=cart_items_list,
                    padding=ft.padding.all(15),
                    expand=True,
                ),
                
                # Order summary (fixed at bottom)
                ft.Container(
                    content=order_summary,
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.only(top=ft.border.BorderSide(1, ft.colors.GREY_300)),
                ),
            ],
        )
    
    def build_cart_item(self, item):
        # Build options text
        options_text = ""
        item_options = item.options
        if isinstance(item_options, dict):
            for option_name, choice in item_options.items():
                if isinstance(choice, list):  # Multiple choices
                    choice_texts = [c["name"] for c in choice]
                    options_text += f"{option_name}: {', '.join(choice_texts)}\n"
                elif isinstance(choice, dict):  # Single choice
                    options_text += f"{option_name}: {choice['name']}\n"
        
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        # Delete button
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color=ft.colors.RED,
                            icon_size=20,
                            on_click=lambda _, item=item: self.remove_from_cart(item),
                        ),
                        
                        # Item details (middle column, expanded)
                        ft.Column(
                            spacing=5,
                            expand=True,
                            controls=[
                                ft.Text(
                                    item.name,
                                    style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Text(
                                    options_text if options_text else "بدون إضافات",
                                    style=text_style_body(size=12, color=ft.colors.GREY),
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Text(
                                    item.notes if item.notes else "",
                                    style=text_style_body(size=12, color=ft.colors.GREY_700),
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    controls=[
                                        ft.Text(
                                            f"{item.total_price:.2f} €",
                                            style=text_style_body(color=BISTRO_PRIMARY),
                                        ),
                                    ],
                                ),
                                # Quantity adjuster
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=5,
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.REMOVE,
                                            icon_size=16,
                                            on_click=lambda _, item=item: self.decrease_quantity(item),
                                        ),
                                        ft.Text(str(item.quantity)),
                                        ft.IconButton(
                                            icon=ft.icons.ADD,
                                            icon_size=16,
                                            on_click=lambda _, item=item: self.increase_quantity(item),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                padding=10,
            ),
        )
    
    def remove_from_cart(self, item):
        self.app_state.remove_from_cart(item.product_id, item.options)
        self.update_ui()
    
    def increase_quantity(self, item):
        self.app_state.update_cart_item_quantity(item.product_id, item.quantity + 1, item.options)
        self.update_ui()
    
    def decrease_quantity(self, item):
        if item.quantity > 1:
            self.app_state.update_cart_item_quantity(item.product_id, item.quantity - 1, item.options)
            self.update_ui()
    
    def show_clear_cart_dialog(self, e):
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def confirm_clear(e):
            self.app_state.clear_cart()
            close_dialog(e)
            self.update_ui()
        
        dialog = ft.AlertDialog(
            title=ft.Text("إفراغ السلة"),
            content=ft.Text("هل أنت متأكد من رغبتك في إفراغ السلة؟"),
            actions=[
                ft.TextButton("إلغاء", on_click=close_dialog),
                ft.TextButton("تأكيد", on_click=confirm_clear),
            ],
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def update_coupon_code(self, e):
        self.coupon_code = e.control.value
    
    def apply_coupon(self, e):
        if not self.coupon_code:
            self.show_message("يرجى إدخال كود الخصم")
            return
        
        coupon_result = DataProvider.validate_coupon(self.coupon_code, self.app_state.cart_total)
        
        if coupon_result["valid"]:
            self.app_state.applied_coupon = coupon_result["code"]
            self.app_state.discount_amount = coupon_result["discount_amount"]
            self.show_message(f"تم تطبيق كود الخصم! وفرت {coupon_result['discount_amount']:.2f} €")
        else:
            self.show_message(coupon_result["message"])
        
        self.update_ui()
    
    def show_message(self, message):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def update_ui(self):
        self.content = self.build()
        self.page.update()
