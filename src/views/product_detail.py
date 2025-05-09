
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body, primary_button_style
from utils.data_provider import DataProvider

class ProductDetailView(ft.Container):
    def __init__(self, page, router, app_state, product_id):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.product_id = product_id
        self.expand = True
        
        # Get product data
        self.product = DataProvider.get_menu_item(product_id)
        if not self.product:
            self.content = ft.Text("المنتج غير موجود!")
            return
        
        # State
        self.quantity = 1
        self.selected_options = {}
        self.notes = ""
        
        # Initialize default selections for required options
        for option in self.product["options"]:
            if option["required"] and not option["multiple"]:
                self.selected_options[option["name"]] = option["choices"][0]
        
        self.content = self.build()
    
    def build(self):
        if not self.product:
            return ft.Text("المنتج غير موجود!")
        
        # Create options UI
        options_controls = []
        for option in self.product["options"]:
            option_ui = self.build_option_ui(option)
            options_controls.append(option_ui)
        
        # Notes field
        notes_field = ft.TextField(
            label="ملاحظات إضافية",
            hint_text="مثال: بدون بصل، إلخ",
            multiline=True,
            min_lines=1,
            max_lines=3,
            text_align=ft.TextAlign.RIGHT,
            text_direction=ft.TextDirection.RTL,
            on_change=self.update_notes,
        )
        
        # Total price calculation
        base_price = self.product["price"]
        options_price = 0
        for option_name, selected_choice in self.selected_options.items():
            if selected_choice:
                options_price += selected_choice.get("price", 0)
        
        item_total_price = (base_price + options_price) * self.quantity
        
        return ft.Column(
            spacing=0,
            controls=[
                # Top bar
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda _: self.router.go("/menu"),
                            ),
                            ft.Text(
                                self.product["name"],
                                style=text_style_heading(size=20),
                            ),
                            ft.Container(width=40),  # Spacer for alignment
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Product content - scrollable
                ft.Container(
                    content=ft.Column(
                        spacing=20,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            # Product image
                            ft.Container(
                                content=ft.Image(
                                    src=f"/assets/menu/{self.product['image']}",
                                    width=float("inf"),
                                    height=200,
                                    fit=ft.ImageFit.COVER,
                                    border_radius=8,
                                ),
                                width=float("inf"),
                                height=200,
                                border_radius=8,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            ),
                            
                            # Product info
                            ft.Container(
                                content=ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(
                                            self.product["name"],
                                            style=text_style_heading(size=24),
                                            text_align=ft.TextAlign.RIGHT,
                                        ),
                                        ft.Text(
                                            self.product["description"],
                                            style=text_style_body(size=16, color=ft.colors.GREY_800),
                                            text_align=ft.TextAlign.RIGHT,
                                        ),
                                        ft.Text(
                                            f"{self.product['price']} €",
                                            style=text_style_body(
                                                size=20,
                                                weight=ft.FontWeight.BOLD,
                                                color=BISTRO_PRIMARY,
                                            ),
                                            text_align=ft.TextAlign.RIGHT,
                                        ),
                                    ],
                                ),
                                padding=ft.padding.symmetric(horizontal=15),
                            ),
                            
                            # Divider
                            ft.Divider(),
                            
                            # Options
                            ft.Container(
                                content=ft.Column(
                                    spacing=20,
                                    controls=options_controls,
                                ),
                                padding=ft.padding.symmetric(horizontal=15),
                            ),
                            
                            # Notes
                            ft.Container(
                                content=notes_field,
                                padding=ft.padding.symmetric(horizontal=15),
                            ),
                            
                            # Quantity selector
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=10,
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.REMOVE_CIRCLE,
                                            icon_color=BISTRO_PRIMARY,
                                            on_click=self.decrease_quantity,
                                            disabled=self.quantity <= 1,
                                        ),
                                        ft.Text(
                                            str(self.quantity),
                                            style=text_style_body(size=18, weight=ft.FontWeight.BOLD),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.ADD_CIRCLE,
                                            icon_color=BISTRO_PRIMARY,
                                            on_click=self.increase_quantity,
                                        ),
                                    ],
                                ),
                                padding=ft.padding.only(top=10, bottom=20),
                            ),
                            
                            # Spacer to ensure bottom bar does not cover content
                            ft.Container(height=70),
                        ],
                    ),
                    expand=True,
                ),
                
                # Bottom bar with price and add to cart button
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text(
                                        "الإجمالي",
                                        style=text_style_body(size=14),
                                    ),
                                    ft.Text(
                                        f"{item_total_price:.2f} €",
                                        style=text_style_body(
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=BISTRO_PRIMARY,
                                        ),
                                    ),
                                ],
                            ),
                            ft.ElevatedButton(
                                text="إضافة إلى السلة",
                                style=primary_button_style(),
                                on_click=self.add_to_cart,
                            ),
                        ],
                    ),
                    padding=ft.padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.only(top=ft.border.BorderSide(1, ft.colors.GREY_300)),
                ),
            ],
        )
    
    def build_option_ui(self, option):
        option_name = option["name"]
        is_multiple = option["multiple"]
        
        option_container = ft.Container(
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text(
                        f"{option_name} {'(اختياري)' if not option['required'] else ''}",
                        style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                        text_align=ft.TextAlign.RIGHT,
                    ),
                ],
            ),
        )
        
        choices_list = ft.Column(spacing=5)
        
        for choice in option["choices"]:
            choice_name = choice["name"]
            choice_price = choice.get("price", 0)
            
            if is_multiple:
                # Checkbox for multiple selection
                checkbox = ft.Checkbox(
                    label=f"{choice_name} {f'(+{choice_price} €)' if choice_price > 0 else ''}",
                    value=False,
                    on_change=lambda e, name=option_name, choice=choice: self.update_multiple_choice(name, choice, e.control.value),
                )
                choices_list.controls.append(checkbox)
            else:
                # Radio button for single selection
                radio = ft.Radio(
                    value=choice_name,
                    label=f"{choice_name} {f'(+{choice_price} €)' if choice_price > 0 else ''}",
                    on_change=lambda e, name=option_name, choice=choice: self.update_single_choice(name, choice),
                )
                # Check if this is the default selection
                if option["required"] and option_name in self.selected_options and self.selected_options[option_name] == choice:
                    radio.value = True
                
                choices_list.controls.append(radio)
        
        option_container.content.controls.append(choices_list)
        return option_container
    
    def update_single_choice(self, option_name, choice):
        self.selected_options[option_name] = choice
        self.update_ui()
    
    def update_multiple_choice(self, option_name, choice, is_selected):
        if option_name not in self.selected_options:
            self.selected_options[option_name] = []
        
        if is_selected:
            if choice not in self.selected_options[option_name]:
                self.selected_options[option_name].append(choice)
        else:
            if choice in self.selected_options[option_name]:
                self.selected_options[option_name].remove(choice)
        
        self.update_ui()
    
    def update_notes(self, e):
        self.notes = e.control.value
    
    def increase_quantity(self, e):
        self.quantity += 1
        self.update_ui()
    
    def decrease_quantity(self, e):
        if self.quantity > 1:
            self.quantity -= 1
            self.update_ui()
    
    def update_ui(self):
        self.content = self.build()
        self.page.update()
    
    def add_to_cart(self, e):
        # Validate required options
        for option in self.product["options"]:
            if option["required"] and option["name"] not in self.selected_options:
                self.page.snack_bar = ft.SnackBar(content=ft.Text(f"يرجى اختيار {option['name']}"))
                self.page.snack_bar.open = True
                self.page.update()
                return
        
        # Add to cart
        self.app_state.add_to_cart(
            product_id=self.product["id"],
            name=self.product["name"],
            price=self.product["price"],
            quantity=self.quantity,
            options=self.selected_options,
            notes=self.notes
        )
        
        # Show confirmation
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"تمت إضافة {self.product['name']} إلى السلة"),
            action="عرض السلة",
            on_action=lambda _: self.router.go("/cart")
        )
        self.page.snack_bar.open = True
        self.page.update()
