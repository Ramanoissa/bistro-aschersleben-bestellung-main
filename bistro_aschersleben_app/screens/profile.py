import flet as ft

user_data = {
    "name": "Max Mustermann",
    "email": "max@example.com",
    "phone": "+49 123 456789",
    "address": "Musterstraße 123, 06449 Aschersleben"
}

order_history = [
    {
        "order_id": "12345",
        "date": "2024-03-15",
        "items": ["Pizza Margherita", "Cola"],
        "total": 11.00,
        "status": "Abgeschlossen"
    },
    {
        "order_id": "12346",
        "date": "2024-03-14",
        "items": ["Cheeseburger", "Fanta"],
        "total": 10.00,
        "status": "Abgeschlossen"
    }
]

def profile_screen(page: ft.Page):
    def create_order_card(order):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(f"Bestellung #{order['order_id']}", size=16, weight="bold"),
                        ft.Text(order["date"], color="gray")
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(),
                    *[ft.Text(item) for item in order["items"]],
                    ft.Row([
                        ft.Text("Gesamt:", weight="bold"),
                        ft.Text(f"{order['total']} €", color="green")
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text(f"Status: {order['status']}", color="blue")
                ]),
                padding=10
            )
        )

    def show_snackbar(msg):
        page.snack_bar = ft.SnackBar(content=ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    return ft.Column(
        controls=[
            ft.Text("Mein Profil", size=30, weight="bold"),
            ft.Divider(),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Persönliche Daten", size=20, weight="bold"),
                        ft.Text(f"Name: {user_data['name']}"),
                        ft.Text(f"E-Mail: {user_data['email']}"),
                        ft.Text(f"Telefon: {user_data['phone']}"),
                        ft.Text(f"Adresse: {user_data['address']}"),
                        ft.ElevatedButton(
                            "Daten bearbeiten",
                            icon=ft.Icons.EDIT,
                            on_click=lambda e: show_snackbar("Diese Funktion wird noch implementiert!")
                        )
                    ]),
                    padding=10
                )
            ),
            ft.Divider(),
            ft.Text("Bestellhistorie", size=20, weight="bold"),
            *[create_order_card(order) for order in order_history],
            ft.Divider(),
            ft.ElevatedButton(
                "Abmelden",
                icon=ft.Icons.LOGOUT,
                on_click=lambda e: show_snackbar("Diese Funktion wird noch implementiert!")
            )
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )
