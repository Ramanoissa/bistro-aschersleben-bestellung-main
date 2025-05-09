
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, primary_button_style

class SignupView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # Form fields
        self.name_field = ft.TextField(
            label="الاسم الكامل",
            autofocus=True,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
        )
        
        self.email_field = ft.TextField(
            label="البريد الإلكتروني",
            keyboard_type=ft.KeyboardType.EMAIL,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
        )
        
        self.phone_field = ft.TextField(
            label="رقم الهاتف",
            keyboard_type=ft.KeyboardType.PHONE,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
        )
        
        self.password_field = ft.TextField(
            label="كلمة المرور",
            password=True,
            can_reveal_password=True,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
        )
        
        self.confirm_password_field = ft.TextField(
            label="تأكيد كلمة المرور",
            password=True,
            can_reveal_password=True,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
        )
        
        self.error_text = ft.Text(
            "",
            color=ft.colors.RED,
            size=14,
            visible=False,
            text_align=ft.TextAlign.CENTER,
        )
        
        self.loading = False
        self.content = self.build()
    
    def build(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                # Top bar with back button
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda _: self.router.go("/"),
                            ),
                            ft.Text("إنشاء حساب جديد", style=text_style_heading(size=20)),
                            ft.Container(width=40),  # Spacer for alignment
                        ]
                    ),
                    margin=ft.margin.only(top=20, left=10, right=10),
                ),
                
                # Form
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                self.name_field,
                                self.email_field,
                                self.phone_field,
                                self.password_field,
                                self.confirm_password_field,
                                self.error_text,
                                ft.ElevatedButton(
                                    text="إنشاء حساب",
                                    style=primary_button_style(),
                                    on_click=self.handle_signup,
                                    width=float("inf"),
                                ),
                            ],
                        ),
                        padding=20,
                        width=float("inf"),
                    ),
                    width=float("inf"),
                    margin=ft.margin.symmetric(horizontal=20),
                ),
                
                # Login link
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Text("لديك حساب بالفعل؟"),
                        ft.TextButton(
                            "تسجيل الدخول",
                            on_click=lambda _: self.router.go("/login"),
                        ),
                    ]
                ),
                
                # Terms and conditions
                ft.Container(
                    content=ft.Text(
                        "بالضغط على إنشاء حساب، فإنك توافق على شروط الاستخدام وسياسة الخصوصية",
                        size=12,
                        color=ft.colors.GREY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    margin=ft.margin.only(bottom=20),
                    padding=ft.padding.symmetric(horizontal=20),
                ),
            ],
        )
    
    def handle_signup(self, e):
        if self.loading:
            return
        
        name = self.name_field.value
        email = self.email_field.value
        phone = self.phone_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value
        
        # Validate inputs
        if not name or not email or not phone or not password:
            self.show_error("يرجى ملء جميع الحقول المطلوبة")
            return
        
        if password != confirm_password:
            self.show_error("كلمات المرور غير متطابقة")
            return
        
        if len(password) < 6:
            self.show_error("كلمة المرور يجب أن تكون 6 أحرف على الأقل")
            return
        
        self.loading = True
        self.page.update()
        
        # Simulate API call with a slight delay
        self.page.splash = ft.ProgressBar()
        self.page.update()
        
        # In a real app, this would register the user with a backend API
        # For this demo, we'll simulate success and redirect
        # Simulate API response delay
        import asyncio
        
        async def simulate_api_call():
            await asyncio.sleep(1)
            
            # Auto-login the new user
            self.app_state.login({
                "user_id": "new_user",
                "name": name,
                "email": email,
                "phone": phone,
                "addresses": []
            })
            
            self.router.go("/menu")
            
            self.loading = False
            self.page.splash = None
            self.page.update()
        
        asyncio.create_task(simulate_api_call())
    
    def show_error(self, message):
        self.error_text.value = message
        self.error_text.visible = True
        self.page.update()
