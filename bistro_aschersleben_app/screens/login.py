import flet as ft

def login_screen(page: ft.Page):
    mode = ft.Ref[ft.Text]()
    email = ft.TextField(label="E-Mail", width=300)
    password = ft.TextField(label="Passwort", password=True, width=300)
    name = ft.TextField(label="Name", width=300)
    address = ft.TextField(label="Adresse", width=300)
    is_register = ft.Ref[ft.Checkbox]()

    def toggle_mode(e):
        if is_register.current.value:
            mode.current.value = "Registrieren"
        else:
            mode.current.value = "Login"
        page.update()

    def submit(e):
        if is_register.current.value:
            page.snack_bar = ft.SnackBar(content=ft.Text(f"Willkommen, {name.value}!"))
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text(f"Willkommen zurück, {email.value}!"))
        page.snack_bar.open = True
        page.update()

    return ft.Column([
        ft.Text(ref=mode, value="Login", size=30, weight="bold"),
        ft.Divider(),
        ft.Checkbox(ref=is_register, label="Ich habe noch kein Konto (Registrieren)", on_change=toggle_mode),
        name,
        email,
        password,
        address,
        ft.ElevatedButton("Absenden", icon=ft.Icons.LOGIN, on_click=submit)
    ], spacing=20, scroll=ft.ScrollMode.AUTO)
