
import flet as ft
from utils.theme import BISTRO_PRIMARY, BISTRO_SECONDARY, text_style_heading, text_style_body
import time
import asyncio

class OrderTrackingView(ft.Container):
    def __init__(self, page, router, app_state, order_id):
        super().__init__()
        self.page = page
        self.router = router
        self.app_state = app_state
        self.order_id = order_id
        self.expand = True
        
        # Order status (in a real app, this would be fetched from a server)
        # For demo, we'll create a fake order if none exists
        if not hasattr(self.app_state, "current_order") or not self.app_state.current_order:
            self.app_state.current_order = {
                "order_id": order_id,
                "status": "pending",
                "delivery_method": "delivery",
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "estimated_time": 30,  # minutes
            }
        
        self.order = self.app_state.current_order
        self.status_updates = []
        self.content = self.build()
        
        # Start automatic status updates
        asyncio.create_task(self.simulate_status_updates())
    
    def build(self):
        # Determine the current status step
        status_steps = ["pending", "preparing", "ready", "out_for_delivery", "delivered"]
        current_step = 0
        for i, status in enumerate(status_steps):
            if self.order["status"] == status:
                current_step = i
                break
        
        # Create the status indicator
        status_indicator = ft.ProgressBar(
            value=current_step / (len(status_steps) - 1),
            color=BISTRO_PRIMARY,
            bgcolor=ft.colors.GREY_300,
            height=10,
        )
        
        # Create a row of status step icons
        status_icons = []
        for i, status in enumerate(status_steps):
            if i <= current_step:
                # Completed or current step
                color = BISTRO_PRIMARY
                icon_name = ft.icons.CHECK_CIRCLE if i < current_step else ft.icons.RADIO_BUTTON_CHECKED
            else:
                # Future step
                color = ft.colors.GREY_400
                icon_name = ft.icons.RADIO_BUTTON_UNCHECKED
            
            # Skip "out_for_delivery" step if pickup
            if self.order["delivery_method"] == "pickup" and status == "out_for_delivery":
                continue
            
            status_icons.append(
                ft.Container(
                    content=ft.Icon(icon_name, color=color),
                    alignment=ft.alignment.center,
                )
            )
        
        # Status message based on current status
        status_messages = {
            "pending": "تم استلام طلبك ويتم الآن مراجعته",
            "preparing": "يتم تحضير طلبك",
            "ready": "طلبك جاهز" + (" للتوصيل" if self.order["delivery_method"] == "delivery" else " للاستلام"),
            "out_for_delivery": "طلبك في الطريق إليك",
            "delivered": "تم تسليم طلبك"
        }
        
        # Build the status updates list
        status_updates_list = ft.Column(
            spacing=10,
            controls=[]
        )
        
        for update in self.status_updates:
            status_updates_list.controls.append(
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                update["time"],
                                style=text_style_body(size=14, color=ft.colors.GREY),
                            ),
                            ft.Text(
                                update["message"],
                                text_align=ft.TextAlign.RIGHT,
                                style=text_style_body(size=14),
                            ),
                        ],
                    ),
                    padding=10,
                    bgcolor=ft.colors.GREY_100,
                    border_radius=8,
                )
            )
        
        # Estimated time calculation
        current_time = time.time()
        order_time = time.mktime(time.strptime(self.order["created_at"], "%Y-%m-%d %H:%M:%S"))
        elapsed_minutes = (current_time - order_time) / 60
        
        total_time = self.order.get("estimated_time", 30)  # Default to 30 minutes if not specified
        remaining_minutes = max(0, total_time - elapsed_minutes)
        
        if self.order["status"] == "delivered":
            time_message = "تم التسليم!"
        else:
            time_message = f"الوقت المتبقي: {int(remaining_minutes)} دقيقة"
        
        return ft.Column(
            spacing=0,
            controls=[
                # Top bar
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.HOME,
                                on_click=lambda _: self.router.go("/"),
                            ),
                            ft.Text(
                                "تتبع الطلب",
                                style=text_style_heading(size=20),
                            ),
                            ft.Container(width=40),  # Spacer for alignment
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                ),
                
                # Content
                ft.Container(
                    content=ft.Column(
                        spacing=20,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            # Order number
                            ft.Container(
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5,
                                    controls=[
                                        ft.Text(
                                            "رقم طلبك",
                                            style=text_style_body(size=14),
                                        ),
                                        ft.Text(
                                            f"#{self.order['order_id']}",
                                            style=text_style_heading(size=24),
                                        ),
                                    ],
                                ),
                                margin=ft.margin.only(top=10),
                            ),
                            
                            # Status
                            ft.Container(
                                content=ft.Column(
                                    spacing=15,
                                    controls=[
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=status_icons,
                                            ),
                                            margin=ft.margin.only(bottom=5),
                                        ),
                                        status_indicator,
                                        ft.Container(
                                            content=ft.Text(
                                                status_messages.get(self.order["status"], "جاري تتبع طلبك"),
                                                style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                            margin=ft.margin.only(top=10),
                                        ),
                                    ],
                                ),
                                margin=ft.margin.symmetric(vertical=10),
                            ),
                            
                            # Time
                            ft.Container(
                                content=ft.Text(
                                    time_message,
                                    style=text_style_heading(size=18),
                                    color=BISTRO_PRIMARY,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                margin=ft.margin.only(bottom=20),
                            ),
                            
                            # Status updates
                            ft.Container(
                                content=ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(
                                            "تحديثات الطلب",
                                            style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                        ),
                                        status_updates_list,
                                    ],
                                ),
                                visible=len(self.status_updates) > 0,
                            ),
                            
                            # Contact info
                            ft.Container(
                                content=ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(
                                            "هل تحتاج للمساعدة؟",
                                            style=text_style_body(size=16, weight=ft.FontWeight.BOLD),
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.ElevatedButton(
                                                    "اتصل بنا",
                                                    icon=ft.icons.PHONE,
                                                    on_click=self.call_restaurant,
                                                ),
                                                ft.ElevatedButton(
                                                    "رسالة",
                                                    icon=ft.icons.MESSAGE,
                                                    on_click=self.message_restaurant,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                margin=ft.margin.only(top=20),
                            ),
                            
                            # Return to menu button
                            ft.Container(
                                content=ft.ElevatedButton(
                                    "العودة إلى القائمة الرئيسية",
                                    on_click=lambda _: self.router.go("/"),
                                    width=float("inf"),
                                ),
                                margin=ft.margin.only(top=20, bottom=30),
                            ),
                        ],
                    ),
                    padding=ft.padding.all(15),
                    expand=True,
                ),
            ],
        )
    
    async def simulate_status_updates(self):
        """Simulate order status updates for demo purposes"""
        status_timeline = [
            {"status": "pending", "delay": 5, "message": "تم استلام طلبك"},
            {"status": "preparing", "delay": 10, "message": "بدأ الطهاة بتحضير طلبك"},
            {"status": "ready", "delay": 15, "message": "طلبك جاهز للتسليم"},
        ]
        
        if self.order["delivery_method"] == "delivery":
            status_timeline.append(
                {"status": "out_for_delivery", "delay": 5, "message": "طلبك في الطريق إليك"}
            )
        
        status_timeline.append(
            {"status": "delivered", "delay": 5, "message": "تم تسليم طلبك"}
        )
        
        for i, step in enumerate(status_timeline):
            # Calculate time to wait (for demo, we'll accelerate the timeline)
            # In a real app, this would be replaced with server-side events
            if i > 0:
                await asyncio.sleep(step["delay"])
            
            # Update the order status
            self.order["status"] = step["status"]
            
            # Add a status update
            self.status_updates.insert(
                0,
                {
                    "time": time.strftime("%H:%M"),
                    "message": step["message"]
                }
            )
            
            # Update the UI
            self.content = self.build()
            self.page.update()
            
            # If delivered, stop the simulation
            if step["status"] == "delivered":
                break
    
    def call_restaurant(self, e):
        # In a real app, this would initiate a phone call
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("جاري الاتصال بالمطعم..."),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def message_restaurant(self, e):
        # In a real app, this would open a messaging interface
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("جاري فتح محادثة مع المطعم..."),
            action="حسناً"
        )
        self.page.snack_bar.open = True
        self.page.update()
