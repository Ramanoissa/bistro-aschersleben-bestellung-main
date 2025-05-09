
import flet as ft

# Color definitions
BISTRO_PRIMARY = "#9C3D54"  # Deep red/burgundy - main brand color
BISTRO_SECONDARY = "#E89005"  # Warm yellow/orange - accent color
BISTRO_BACKGROUND = "#FFFBF0"  # Warm off-white
BISTRO_SURFACE = "#FFFFFF"  # Pure white for cards, dialogs
BISTRO_ERROR = "#B00020"  # Standard error color
BISTRO_TEXT_PRIMARY = "#1F1F1F"  # Almost black for primary text
BISTRO_TEXT_SECONDARY = "#666666"  # Gray for secondary text
BISTRO_DISABLED = "#CCCCCC"  # Gray for disabled elements
BISTRO_SUCCESS = "#4CAF50"  # Green for success states

# Create theme
app_theme = ft.Theme(
    color_scheme_seed=BISTRO_PRIMARY,
    color_scheme=ft.ColorScheme(
        primary=BISTRO_PRIMARY,
        primary_container=BISTRO_PRIMARY,
        secondary=BISTRO_SECONDARY,
        background=BISTRO_BACKGROUND,
        surface=BISTRO_SURFACE,
        error=BISTRO_ERROR,
        on_primary="#FFFFFF",
        on_secondary="#000000",
        on_background=BISTRO_TEXT_PRIMARY,
        on_surface=BISTRO_TEXT_PRIMARY,
    ),
    visual_density=ft.ThemeVisualDensity.COMFORTABLE,
    use_material3=True,
)

# Typography
FONT_FAMILY = "Cairo, Roboto, sans-serif"

# Styles
def text_style_heading(size=24, weight=ft.FontWeight.BOLD, color=BISTRO_TEXT_PRIMARY):
    return ft.TextStyle(
        font_family=FONT_FAMILY,
        size=size,
        weight=weight,
        color=color,
    )

def text_style_body(size=16, weight=ft.FontWeight.NORMAL, color=BISTRO_TEXT_PRIMARY):
    return ft.TextStyle(
        font_family=FONT_FAMILY,
        size=size,
        weight=weight,
        color=color,
    )

# Common UI element styles
def primary_button_style():
    return ft.ButtonStyle(
        color=ft.colors.WHITE,
        bgcolor=BISTRO_PRIMARY,
        elevation=1,
        padding=10,
        shape=ft.RoundedRectangleBorder(radius=8),
    )

def secondary_button_style():
    return ft.ButtonStyle(
        color=BISTRO_PRIMARY,
        bgcolor=ft.colors.WHITE,
        elevation=0,
        side=ft.BorderSide(1, BISTRO_PRIMARY),
        padding=10,
        shape=ft.RoundedRectangleBorder(radius=8),
    )

def card_style():
    return ft.CardStyle(
        color=BISTRO_SURFACE,
        elevation=2,
        shape=ft.RoundedRectangleBorder(radius=12),
    )
