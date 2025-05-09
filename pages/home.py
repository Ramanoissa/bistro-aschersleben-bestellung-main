import flet as ft

def HomePage(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("Willkommen bei Bistro Aschersleben!", size=30, weight="bold"),
            ft.Text("Ihr Lieblingsrestaurant in Aschersleben", size=16),
            ft.Divider(),
            ft.Text("Unsere Spezialitäten", size=20, weight="bold"),
            ft.Row(
                controls=[
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Image(src="https://images.unsplash.com/photo-1513104890138-7c749659a591", width=150, height=150, fit=ft.ImageFit.COVER),
                                ft.Text("Pizza Margherita", size=16, weight="bold"),
                                ft.Text("8,50 €", color="green"),
                                ft.ElevatedButton("Bestellen", on_click=lambda e: page.go("/menu"))
                            ]),
                            padding=10
                        )
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Image(src="https://images.unsplash.com/photo-1550547660-d9450f859349", width=150, height=150, fit=ft.ImageFit.COVER),
                                ft.Text("Cheeseburger", size=16, weight="bold"),
                                ft.Text("7,50 €", color="green"),
                                ft.ElevatedButton("Bestellen", on_click=lambda e: page.go("/menu"))
                            ]),
                            padding=10
                        )
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            ft.Divider(),
            ft.Text("Öffnungszeiten", size=20, weight="bold"),
            ft.Text("Montag - Freitag: 11:00 - 22:00"),
            ft.Text("Samstag - Sonntag: 12:00 - 23:00"),
            ft.Divider(),
            ft.ElevatedButton(
                "Jetzt bestellen",
                icon=ft.Icons.SHOPPING_CART,
                on_click=lambda e: page.go("/menu")
            )
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    ) 