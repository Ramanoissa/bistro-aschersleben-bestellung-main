import flet as ft
from services.menu_data import menu_data
from screens.product_detail import product_detail_screen
from services.favorites import favorites

# Favoriten werden jetzt zentral in services.favorites gehalten

def menu_screen(page: ft.Page):
    categories = [cat["category"] for cat in menu_data]
    selected_category = ft.Dropdown(
        label="Kategorie filtern",
        options=[ft.DropdownOption(cat) for cat in categories],
        value=None,
        on_change=lambda e: page.update(),
        width=300,
        border_color="#FF4B2B",
        focused_border_color="#FF4B2B",
        color="#333333"
    )
    
    search = ft.TextField(
        label="Suche...",
        width=300,
        on_change=lambda e: page.update(),
        border_color="#FF4B2B",
        focused_border_color="#FF4B2B",
        color="#333333"
    )
    
    show_favs = ft.Checkbox(
        label="Nur Favoriten anzeigen",
        value=False,
        on_change=lambda e: page.update(),
        fill_color="#FF4B2B"
    )

    def show_product_detail(product_id):
        page.clean()
        page.add(product_detail_screen(page, product_id))

    def toggle_fav(item_id):
        if item_id in favorites:
            favorites.remove(item_id)
        else:
            favorites.add(item_id)
        page.update()

    def create_menu_item(item):
        if isinstance(item["price"], dict):
            price_str = " / ".join([f"{size}: {price}€" for size, price in item["price"].items()])
        else:
            price_str = f"{item['price']} €"
            
        image_url = item.get("image") or "https://images.unsplash.com/photo-1513104890138-7c749659a591"
        is_fav = item["id"] in favorites
        
        return ft.Card(
            content=ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Image(
                            src=image_url,
                            width=100,
                            height=100,
                            fit=ft.ImageFit.COVER,
                        ),
                        border_radius=10,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text(item["name"], size=18, weight="bold", color="#333333"),
                                ft.IconButton(
                                    icon=ft.Icons.FAVORITE if is_fav else ft.Icons.FAVORITE_BORDER,
                                    icon_color="#FF4B2B" if is_fav else "#666666",
                                    tooltip="Als Favorit markieren",
                                    on_click=lambda e, pid=item["id"]: toggle_fav(pid)
                                )
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Text(item["description"], size=14, color="#666666"),
                            ft.Text(price_str, color="#FF4B2B", size=16, weight="bold"),
                            ft.Row([
                                ft.ElevatedButton(
                                    "Details",
                                    icon=ft.Icons.INFO,
                                    style=ft.ButtonStyle(
                                        color="#FFFFFF",
                                        bgcolor="#FF4B2B",
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=lambda e, pid=item["id"]: show_product_detail(pid)
                                ),
                                ft.ElevatedButton(
                                    "In den Warenkorb",
                                    icon=ft.Icons.ADD_SHOPPING_CART,
                                    style=ft.ButtonStyle(
                                        color="#FFFFFF",
                                        bgcolor="#FF4B2B",
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=lambda e: add_to_cart(item)
                                )
                            ], spacing=10)
                        ], spacing=5),
                        padding=10,
                        expand=True
                    )
                ]),
                padding=10
            ),
            elevation=5,
            margin=5
        )

    def add_to_cart(item):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{item['name']} wurde zum Warenkorb hinzugefügt!"),
            bgcolor="#FF4B2B"
        )
        page.snack_bar.open = True
        page.update()

    def get_filtered_menu():
        q = search.value.lower() if search.value else ""
        cat = selected_category.value
        only_favs = show_favs.value
        filtered = []
        for category in menu_data:
            if cat and category["category"] != cat:
                continue
            filtered_products = [item for item in category["products"] if (q in item["name"].lower() or q in item["description"].lower()) and (not only_favs or item["id"] in favorites)]
            if filtered_products:
                filtered.append({"category": category["category"], "products": filtered_products})
        return filtered

    def build_menu_content():
        content = []
        for category in get_filtered_menu():
            content.extend([
                ft.Container(
                    content=ft.Text(category["category"], size=24, weight="bold", color="#333333"),
                    padding=ft.Margin(0, 0, 0, 10)
                ),
                ft.Divider(color="#FF4B2B"),
                *[create_menu_item(item) for item in category["products"]],
                ft.Divider(color="#FF4B2B"),
            ])
        return content

    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Text("Unsere Speisekarte", size=32, weight="bold", color="#333333"),
                    ft.Text("Wählen Sie aus unseren leckeren Gerichten", size=16, color="#666666"),
                ]),
                padding=ft.Margin(0, 0, 0, 20)
            ),
            ft.Container(
                content=ft.Column([
                    selected_category,
                    search,
                    show_favs,
                ], spacing=10),
                padding=ft.Margin(0, 0, 0, 20)
            ),
            ft.Column(build_menu_content(), spacing=20, scroll=ft.ScrollMode.AUTO)
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )
