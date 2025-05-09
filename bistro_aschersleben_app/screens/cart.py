import flet as ft

cart_items = []

def cart_screen(page: ft.Page):
    def update_cart():
        cart_content.controls = create_cart_items()
        page.update()

    def create_cart_items():
        if not cart_items:
            return [ft.Text("Ihr Warenkorb ist leer", size=20)]
        items = []
        total = 0
        for item in cart_items:
            total += item["price"]
            items.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Row([
                            ft.Image(src=item["image"], width=80, height=80, fit=ft.ImageFit.COVER),
                            ft.Column([
                                ft.Text(item["name"], size=16, weight="bold"),
                                ft.Text(f"{item['price']} €", color="green"),
                                ft.Row([
                                    ft.IconButton(
                                        icon=ft.Icons.REMOVE,
                                        on_click=lambda e, i=item: remove_from_cart(i)
                                    ),
                                    ft.Text("1"),
                                    ft.IconButton(
                                        icon=ft.Icons.ADD,
                                        on_click=lambda e, i=item: add_to_cart(i)
                                    )
                                ])
                            ])
                        ]),
                        padding=10
                    )
                )
            )
        items.extend([
            ft.Divider(),
            ft.Row([
                ft.Text("Gesamt:", size=20, weight="bold"),
                ft.Text(f"{total:.2f} €", size=20, color="green", weight="bold")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.ElevatedButton(
                "Zur Kasse",
                icon=ft.Icons.PAYMENT,
                on_click=lambda e: page.show_screen("checkout")
            )
        ])
        return items

    def add_to_cart(item):
        cart_items.append(item)
        update_cart()
        page.snack_bar = ft.SnackBar(content=ft.Text(f"{item['name']} wurde zum Warenkorb hinzugefügt!"))
        page.snack_bar.open = True
        page.update()

    def remove_from_cart(item):
        if item in cart_items:
            cart_items.remove(item)
            update_cart()
            page.snack_bar = ft.SnackBar(content=ft.Text(f"{item['name']} wurde aus dem Warenkorb entfernt!"))
            page.snack_bar.open = True
            page.update()

    cart_content = ft.Column(
        controls=create_cart_items(),
        spacing=10,
        scroll=ft.ScrollMode.AUTO
    )

    return ft.Column(
        controls=[
            ft.Text("Ihr Warenkorb", size=30, weight="bold"),
            ft.Divider(),
            cart_content
        ],
        spacing=20
    )
