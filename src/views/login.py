
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, primary_button_style
from utils.data_provider import DataProvider

class LoginView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # Form fields
        self.email_field = ft.TextField(
            label="البريد الإلكتروني",
            keyboard_type=ft.KeyboardType.EMAIL,
            autofocus=True,
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
                            ft.Text("تسجيل الدخول", style=text_style_heading(size=20)),
                            ft.Container(width=40),  # Spacer for alignment
                        ]
                    ),
                    margin=ft.margin.only(top=20, left=10, right=10),
                ),
                
                # Logo
                ft.Container(
                    content=ft.Image(
                        src="/assets/logo.png",  # Will need a logo image
                        width=120,
                        height=120,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    margin=ft.margin.only(top=20, bottom=20),
                ),
                
                # Form
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                self.email_field,
                                self.password_field,
                                self.error_text,
                                ft.ElevatedButton(
                                    text="تسجيل الدخول",
                                    style=primary_button_style(),
                                    on_click=self.handle_login,
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
                
                # Forgot password link
                ft.TextButton(
                    "نسيت كلمة المرور؟",
                    on_click=self.handle_forgot_password,
                ),
                
                # Sign up link
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Text("ليس لديك حساب؟"),
                        ft.TextButton(
                            "إنشاء حساب جديد",
                            on_click=lambda _: self.router.go("/signup"),
                        ),
                    ]
                ),
                
                # Demo credentials info
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text("بيانات تجريبية للاختبار:", size=14, color=ft.colors.GREY),
                            ft.Text("البريد: test@example.com", size=14, color=ft.colors.GREY),
                            ft.Text("كلمة المرور: password", size=14, color=ft.colors.GREY),
                        ],
                    ),
                    margin=ft.margin.only(top=30),
                ),
            ],
        )
    
    def handle_login(self, e):
        if self.loading:
            return
        
        email = self.email_field.value
        password = self.password_field.value
        
        if not email or not password:
            self.show_error("يرجى إدخال البريد الإلكتروني وكلمة المرور")
            return
        
        self.loading = True
        self.page.update()
        
        # Simulate API call with a slight delay
        self.page.splash = ft.ProgressBar()
        self.page.update()
        
        # In a real app, this would be an API call
        login_result = DataProvider.mock_login(email, password)
        
        if login_result["success"]:
            self.app_state.login(login_result["user_data"])
            self.router.go("/menu")
        else:
            self.show_error(login_result["message"])
        
        self.loading = False
        self.page.splash = None
        self.page.update()
    
    def show_error(self, message):
        self.error_text.value = message
        self.error_text.visible = True
        self.page.update()
    
    def handle_forgot_password(self, e):
        # In a real app, this would navigate to password reset
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("سيتم إرسال رابط إعادة تعيين كلمة المرور إلى بريدك الإلكتروني"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
