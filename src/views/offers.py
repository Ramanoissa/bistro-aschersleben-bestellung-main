
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body
from utils.data_provider import DataProvider

class OffersView(ft.Container):
    def __init__(self, page, router, app_state):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.expand = True
        
        # Get offers data
        self.offers = DataProvider.get_offers()
        
        self.content = self.build()
    
    def build(self):
        # Create offers list
        offers_list = ft.Column(
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        )
        
        if self.offers:
            for offer in self.offers:
                offers_list.controls.append(self.build_offer_card(offer))
                
            # Add some promotional content at the end
            offers_list.controls.extend([
                ft.Divider(),
                ft.Container(
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Text(
                                "احصل على العروض الحصرية",
                                style=text_style_heading(size=18),
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "انضم إلى نشرتنا البريدية للحصول على أحدث العروض والكوبونات",
                                style=text_style_body(size=14),
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(
                                        hint_text="أدخل بريدك الإلكتروني",
                                        width=250,
                                        border_radius=30,
                                        text_align=ft.TextAlign.RIGHT,
                                        text_direction=ft.TextDirection.RTL,
                                    ),
                                ],
                            ),
                            ft.ElevatedButton(
                                "اشترك الآن",
                                style=ft.ButtonStyle(
                                    bgcolor=BISTRO_SECONDARY,
                                    color=ft.colors.WHITE,
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                ),
                                width=200,
                                on_click=self.subscribe_newsletter,
                            ),
                        ],
                    ),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.GREY_50,
                ),
            ])
        else:
            # No offers available
            offers_list.controls.append(
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.Icon(
                                name=ft.icons.LOCAL_OFFER_OUTLINED,
                                size=80,
                                color=ft.colors.GREY_400,
                            ),
                            ft.Text(
                                "لا توجد عروض حالياً",
                                style=text_style_heading(size=20),
                            ),
                            ft.Text(
                                "تحقق مرة أخرى قريباً للحصول على عروض رائعة",
                                style=text_style_body(size=16, color=ft.colors.GREY),
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
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
                                icon=ft.icons.NOTIFICATIONS,
                                tooltip="الإشعارات",
                                on_click=self.show_notifications,
                            ),
                            ft.Text(
                                "العروض والكوبونات",
                                style=text_style_heading(size=20),
                            ),
                            ft.IconButton(
                                icon=ft.icons.REFRESH,
                                tooltip="تحديث",
                                on_click=lambda _: self.refresh_offers(),
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Content
                ft.Container(
                    content=offers_list,
                    padding=ft.padding.all(15),
                    expand=True,
                ),
            ],
        )
    
    def build_offer_card(self, offer):
        # Calculate discount percentage
        if "original_price" in offer and offer["original_price"] > 0:
            discount_percent = int(100 - (offer["price"] / offer["original_price"] * 100))
        else:
            discount_percent = 0
        
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    spacing=10,
                    controls=[
                        # Offer image with discount badge
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src=f"/assets/offers/{offer['image']}",
                                        width=float("inf"),
                                        height=150,
                                        fit=ft.ImageFit.COVER,
                                        border_radius=ft.border_radius.only(
                                            top_left=8, top_right=8
                                        ),
                                    ),
                                    width=float("inf"),
                                    height=150,
                                    border_radius=ft.border_radius.only(
                                        top_left=8, top_right=8
                                    ),
                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                ),
                                # Discount badge
                                ft.Container(
                                    content=ft.Text(
                                        f"خصم {discount_percent}%",
                                        color=ft.colors.WHITE,
                                        weight=ft.FontWeight.BOLD,
                                        size=14,
                                    ),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    border_radius=ft.border_radius.only(
                                        bottom_right=10, top_left=8
                                    ),
                                    bgcolor=BISTRO_PRIMARY,
                                ),
                            ],
                        ),
                        
                        # Offer details
                        ft.Container(
                            content=ft.Column(
                                spacing=5,
                                controls=[
                                    ft.Text(
                                        offer["title"],
                                        style=text_style_heading(size=18),
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                    ft.Text(
                                        offer["description"],
                                        style=text_style_body(size=14),
                                        text_align=ft.TextAlign.RIGHT,
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Text(
                                                f"تنتهي في: {offer['expires_at']}",
                                                style=text_style_body(size=12, color=ft.colors.GREY),
                                            ),
                                            ft.Row(
                                                spacing=5,
                                                controls=[
                                                    ft.Text(
                                                        f"{offer['price']:.2f} €",
                                                        style=text_style_body(
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD,
                                                            color=BISTRO_PRIMARY,
                                                        ),
                                                    ),
                                                    ft.Text(
                                                        f"{offer['original_price']:.2f} €",
                                                        style=text_style_body(
                                                            size=14,
                                                            color=ft.colors.GREY,
                                                            decoration=ft.TextDecoration.LINE_THROUGH,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    ft.ElevatedButton(
                                        "اطلب الآن",
                                        icon=ft.icons.SHOPPING_CART,
                                        style=ft.ButtonStyle(
                                            bgcolor=BISTRO_PRIMARY,
                                            color=ft.colors.WHITE,
                                        ),
                                        width=float("inf"),
                                        on_click=lambda _, offer_id=offer["id"]: self.order_offer(offer_id),
                                    ),
                                ],
                            ),
                            padding=ft.padding.all(10),
                        ),
                    ],
                ),
                border_radius=8,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            ),
            elevation=2,
        )
    
    def order_offer(self, offer_id):
        # In a real app, this would add the offer to the cart
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"تمت إضافة العرض إلى السلة"),
            action="عرض السلة",
            on_action=lambda _: self.router.go("/cart")
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def subscribe_newsletter(self, e):
        # In a real app, this would subscribe the user to the newsletter
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("تم الاشتراك بنجاح في النشرة البريدية"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def show_notifications(self, e):
        # In a real app, this would show notifications
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("لا توجد إشعارات جديدة"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def refresh_offers(self):
        # In a real app, this would refresh offers from the server
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("تم تحديث العروض"),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
