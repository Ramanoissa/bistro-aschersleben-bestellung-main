import flet as ft

def home_screen(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Text("Willkommen bei", size=24, color="#666666"),
                    ft.Text("Bistro Aschersleben", size=32, weight="bold", color="#333333"),
                    ft.Text("Ihr Lieblingsrestaurant in Aschersleben", size=16, color="#666666"),
                ]),
                padding=ft.Margin(0, 0, 0, 20)  # left, top, right, bottom
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Unsere Spezialitäten", size=24, weight="bold", color="#333333"),
                    ft.Row(
                        controls=[
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.Container(
                                            content=ft.Image(
                                                src="https://images.unsplash.com/photo-1513104890138-7c749659a591",
                                                width=150,
                                                height=150,
                                                fit=ft.ImageFit.COVER,
                                            ),
                                            border_radius=10,
                                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        ),
                                        ft.Container(
                                            content=ft.Column([
                                                ft.Text("Pizza Margherita", size=18, weight="bold", color="#333333"),
                                                ft.Text("8,50 €", color="#FF4B2B", size=16, weight="bold"),
                                                ft.ElevatedButton(
                                                    "Bestellen",
                                                    style=ft.ButtonStyle(
                                                        color="#FFFFFF",
                                                        bgcolor="#FF4B2B",
                                                        shape=ft.RoundedRectangleBorder(radius=10),
                                                    ),
                                                    on_click=lambda e: page.show_screen("menu")
                                                )
                                            ], spacing=10),
                                            padding=10
                                        )
                                    ]),
                                ),
                                elevation=5,
                                margin=5
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.Container(
                                            content=ft.Image(
                                                src="https://images.unsplash.com/photo-1550547660-d9450f859349",
                                                width=150,
                                                height=150,
                                                fit=ft.ImageFit.COVER,
                                            ),
                                            border_radius=10,
                                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        ),
                                        ft.Container(
                                            content=ft.Column([
                                                ft.Text("Cheeseburger", size=18, weight="bold", color="#333333"),
                                                ft.Text("7,50 €", color="#FF4B2B", size=16, weight="bold"),
                                                ft.ElevatedButton(
                                                    "Bestellen",
                                                    style=ft.ButtonStyle(
                                                        color="#FFFFFF",
                                                        bgcolor="#FF4B2B",
                                                        shape=ft.RoundedRectangleBorder(radius=10),
                                                    ),
                                                    on_click=lambda e: page.show_screen("menu")
                                                )
                                            ], spacing=10),
                                            padding=10
                                        )
                                    ]),
                                ),
                                elevation=5,
                                margin=5
                            )
                        ],
                        scroll=ft.ScrollMode.AUTO
                    ),
                ]),
                padding=ft.Margin(0, 0, 0, 20)  # left, top, right, bottom
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Öffnungszeiten", size=24, weight="bold", color="#333333"),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Montag - Freitag: 11:00 - 22:00", size=16, color="#666666"),
                            ft.Text("Samstag - Sonntag: 12:00 - 23:00", size=16, color="#666666"),
                        ]),
                        padding=10,
                        bgcolor="#f8f8f8",
                        border_radius=10
                    )
                ]),
                padding=ft.Margin(0, 0, 0, 20)  # left, top, right, bottom
            ),
            ft.ElevatedButton(
                "Jetzt bestellen",
                icon=ft.Icons.SHOPPING_CART,
                style=ft.ButtonStyle(
                    color="#FFFFFF",
                    bgcolor="#FF4B2B",
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                on_click=lambda e: page.show_screen("menu")
            )
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )
