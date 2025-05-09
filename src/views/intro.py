
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body

class IntroView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        self.alignment = ft.alignment.center
        self.bgcolor = BISTRO_PRIMARY
        
        self.content = self.build()
    
    def build(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                # Logo
                ft.Container(
                    content=ft.Image(
                        src="/assets/logo.png",  # Will need a logo image
                        width=200,
                        height=200,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    border_radius=100,
                    bgcolor=ft.colors.WHITE,
                    width=200,
                    height=200,
                    alignment=ft.alignment.center,
                ),
                
                # Restaurant name
                ft.Text(
                    "بسترو اشرسلیبن",
                    style=text_style_heading(size=32, color=ft.colors.WHITE),
                    text_align=ft.TextAlign.CENTER,
                ),
                
                # Tagline
                ft.Text(
                    "مطعم للمأكولات السريعة الشهية",
                    style=text_style_body(size=18, color=ft.colors.WHITE),
                    text_align=ft.TextAlign.CENTER,
                ),
                
                # Spacer
                ft.Container(height=40),
                
                # Start buttons
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                    controls=[
                        ft.ElevatedButton(
                            "تصفح القائمة",
                            icon=ft.icons.MENU_BOOK,
                            on_click=lambda _: self.router.go("/menu"),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.WHITE,
                                color=BISTRO_PRIMARY,
                                elevation=4,
                                padding=ft.padding.symmetric(vertical=20, horizontal=30),
                                shape=ft.RoundedRectangleBorder(radius=30),
                            ),
                            width=280,
                        ),
                        
                        ft.ElevatedButton(
                            "تسجيل الدخول",
                            icon=ft.icons.LOGIN,
                            on_click=lambda _: self.router.go("/login"),
                            style=ft.ButtonStyle(
                                bgcolor=BISTRO_SECONDARY, 
                                color=ft.colors.WHITE,
                                elevation=4,
                                padding=ft.padding.symmetric(vertical=20, horizontal=30),
                                shape=ft.RoundedRectangleBorder(radius=30),
                            ),
                            width=280,
                        ),
                        
                        ft.TextButton(
                            "إنشاء حساب جديد",
                            on_click=lambda _: self.router.go("/signup"),
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                            ),
                        ),
                    ],
                ),
            ],
        )
