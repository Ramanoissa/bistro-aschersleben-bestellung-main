import flet as ft
from services.menu_data import menu_data
from services.favorites import favorites

def product_detail_screen(page: ft.Page, product_id):
    # Produkt suchen
    product = None
    for category in menu_data:
        for item in category["products"]:
            if item["id"] == product_id:
                product = item
                break
    if not product:
        return ft.Text("Produkt nicht gefunden.")

    # Preis-Handling
    if isinstance(product["price"], dict):
        price_str = " / ".join([f"{size}: {price}€" for size, price in product["price"].items()])
    else:
        price_str = f"{product['price']} €"

    # Bild
    image_url = product.get("image") or "https://placehold.co/300x200?text=Kein+Bild"

    # Extras, Allergene, Zusatzstoffe
    extras = product.get("extras")
    allergens = ", ".join(product.get("allergens", []))
    zusatzstoffe = ", ".join(product.get("zusatzstoffe", []))

    # Extras auswählbar (Checkboxen)
    extras_options = []
    if extras:
        extras_options = [e.strip() for e in extras.split(",")]
    selected_extras = {e: ft.Ref[ft.Checkbox]() for e in extras_options}

    # Mengenwahl
    quantity = ft.Ref[ft.Text]()
    qty = {"value": 1}
    def inc(e):
        qty["value"] += 1
        quantity.current.value = str(qty["value"])
        page.update()
    def dec(e):
        if qty["value"] > 1:
            qty["value"] -= 1
            quantity.current.value = str(qty["value"])
            page.update()

    # Favoriten-Feature
    is_fav = product_id in favorites
    def toggle_fav(e):
        if product_id in favorites:
            favorites.remove(product_id)
        else:
            favorites.add(product_id)
        page.update()

    def add_to_cart(e):
        chosen_extras = [ex for ex, ref in selected_extras.items() if ref.current.value]
        msg = f"{product['name']} x{qty['value']}" + (f" mit {', '.join(chosen_extras)}" if chosen_extras else "")
        page.snack_bar = ft.SnackBar(content=ft.Text(msg + " zum Warenkorb hinzugefügt!"))
        page.snack_bar.open = True
        page.update()

    return ft.Column([
        ft.Row([
            ft.Image(src=image_url, width=300, height=200, fit=ft.ImageFit.COVER),
            ft.IconButton(
                icon=ft.Icons.FAVORITE if is_fav else ft.Icons.FAVORITE_BORDER,
                icon_color="red" if is_fav else "grey",
                tooltip="Als Favorit markieren",
                on_click=toggle_fav,
                style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=30)})
            )
        ], alignment=ft.MainAxisAlignment.START),
        ft.Text(product["name"], size=28, weight="bold"),
        ft.Text(product["description"], size=18),
        ft.Text(price_str, color="green", size=22, weight="bold"),
        ft.Divider(),
        ft.Text("Extras wählen:" if extras_options else "", size=16),
        ft.Row([
            *[ft.Checkbox(label=ex, ref=selected_extras[ex]) for ex in extras_options]
        ], spacing=10),
        ft.Text(f"Allergene: {allergens}" if allergens else "", size=14, color="red"),
        ft.Text(f"Zusatzstoffe: {zusatzstoffe}" if zusatzstoffe else "", size=14, color="orange"),
        ft.Divider(),
        ft.Row([
            ft.Text("Menge:", size=16),
            ft.IconButton(ft.Icons.REMOVE, on_click=dec),
            ft.Text(str(qty["value"]), ref=quantity, size=18, weight="bold"),
            ft.IconButton(ft.Icons.ADD, on_click=inc),
        ], spacing=5),
        ft.ElevatedButton("In den Warenkorb", icon=ft.Icons.ADD_SHOPPING_CART, on_click=add_to_cart),
        ft.ElevatedButton("Zurück zur Speisekarte", icon=ft.Icons.ARROW_BACK, on_click=lambda e: page.show_screen("menu")),
    ], spacing=16, scroll=ft.ScrollMode.AUTO) 