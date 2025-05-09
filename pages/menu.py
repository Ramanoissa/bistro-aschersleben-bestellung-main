import flet as ft

# Beispiel-Menüdaten
MENU_DATA = {
    "Pizza": [
        {"name": "Margherita", "price": 8.50, "description": "Tomatensoße, Mozzarella, Basilikum", "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591"},
        {"name": "Salami", "price": 9.50, "description": "Tomatensoße, Mozzarella, Salami", "image": "https://images.unsplash.com/photo-1548365328-8b849e6c7b8b"},
        {"name": "Hawaii", "price": 10.50, "description": "Tomatensoße, Mozzarella, Schinken, Ananas", "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836"},
    ],
    "Burger": [
        {"name": "Cheeseburger", "price": 7.50, "description": "Rindfleisch, Käse, Salat, Tomate, Zwiebel", "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"},
        {"name": "Chicken Burger", "price": 7.00, "description": "Hähnchen, Salat, Tomate, Zwiebel", "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"},
    ],
    "Getränke": [
        {"name": "Cola", "price": 2.50, "description": "0,5L", "image": "https://images.unsplash.com/photo-1502741338009-cac2772e18bc"},
        {"name": "Fanta", "price": 2.50, "description": "0,5L", "image": "https://images.unsplash.com/photo-1519864600265-abb23847ef2c"},
    ]
}

def MenuPage(page: ft.Page):
    def create_menu_item(item):
        return ft.Card(
            content=ft.Container(
                content=ft.Row([
                    ft.Image(src=item["image"], width=100, height=100, fit=ft.ImageFit.COVER),
                    ft.Column([
                        ft.Text(item["name"], size=16, weight="bold"),
                        ft.Text(item["description"], size=14),
                        ft.Text(f"{item['price']} €", color="green", size=16),
                        ft.ElevatedButton(
                            "In den Warenkorb",
                            icon=ft.Icons.ADD_SHOPPING_CART,
                            on_click=lambda e: add_to_cart(item)
                        )
                    ], spacing=5)
                ]),
                padding=10
            )
        )

    def add_to_cart(item):
        # TODO: Implementiere Warenkorb-Funktionalität
        page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{item['name']} wurde zum Warenkorb hinzugefügt!")))

    # Erstelle die Menüseite
    menu_content = []
    for category, items in MENU_DATA.items():
        menu_content.extend([
            ft.Text(category, size=24, weight="bold"),
            ft.Divider(),
            *[create_menu_item(item) for item in items],
            ft.Divider(),
        ])

    return ft.Column(
        controls=[
            ft.Text("Unsere Speisekarte", size=30, weight="bold"),
            ft.Text("Wählen Sie aus unseren leckeren Gerichten", size=16),
            ft.Divider(),
            *menu_content
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    ) 