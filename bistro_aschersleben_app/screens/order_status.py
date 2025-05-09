import flet as ft

def order_status_screen(page: ft.Page, order_id="12345", status="in_progress"):
    # Status kann sein: in_progress, on_the_way, delivered
    status_map = {
        "in_progress": ("In Zubereitung", 0.33),
        "on_the_way": ("Unterwegs", 0.66),
        "delivered": ("Geliefert", 1.0)
    }
    status_text, progress = status_map.get(status, ("Unbekannt", 0))
    return ft.Column([
        ft.Text(f"Bestellstatus #{order_id}", size=30, weight="bold"),
        ft.Divider(),
        ft.Text(f"Status: {status_text}", size=20),
        ft.ProgressBar(value=progress, width=300),
        ft.Text("Erwartete Lieferzeit: 30-45 Minuten", size=16),
        ft.ElevatedButton("Zurück zur Startseite", icon=ft.Icons.HOME, on_click=lambda e: page.show_screen("home"))
    ], spacing=20, scroll=ft.ScrollMode.AUTO)
