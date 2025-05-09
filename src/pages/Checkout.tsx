
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowLeft } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Link, useNavigate } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";

const Checkout = () => {
  const [deliveryMethod, setDeliveryMethod] = useState("delivery");
  const [paymentMethod, setPaymentMethod] = useState("cash");
  const [isLoading, setIsLoading] = useState(false);
  
  const navigate = useNavigate();
  const { toast } = useToast();

  // Form states
  const [address, setAddress] = useState({
    name: "",
    street: "",
    city: "Aschersleben",
    postalCode: "06449",
    notes: ""
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAddress(prev => ({ ...prev, [name]: value }));
  };

  const handlePlaceOrder = () => {
    if (deliveryMethod === "delivery" && (!address.name || !address.street)) {
      toast({
        title: "خطأ",
        description: "الرجاء إدخال بيانات العنوان بشكل صحيح",
        variant: "destructive",
      });
      return;
    }
    
    setIsLoading(true);
    
    // Simulate order placement
    setTimeout(() => {
      setIsLoading(false);
      toast({
        title: "تم تأكيد الطلب",
        description: "سيتم توصيل طلبك قريبًا",
      });
      navigate("/order-tracking/123456");
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">تأكيد الطلب</h1>
        <Link to="/cart">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      <div className="flex-1 p-4">
        {/* Delivery Options */}
        <Card className="p-4 mb-4">
          <h2 className="font-bold text-lg text-right mb-4">خيارات الاستلام</h2>
          
          <Tabs defaultValue="delivery" className="w-full" onValueChange={setDeliveryMethod}>
            <TabsList className="grid w-full grid-cols-2 mb-4">
              <TabsTrigger value="pickup">استلام من المطعم</TabsTrigger>
              <TabsTrigger value="delivery">توصيل للمنزل</TabsTrigger>
            </TabsList>
            
            <TabsContent value="delivery" className="space-y-4">
              <div className="space-y-2 text-right">
                <label htmlFor="name" className="block font-medium">
                  الاسم على الجرس
                </label>
                <Input
                  id="name"
                  name="name"
                  placeholder="محمد أحمد"
                  value={address.name}
                  onChange={handleInputChange}
                  className="text-right"
                  dir="rtl"
                />
              </div>
              
              <div className="space-y-2 text-right">
                <label htmlFor="street" className="block font-medium">
                  الشارع ورقم المنزل
                </label>
                <Input
                  id="street"
                  name="street"
                  placeholder="Herrenbreite 12"
                  value={address.street}
                  onChange={handleInputChange}
                  className="text-right"
                  dir="rtl"
                />
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2 text-right">
                  <label htmlFor="postalCode" className="block font-medium">
                    الرمز البريدي
                  </label>
                  <Input
                    id="postalCode"
                    name="postalCode"
                    value={address.postalCode}
                    onChange={handleInputChange}
                    className="text-right"
                    dir="rtl"
                  />
                </div>
                <div className="space-y-2 text-right">
                  <label htmlFor="city" className="block font-medium">
                    المدينة
                  </label>
                  <Input
                    id="city"
                    name="city"
                    value={address.city}
                    onChange={handleInputChange}
                    className="text-right"
                    dir="rtl"
                  />
                </div>
              </div>
              
              <div className="space-y-2 text-right">
                <label htmlFor="notes" className="block font-medium">
                  ملاحظات إضافية (اختياري)
                </label>
                <Input
                  id="notes"
                  name="notes"
                  placeholder="مثال: الطابق الثالث"
                  value={address.notes}
                  onChange={handleInputChange}
                  className="text-right"
                  dir="rtl"
                />
              </div>
              
              <div className="bg-gray-100 rounded p-3 text-center">
                <p>وقت التوصيل المتوقع: 30-45 دقيقة</p>
                <p>رسوم التوصيل: 2.00 €</p>
              </div>
            </TabsContent>
            
            <TabsContent value="pickup">
              <div className="bg-gray-100 rounded p-4 text-center">
                <h3 className="font-bold mb-2">Bistro Aschersleben</h3>
                <p className="mb-2">Herrenbreite 12, 06449 Aschersleben</p>
                <p>وقت التحضير المتوقع: 15-20 دقيقة</p>
              </div>
            </TabsContent>
          </Tabs>
        </Card>
        
        {/* Payment Options */}
        <Card className="p-4 mb-4">
          <h2 className="font-bold text-lg text-right mb-4">طريقة الدفع</h2>
          
          <div className="space-y-3 text-right">
            <div className="flex items-center justify-end space-x-2 space-x-reverse">
              <label htmlFor="cash" className="cursor-pointer">الدفع عند الاستلام (نقدًا)</label>
              <input
                type="radio"
                id="cash"
                name="paymentMethod"
                value="cash"
                checked={paymentMethod === "cash"}
                onChange={() => setPaymentMethod("cash")}
                className="cursor-pointer"
              />
            </div>
            
            <div className="flex items-center justify-end space-x-2 space-x-reverse">
              <label htmlFor="card" className="cursor-pointer">الدفع عند الاستلام (بطاقة)</label>
              <input
                type="radio"
                id="card"
                name="paymentMethod"
                value="card"
                checked={paymentMethod === "card"}
                onChange={() => setPaymentMethod("card")}
                className="cursor-pointer"
              />
            </div>
            
            <div className="flex items-center justify-end space-x-2 space-x-reverse">
              <label htmlFor="online" className="cursor-pointer">الدفع الإلكتروني</label>
              <input
                type="radio"
                id="online"
                name="paymentMethod"
                value="online"
                checked={paymentMethod === "online"}
                onChange={() => setPaymentMethod("online")}
                className="cursor-pointer"
              />
            </div>
          </div>
        </Card>
        
        {/* Order Summary */}
        <Card className="p-4">
          <h2 className="font-bold text-lg text-right mb-4">ملخص الطلب</h2>
          
          <div className="space-y-2 text-right">
            <div className="flex justify-between">
              <span>16.96 €</span>
              <span>المجموع الفرعي:</span>
            </div>
            
            {deliveryMethod === "delivery" && (
              <div className="flex justify-between">
                <span>2.00 €</span>
                <span>رسوم التوصيل:</span>
              </div>
            )}
            
            <div className="border-t pt-2 mt-2">
              <div className="flex justify-between font-bold">
                <span>{deliveryMethod === "delivery" ? "18.96 €" : "16.96 €"}</span>
                <span>الإجمالي:</span>
              </div>
            </div>
          </div>
        </Card>
      </div>
      
      {/* Place Order Button */}
      <div className="p-4 bg-white border-t">
        <Button
          onClick={handlePlaceOrder}
          className="w-full bg-[#9C3D54] hover:bg-[#7d314a] h-12 text-lg"
          disabled={isLoading}
        >
          {isLoading ? "جاري تأكيد الطلب..." : "تأكيد الطلب"}
        </Button>
      </div>
    </div>
  );
};

export default Checkout;
