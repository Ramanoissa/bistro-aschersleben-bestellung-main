import flet as ft

def checkout_screen(page: ft.Page):
    delivery_method = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="delivery", label="Lieferung"),
            ft.Radio(value="pickup", label="Abholung")
        ]),
        value="delivery"
    )
    address = ft.TextField(label="Lieferadresse", width=300)
    payment_method = ft.Dropdown(
        label="Zahlungsmethode",
        options=[
            ft.DropdownOption("PayPal"),
            ft.DropdownOption("Kreditkarte"),
            ft.DropdownOption("Apple Pay"),
            ft.DropdownOption("Barzahlung bei Lieferung")
        ],
        value="PayPal"
    )
    def pay(e):
        page.snack_bar = ft.SnackBar(content=ft.Text("Bezahlung erfolgreich!"))
        page.snack_bar.open = True
        page.update()
    return ft.Column([
        ft.Text("Checkout", size=30, weight="bold"),
        ft.Divider(),
        ft.Text("Lieferoption wählen:"),
        delivery_method,
        address,
        ft.Text("Zahlungsmethode wählen:"),
        payment_method,
        ft.ElevatedButton("Jetzt bezahlen", icon=ft.Icons.PAYMENT, on_click=pay)
    ], spacing=20, scroll=ft.ScrollMode.AUTO)
