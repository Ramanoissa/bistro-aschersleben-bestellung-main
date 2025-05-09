
import flet as ft
from utils.theme import BISTRO_PRIMARY, text_style_heading, text_style_body, primary_button_style

class ProfileView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # Redirect to login if not authenticated
        if not self.app_state.is_authenticated():
            self.router.go("/login")
            return
        
        self.user = self.app_state.user
        self.content = self.build()
    
    def build(self):
        # Mock order history for demo
        order_history = [
            {
                "id": "ORD12345",
                "date": "2023-05-01 19:30",
                "total": 24.99,
                "status": "delivered",
                "items": ["برجر كلاسيك", "بطاطس كبيرة", "كولا"]
            },
            {
                "id": "ORD12289",
                "date": "2023-04-25 20:15",
                "total": 32.50,
                "status": "delivered",
                "items": ["بيتزا مارجريتا وسط", "سلطة يونانية", "عصير برتقال"]
            }
        ]
        
        # Create order history list
        order_history_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        )
        
        if order_history:
            for order in order_history:
                order_history_list.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Text(
                                                order["date"],
                                                style=text_style_body(size=12, color=ft.colors.GREY),
                                            ),
                                            ft.Text(
                                                f"#{order['id']}",
                                                style=text_style_body(size=14, weight=ft.FontWeight.BOLD),
                                            ),
                                        ],
                                    ),
                                    ft.Text(
                                        ", ".join(order["items"]),
                                        style=text_style_body(size=14),
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(
                                                    self.get_status_text(order["status"]),
                                                    color=ft.colors.WHITE,
                                                    size=12,
                                                ),
                                                padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                                border_radius=15,
                                                bgcolor=self.get_status_color(order["status"]),
                                            ),
                                            ft.Text(
                                                f"{order['total']:.2f} €",
                                                style=text_style_body(
                                                    size=14,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=BISTRO_PRIMARY,
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.END,
                                        controls=[
                                            ft.TextButton(
                                                "إعادة الطلب",
                                                icon=ft.icons.REFRESH,
                                                on_click=lambda _, order_id=order["id"]: self.reorder(order_id),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            padding=15,
                        ),
                    )
                )
        else:
            order_history_list.controls.append(
                ft.Container(
                    content=ft.Text(
                        "لا توجد طلبات سابقة",
                        style=text_style_body(size=14, color=ft.colors.GREY),
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=20),
                )
            )
        
        # Create saved addresses list
        saved_addresses_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        )
        
        if hasattr(self.user, "addresses") and self.user.addresses:
            for address in self.user.addresses:
                saved_addresses_list.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                spacing=5,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Row(
                                                spacing=5,
                                                controls=[
                                                    ft.IconButton(
                                                        icon=ft.icons.EDIT,
                                                        icon_size=16,
                                                        on_click=lambda _, addr_id=address["id"]: self.edit_address(addr_id),
                                                    ),
                                                    ft.IconButton(
                                                        icon=ft.icons.DELETE,
                                                        icon_size=16,
                                                        icon_color=ft.colors.RED,
                                                        on_click=lambda _, addr_id=address["id"]: self.delete_address(addr_id),
                                                    ),
                                                ],
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
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                    ft.Text(
                                        f"{address['postcode']} {address['city']}",
                                        style=text_style_body(size=14),
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                    ft.Text(
                                        address.get("instructions", ""),
                                        style=text_style_body(size=12, color=ft.colors.GREY),
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                ],
                            ),
                            padding=15,
                        ),
                    )
                )
            
            # Add button for new address
            saved_addresses_list.controls.append(
                ft.ElevatedButton(
                    "إضافة عنوان جديد",
                    icon=ft.icons.ADD,
                    on_click=self.add_new_address,
                    style=primary_button_style(),
                    width=float("inf"),
                )
            )
        else:
            saved_addresses_list.controls.extend([
                ft.Container(
                    content=ft.Text(
                        "لا توجد عناوين محفوظة",
                        style=text_style_body(size=14, color=ft.colors.GREY),
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=20),
                ),
                ft.ElevatedButton(
                    "إضافة عنوان جديد",
                    icon=ft.icons.ADD,
                    on_click=self.add_new_address,
                    style=primary_button_style(),
                    width=float("inf"),
                )
            ])
        
        return ft.Column(
            spacing=0,
            controls=[
                # Top bar
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.LOGOUT,
                                tooltip="تسجيل الخروج",
                                on_click=self.show_logout_dialog,
                            ),
                            ft.Text(
                                "حسابي",
                                style=text_style_heading(size=20),
                            ),
                            ft.IconButton(
                                icon=ft.icons.SETTINGS,
                                tooltip="الإعدادات",
                                on_click=self.open_settings,
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # User info
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.CircleAvatar(
                                content=ft.Text(
                                    self.user.name[0] if hasattr(self.user, "name") and self.user.name else "؟",
                                    size=30,
                                ),
                                bgcolor=BISTRO_PRIMARY,
                                foreground_color=ft.colors.WHITE,
                                radius=40,
                            ),
                            ft.Text(
                                self.user.name if hasattr(self.user, "name") else "مستخدم",
                                style=text_style_heading(size=20),
                            ),
                            ft.Text(
                                self.user.email if hasattr(self.user, "email") else "بدون بريد إلكتروني",
                                style=text_style_body(size=16, color=ft.colors.GREY),
                            ),
                            ft.TextButton(
                                "تعديل الملف الشخصي",
                                icon=ft.icons.EDIT,
                                on_click=self.edit_profile,
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(vertical=20),
                ),
                
                # Tabs for order history and addresses
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="طلباتي",
                            icon=ft.icons.RECEIPT_LONG,
                            content=ft.Container(
                                content=order_history_list,
                                padding=ft.padding.all(15),
                            ),
                        ),
                        ft.Tab(
                            text="عناويني",
                            icon=ft.icons.LOCATION_ON,
                            content=ft.Container(
                                content=saved_addresses_list,
                                padding=ft.padding.all(15),
                            ),
                        ),
                    ],
                    expand=True,
                ),
            ],
        )
    
    def get_status_text(self, status):
        status_texts = {
            "pending": "قيد الانتظار",
            "preparing": "قيد التحضير",
            "out_for_delivery": "في الطريق",
            "delivered": "تم التسليم",
            "cancelled": "تم الإلغاء"
        }
        return status_texts.get(status, status)
    
    def get_status_color(self, status):
        status_colors = {
            "pending": ft.colors.ORANGE,
            "preparing": ft.colors.BLUE,
            "out_for_delivery": ft.colors.AMBER_700,
            "delivered": ft.colors.GREEN,
            "cancelled": ft.colors.RED
        }
        return status_colors.get(status, ft.colors.GREY)
    
    def reorder(self, order_id):
        # In a real app, this would add the items from the previous order to the cart
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"جاري إعادة الطلب {order_id}..."),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def edit_address(self, address_id):
        # In a real app, this would open an address edit form
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"تعديل العنوان {address_id}"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def delete_address(self, address_id):
        # In a real app, this would delete the address after confirmation
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def confirm_delete(e):
            # Delete the address (in a real app, this would call an API)
            if hasattr(self.user, "addresses"):
                self.user.addresses = [addr for addr in self.user.addresses if addr["id"] != address_id]
            close_dialog(e)
            self.content = self.build()
            self.page.update()
            
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("تم حذف العنوان"),
                action="حسناً"
            )
            self.page.snack_bar.open = True
            self.page.update()
        
        dialog = ft.AlertDialog(
            title=ft.Text("حذف العنوان"),
            content=ft.Text("هل أنت متأكد من رغبتك في حذف هذا العنوان؟"),
            actions=[
                ft.TextButton("إلغاء", on_click=close_dialog),
                ft.TextButton("تأكيد", on_click=confirm_delete),
            ],
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def add_new_address(self, e):
        # In a real app, this would open an address form
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("إضافة عنوان جديد"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def edit_profile(self, e):
        # In a real app, this would open a profile edit form
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("تعديل الملف الشخصي"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def open_settings(self, e):
        # In a real app, this would open settings page
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("إعدادات الحساب"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def show_logout_dialog(self, e):
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def confirm_logout(e):
            self.app_state.logout()
            close_dialog(e)
            self.router.go("/")
        
        dialog = ft.AlertDialog(
            title=ft.Text("تسجيل الخروج"),
            content=ft.Text("هل أنت متأكد من رغبتك في تسجيل الخروج؟"),
            actions=[
                ft.TextButton("إلغاء", on_click=close_dialog),
                ft.TextButton("تأكيد", on_click=confirm_logout),
            ],
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
