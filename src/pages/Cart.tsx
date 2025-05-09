
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { ArrowLeft, Trash, Plus, Minus } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";

// Sample cart items
const initialCartItems = [
  {
    id: "classic_burger",
    name: "برجر كلاسيك",
    price: 6.99,
    quantity: 1,
    options: "مع جبنة إضافية"
  },
  {
    id: "fries",
    name: "بطاطس مقلية",
    price: 2.99,
    quantity: 2,
    options: "حجم كبير"
  },
  {
    id: "cola",
    name: "كولا",
    price: 1.99,
    quantity: 1,
    options: ""
  }
];

const Cart = () => {
  const [cartItems, setCartItems] = useState(initialCartItems);
  const [couponCode, setCouponCode] = useState("");
  const [discount, setDiscount] = useState(0);
  const [isApplyingCoupon, setIsApplyingCoupon] = useState(false);
  
  const navigate = useNavigate();
  const { toast } = useToast();

  const subtotal = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const deliveryFee = 2.00;
  const total = subtotal + deliveryFee - discount;

  const handleQuantityChange = (id, change) => {
    setCartItems(prev => prev.map(item => {
      if (item.id === id) {
        const newQuantity = Math.max(1, item.quantity + change);
        return { ...item, quantity: newQuantity };
      }
      return item;
    }));
  };

  const handleRemoveItem = (id) => {
    setCartItems(prev => prev.filter(item => item.id !== id));
  };

  const handleApplyCoupon = () => {
    if (!couponCode) {
      toast({
        title: "خطأ",
        description: "الرجاء إدخال كود الخصم",
        variant: "destructive",
      });
      return;
    }
    
    setIsApplyingCoupon(true);
    
    // Simulate coupon validation
    setTimeout(() => {
      if (couponCode === "WELCOME10") {
        const discountAmount = subtotal * 0.1; // 10% discount
        setDiscount(discountAmount);
        toast({
          title: "تم تطبيق الخصم",
          description: `تم خصم ${discountAmount.toFixed(2)} €`,
        });
      } else {
        toast({
          title: "خطأ",
          description: "كود الخصم غير صالح",
          variant: "destructive",
        });
      }
      setIsApplyingCoupon(false);
    }, 1000);
  };

  const handleCheckout = () => {
    if (cartItems.length === 0) {
      toast({
        title: "السلة فارغة",
        description: "الرجاء إضافة منتجات إلى السلة أولاً",
        variant: "destructive",
      });
      return;
    }
    
    navigate("/checkout");
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">سلة التسوق</h1>
        <Link to="/menu">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      {/* Cart Items */}
      <div className="flex-1 p-4">
        {cartItems.length === 0 ? (
          <div className="text-center py-16">
            <div className="text-gray-400 text-5xl mb-4">🛒</div>
            <h2 className="text-xl font-bold mb-2">السلة فارغة</h2>
            <p className="text-gray-600 mb-6">لم تقم بإضافة أي منتجات إلى السلة بعد</p>
            <Button 
              onClick={() => navigate("/menu")} 
              className="bg-[#9C3D54] hover:bg-[#7d314a]"
            >
              تصفح القائمة
            </Button>
          </div>
        ) : (
          <div className="space-y-4">
            {cartItems.map((item) => (
              <Card key={item.id} className="p-4">
                <div className="flex justify-between">
                  <div className="flex flex-col items-end flex-1">
                    <div className="flex justify-between w-full">
                      <button 
                        onClick={() => handleRemoveItem(item.id)}
                        className="text-red-500 p-1"
                      >
                        <Trash className="h-5 w-5" />
                      </button>
                      <h3 className="font-bold text-lg">{item.name}</h3>
                    </div>
                    
                    {item.options && (
                      <p className="text-sm text-gray-600 mt-1">{item.options}</p>
                    )}
                    
                    <div className="flex justify-between w-full mt-2">
                      <div className="flex items-center">
                        <button 
                          onClick={() => handleQuantityChange(item.id, -1)}
                          className="p-1 rounded-full bg-gray-200"
                        >
                          <Minus className="h-4 w-4" />
                        </button>
                        <span className="mx-2 min-w-[20px] text-center">{item.quantity}</span>
                        <button 
                          onClick={() => handleQuantityChange(item.id, 1)}
                          className="p-1 rounded-full bg-gray-200"
                        >
                          <Plus className="h-4 w-4" />
                        </button>
                      </div>
                      <span className="font-bold">{(item.price * item.quantity).toFixed(2)} €</span>
                    </div>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>
      
      {/* Order Summary */}
      {cartItems.length > 0 && (
        <Card className="m-4 p-4">
          <h3 className="font-bold text-lg text-right mb-4">ملخص الطلب</h3>
          
          {/* Coupon */}
          <div className="flex space-x-2 space-x-reverse flex-row-reverse mb-4">
            <Input
              placeholder="كود الخصم"
              value={couponCode}
              onChange={(e) => setCouponCode(e.target.value)}
              className="text-right"
              dir="rtl"
            />
            <Button 
              onClick={handleApplyCoupon}
              disabled={isApplyingCoupon}
              variant="outline"
              className="border-[#9C3D54] text-[#9C3D54]"
            >
              تطبيق
            </Button>
          </div>
          
          {/* Price breakdown */}
          <div className="space-y-2 text-right">
            <div className="flex justify-between">
              <span>{subtotal.toFixed(2)} €</span>
              <span>المجموع الفرعي:</span>
            </div>
            <div className="flex justify-between">
              <span>{deliveryFee.toFixed(2)} €</span>
              <span>رسوم التوصيل:</span>
            </div>
            {discount > 0 && (
              <div className="flex justify-between text-green-600">
                <span>-{discount.toFixed(2)} €</span>
                <span>الخصم:</span>
              </div>
            )}
            <div className="border-t pt-2 mt-2">
              <div className="flex justify-between font-bold">
                <span>{total.toFixed(2)} €</span>
                <span>الإجمالي:</span>
              </div>
            </div>
          </div>
          
          {/* Checkout button */}
          <Button
            onClick={handleCheckout}
            className="w-full bg-[#9C3D54] hover:bg-[#7d314a] h-12 text-lg mt-4"
          >
            متابعة للدفع
          </Button>
        </Card>
      )}
      
      {/* Navigation Footer */}
      <footer className="bg-white border-t border-gray-200 p-4 sticky bottom-0">
        <div className="flex justify-around">
          <Link to="/profile" className="flex flex-col items-center text-gray-600">
            <span>👤</span>
            <span className="text-xs">الحساب</span>
          </Link>
          <Link to="/offers" className="flex flex-col items-center text-gray-600">
            <span>🏷️</span>
            <span className="text-xs">العروض</span>
          </Link>
          <Link to="/cart" className="flex flex-col items-center text-[#9C3D54]">
            <span>🛒</span>
            <span className="text-xs">السلة</span>
          </Link>
          <Link to="/menu" className="flex flex-col items-center text-gray-600">
            <span>🍔</span>
            <span className="text-xs">القائمة</span>
          </Link>
        </div>
      </footer>
    </div>
  );
};

export default Cart;
