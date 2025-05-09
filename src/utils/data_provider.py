
"""
Data provider module that simulates backend API for menu items, categories, etc.
In a real app, this would fetch data from an actual backend API.
"""

from typing import List, Dict, Any

# Sample menu categories
CATEGORIES = [
    {"id": "1", "name": "البرجر", "image": "burger.png"},
    {"id": "2", "name": "البيتزا", "image": "pizza.png"},
    {"id": "3", "name": "المشروبات", "image": "drinks.png"},
    {"id": "4", "name": "الوجبات الجانبية", "image": "sides.png"},
    {"id": "5", "name": "الحلويات", "image": "desserts.png"},
]

# Sample menu items
MENU_ITEMS = [
    {
        "id": "101",
        "category_id": "1",
        "name": "برجر كلاسيك",
        "description": "برجر لحم طازج مع خس وطماطم وجبن وصلصة خاصة",
        "price": 6.99,
        "image": "classic_burger.png",
        "options": [
            {
                "name": "الحجم",
                "required": True,
                "multiple": False,
                "choices": [
                    {"name": "عادي", "price": 0},
                    {"name": "كبير", "price": 2.00}
                ]
            },
            {
                "name": "إضافات",
                "required": False,
                "multiple": True,
                "choices": [
                    {"name": "جبن إضافي", "price": 0.75},
                    {"name": "لحم إضافي", "price": 2.50},
                    {"name": "بيض", "price": 1.00}
                ]
            }
        ]
    },
    {
        "id": "102",
        "category_id": "1",
        "name": "برجر دجاج",
        "description": "برجر دجاج متبل مع خس وطماطم ومايونيز",
        "price": 5.99,
        "image": "chicken_burger.png",
        "options": [
            {
                "name": "الحجم",
                "required": True,
                "multiple": False,
                "choices": [
                    {"name": "عادي", "price": 0},
                    {"name": "كبير", "price": 1.50}
                ]
            },
            {
                "name": "إضافات",
                "required": False,
                "multiple": True,
                "choices": [
                    {"name": "جبن", "price": 0.75},
                    {"name": "بيكون", "price": 1.50}
                ]
            }
        ]
    },
    {
        "id": "201",
        "category_id": "2",
        "name": "بيتزا مارجريتا",
        "description": "صلصة طماطم وجبن موزاريلا وريحان",
        "price": 8.99,
        "image": "margherita.png",
        "options": [
            {
                "name": "الحجم",
                "required": True,
                "multiple": False,
                "choices": [
                    {"name": "صغير", "price": 0},
                    {"name": "وسط", "price": 2.00},
                    {"name": "كبير", "price": 4.00}
                ]
            },
            {
                "name": "إضافات",
                "required": False,
                "multiple": True,
                "choices": [
                    {"name": "فلفل", "price": 0.50},
                    {"name": "فطر", "price": 0.75},
                    {"name": "زيتون", "price": 0.50}
                ]
            }
        ]
    },
    {
        "id": "301",
        "category_id": "3",
        "name": "كولا",
        "description": "مشروب كولا منعش",
        "price": 1.99,
        "image": "cola.png",
        "options": [
            {
                "name": "الحجم",
                "required": True,
                "multiple": False,
                "choices": [
                    {"name": "صغير", "price": 0},
                    {"name": "وسط", "price": 0.50},
                    {"name": "كبير", "price": 1.00}
                ]
            }
        ]
    },
]

# Sample offers
OFFERS = [
    {
        "id": "o1",
        "title": "وجبة عائلية بخصم ٢٠٪",
        "description": "بيتزا كبيرة + ٢ برجر + بطاطس كبيرة + ٢ كولا",
        "image": "family_deal.png",
        "price": 19.99,
        "original_price": 24.99,
        "expires_at": "2023-12-31"
    },
    {
        "id": "o2",
        "title": "برجر + بطاطس + مشروب",
        "description": "وجبة برجر كاملة بسعر خاص",
        "image": "burger_meal.png",
        "price": 9.99,
        "original_price": 12.99,
        "expires_at": "2023-12-31"
    }
]

# Sample coupons
COUPONS = {
    "WELCOME10": {"discount_percent": 10, "min_order": 15.00, "expires_at": "2023-12-31"},
    "BISTRO20": {"discount_percent": 20, "min_order": 25.00, "expires_at": "2023-12-31"}
}

class DataProvider:
    @staticmethod
    def get_categories() -> List[Dict[str, Any]]:
        return CATEGORIES
    
    @staticmethod
    def get_menu_items(category_id: str = None) -> List[Dict[str, Any]]:
        if category_id:
            return [item for item in MENU_ITEMS if item["category_id"] == category_id]
        return MENU_ITEMS
    
    @staticmethod
    def get_menu_item(item_id: str) -> Dict[str, Any]:
        for item in MENU_ITEMS:
            if item["id"] == item_id:
                return item
        return None
    
    @staticmethod
    def get_offers() -> List[Dict[str, Any]]:
        return OFFERS
    
    @staticmethod
    def validate_coupon(code: str, order_total: float) -> Dict[str, Any]:
        code = code.upper()
        if code in COUPONS:
            coupon = COUPONS[code]
            if order_total >= coupon["min_order"]:
                return {
                    "valid": True,
                    "code": code,
                    "discount_percent": coupon["discount_percent"],
                    "discount_amount": (order_total * coupon["discount_percent"]) / 100
                }
            else:
                return {
                    "valid": False, 
                    "message": f"الطلب يجب أن يكون بقيمة {coupon['min_order']} € على الأقل"
                }
        return {"valid": False, "message": "كود الخصم غير صالح"}
    
    @staticmethod
    def mock_login(email: str, password: str) -> Dict[str, Any]:
        """Mock login function - in a real app this would authenticate with a backend"""
        if email == "test@example.com" and password == "password":
            return {
                "success": True,
                "user_data": {
                    "user_id": "u1",
                    "name": "أحمد محمد",
                    "email": "test@example.com",
                    "phone": "+49 123456789",
                    "addresses": [
                        {
                            "id": "addr1",
                            "name": "المنزل",
                            "street": "Herrenbreite 12",
                            "city": "Aschersleben",
                            "postcode": "06449",
                            "instructions": "الطابق الثاني"
                        }
                    ]
                }
            }
        return {"success": False, "message": "بريد إلكتروني أو كلمة مرور خاطئة"}
