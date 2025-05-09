
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body, primary_button_style, secondary_button_style
import uuid
import time

class PaymentView(ft.Container):
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
        self.payment_method = ""
        self.processing_payment = False
        
        self.content = self.build()
    
    def build(self):
        # Calculate totals
        subtotal = self.app_state.cart_total
        delivery_fee = 2.0 if self.app_state.delivery_method == "delivery" else 0.0
        discount = self.app_state.discount_amount
        total = subtotal + delivery_fee - discount
        
        # Payment method selection
        payment_methods = [
            {
                "id": "cash",
                "name": "الدفع عند الاستلام (نقداً)",
                "icon": ft.icons.PAYMENTS,
            },
            {
                "id": "card",
                "name": "الدفع عند الاستلام (بطاقة)",
                "icon": ft.icons.CREDIT_CARD,
            },
            {
                "id": "online_card",
                "name": "بطاقة ائتمان / خصم",
                "icon": ft.icons.CREDIT_SCORE,
            },
            {
                "id": "paypal",
                "name": "PayPal",
                "icon": ft.icons.PAYPAL,
            },
            {
                "id": "apple_pay",
                "name": "Apple Pay",
                "icon": ft.icons.APPLE,
                "disabled": True,  # Disabled for demo
            },
        ]
        
        payment_methods_list = ft.Column(spacing=10)
        
        for method in payment_methods:
            payment_methods_list.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.Radio(
                            value=method["id"], 
                            group="payment_method",
                            on_change=lambda e, method_id=method["id"]: self.select_payment_method(method_id),
                        ),
                        title=ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.Text(method["name"]),
                            ],
                        ),
                        trailing=ft.Icon(method["icon"]),
                    ),
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=8,
                    margin=ft.margin.only(bottom=5),
                    disabled=method.get("disabled", False),
                )
            )
        
        # Order summary
        order_summary = ft.Container(
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text(
                        "ملخص الطلب",
                        style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                        text_align=ft.TextAlign.RIGHT,
                    ),
                    ft.Divider(height=1),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"{subtotal:.2f} €"),
                            ft.Text("المجموع الفرعي:"),
                        ],
                    ),
                    
                    # Delivery fee (if applicable)
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"{delivery_fee:.2f} €"),
                            ft.Text("رسوم التوصيل:"),
                        ],
                        visible=delivery_fee > 0,
                    ),
                    
                    # Discount (if applicable)
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"- {discount:.2f} €", color=ft.colors.GREEN),
                            ft.Text("الخصم:"),
                        ],
                        visible=discount > 0,
                    ),
                    
                    ft.Divider(height=1),
                    
                    # Total
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                f"{total:.2f} €",
                                style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                            ),
                            ft.Text(
                                "الإجمالي:",
                                style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                            ),
                        ],
                    ),
                ],
            ),
            padding=15,
            bgcolor=ft.colors.GREY_50,
            border_radius=8,
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
                                on_click=lambda _: self.router.go("/delivery-options"),
                            ),
                            ft.Text(
                                "الدفع",
                                style=text_style_heading(size=20),
                            ),
                            ft.Container(width=40),  # Spacer for alignment
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Content
                ft.Container(
                    content=ft.Column(
                        spacing=20,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            # Payment methods
                            ft.Text(
                                "اختر طريقة الدفع",
                                style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                                text_align=ft.TextAlign.RIGHT,
                            ),
                            payment_methods_list,
                            
                            # Order summary
                            order_summary,
                            
                            # Note about payment
                            ft.Container(
                                content=ft.Text(
                                    "ملاحظة: هذه نسخة تجريبية، لن يتم معالجة أي مدفوعات فعلية.",
                                    style=text_style_body(size=12, color=ft.colors.GREY),
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                margin=ft.margin.only(top=10, bottom=60),
                            ),
                        ],
                    ),
                    padding=ft.padding.all(15),
                    expand=True,
                ),
                
                # Bottom bar with payment button
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton(
                                text="العودة",
                                style=secondary_button_style(),
                                on_click=lambda _: self.router.go("/delivery-options"),
                            ),
                            ft.ElevatedButton(
                                text="تأكيد الطلب",
                                style=primary_button_style(),
                                on_click=self.process_payment,
                                disabled=not self.payment_method or self.processing_payment,
                            ),
                        ],
                    ),
                    padding=ft.padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.only(top=ft.border.BorderSide(1, ft.colors.GREY_300)),
                ),
            ],
        )
    
    def select_payment_method(self, method_id):
        self.payment_method = method_id
        self.content = self.build()
        self.page.update()
    
    def process_payment(self, e):
        if not self.payment_method:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("يرجى اختيار طريقة الدفع"),
                action="حسناً"
            )
            self.page.snack_bar.open = True
            self.page.update()
            return
        
        self.processing_payment = True
        self.page.update()
        
        # Show progress indicator
        self.page.splash = ft.ProgressBar()
        self.page.update()
        
        # Simulate payment processing
        import asyncio
        
        async def simulate_payment():
            await asyncio.sleep(2)
            
            # Generate an order ID
            order_id = str(uuid.uuid4())[:8].upper()
            
            # Create an order (in a real app, this would be saved to a database)
            self.app_state.current_order = {
                "order_id": order_id,
                "items": self.app_state.cart_items,
                "subtotal": self.app_state.cart_total,
                "discount": self.app_state.discount_amount,
                "delivery_fee": 2.0 if self.app_state.delivery_method == "delivery" else 0.0,
                "total": self.app_state.final_total + (2.0 if self.app_state.delivery_method == "delivery" else 0.0),
                "delivery_method": self.app_state.delivery_method,
                "address": self.app_state.selected_address if self.app_state.delivery_method == "delivery" else None,
                "payment_method": self.payment_method,
                "status": "pending",
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            
            # Clear the cart
            self.app_state.clear_cart()
            
            # Hide progress indicator
            self.page.splash = None
            self.processing_payment = False
            
            # Navigate to order tracking
            self.router.go(f"/order-tracking/{order_id}")
        
        asyncio.create_task(simulate_payment())
