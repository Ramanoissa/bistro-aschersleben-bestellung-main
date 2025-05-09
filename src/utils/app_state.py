
import json
import os
from typing import Dict, List, Optional

class User:
    def __init__(self, user_id: str = "", name: str = "", email: str = "", phone: str = ""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.addresses = []

class CartItem:
    def __init__(self, product_id: str, name: str, price: float, quantity: int = 1, options: Dict = None, notes: str = ""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.options = options if options else {}
        self.notes = notes
        
    @property
    def total_price(self):
        # Calculate the total price including options
        base_price = self.price * self.quantity
        options_price = sum(option.get('price', 0) for option in self.options.values())
        return base_price + (options_price * self.quantity)
    
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "options": self.options,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            options=data["options"],
            notes=data["notes"]
        )

class Order:
    def __init__(self, order_id: str, user_id: str, items: List[CartItem], 
                 total: float, status: str, delivery_method: str, 
                 address: Dict = None, payment_method: str = "", created_at: str = ""):
        self.order_id = order_id
        self.user_id = user_id
        self.items = items
        self.total = total
        self.status = status  # "pending", "preparing", "out_for_delivery", "delivered"
        self.delivery_method = delivery_method  # "delivery" or "pickup"
        self.address = address
        self.payment_method = payment_method
        self.created_at = created_at

class AppState:
    def __init__(self):
        self.user: Optional[User] = None
        self.cart_items: List[CartItem] = []
        self.current_order: Optional[Order] = None
        self.applied_coupon: Optional[str] = None
        self.discount_amount: float = 0.0
        self.selected_address: Optional[Dict] = None
        self.selected_payment_method: Optional[str] = None
        self.delivery_method: str = "delivery"  # Default to delivery
        
        # Load user data if available (would connect to backend in production)
        self._load_user_data()
        self._load_cart_data()
    
    def _load_user_data(self):
        """Load user data from storage (mock implementation)"""
        # In a real app, this would fetch from a backend API
        pass
    
    def _load_cart_data(self):
        """Load cart data from local storage"""
        # In a real app, this might use local storage APIs
        try:
            if os.path.exists("cart_data.json"):
                with open("cart_data.json", "r") as f:
                    cart_data = json.load(f)
                    self.cart_items = [CartItem.from_dict(item) for item in cart_data]
        except Exception:
            # If loading fails, start with an empty cart
            self.cart_items = []
    
    def save_cart_data(self):
        """Save cart data to local storage"""
        try:
            with open("cart_data.json", "w") as f:
                json.dump([item.to_dict() for item in self.cart_items], f)
        except Exception:
            # Handle error (in production, would log this)
            pass
    
    def add_to_cart(self, product_id: str, name: str, price: float, quantity: int = 1, options: Dict = None, notes: str = ""):
        # Check if the product is already in cart
        for item in self.cart_items:
            if item.product_id == product_id and item.options == options:
                item.quantity += quantity
                self.save_cart_data()
                return
        
        # If not found, add new item
        new_item = CartItem(product_id, name, price, quantity, options, notes)
        self.cart_items.append(new_item)
        self.save_cart_data()
    
    def remove_from_cart(self, product_id: str, options: Dict = None):
        self.cart_items = [item for item in self.cart_items 
                           if not (item.product_id == product_id and item.options == options)]
        self.save_cart_data()
    
    def update_cart_item_quantity(self, product_id: str, quantity: int, options: Dict = None):
        for item in self.cart_items:
            if item.product_id == product_id and item.options == options:
                if quantity <= 0:
                    self.remove_from_cart(product_id, options)
                else:
                    item.quantity = quantity
                self.save_cart_data()
                return
    
    def clear_cart(self):
        self.cart_items = []
        self.save_cart_data()
    
    @property
    def cart_total(self):
        return sum(item.total_price for item in self.cart_items)
    
    @property
    def final_total(self):
        return max(0, self.cart_total - self.discount_amount)
    
    @property
    def cart_item_count(self):
        return sum(item.quantity for item in self.cart_items)
    
    def login(self, user_data: Dict):
        # In a real app, this would verify credentials with a backend
        self.user = User(
            user_id=user_data.get("user_id", ""),
            name=user_data.get("name", ""),
            email=user_data.get("email", ""),
            phone=user_data.get("phone", "")
        )
        # Load user's addresses
        self.user.addresses = user_data.get("addresses", [])
        return True
    
    def logout(self):
        self.user = None
        # Optionally clear other personal data
    
    def is_authenticated(self):
        return self.user is not None
