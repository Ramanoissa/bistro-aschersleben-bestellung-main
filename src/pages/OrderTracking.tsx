
import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { ArrowLeft } from "lucide-react";
import { Card } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";

const OrderTracking = () => {
  const { orderId } = useParams();
  const [orderStatus, setOrderStatus] = useState("preparing"); // "preparing", "on_the_way", "delivered"
  const [progress, setProgress] = useState(30);
  const [estimatedTime, setEstimatedTime] = useState(30); // minutes
  const [orderDetails] = useState({
    id: orderId,
    items: [
      { name: "برجر كلاسيك", quantity: 1, price: 6.99 },
      { name: "بطاطس مقلية", quantity: 2, price: 2.99 },
      { name: "كولا", quantity: 1, price: 1.99 }
    ],
    total: 18.96,
    deliveryMethod: "delivery",
    address: "Herrenbreite 12, 06449 Aschersleben",
    paymentMethod: "cash"
  });

  // Simulate order progress
  useEffect(() => {
    const timer = setTimeout(() => {
      if (orderStatus === "preparing") {
        setOrderStatus("on_the_way");
        setProgress(60);
        setEstimatedTime(15);
      } else if (orderStatus === "on_the_way") {
        setOrderStatus("delivered");
        setProgress(100);
        setEstimatedTime(0);
      }
    }, 10000); // Change status every 10 seconds for demo

    return () => clearTimeout(timer);
  }, [orderStatus]);

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">تتبع الطلب</h1>
        <Link to="/menu">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      <div className="flex-1 p-4">
        {/* Order ID and Status */}
        <Card className="p-4 mb-4">
          <div className="flex justify-between items-center">
            <span className={`px-2 py-1 rounded text-sm ${
              orderStatus === "preparing" ? "bg-yellow-100 text-yellow-800" :
              orderStatus === "on_the_way" ? "bg-blue-100 text-blue-800" : 
              "bg-green-100 text-green-800"
            }`}>
              {orderStatus === "preparing" ? "قيد التحضير" :
               orderStatus === "on_the_way" ? "في الطريق" : 
               "تم التسليم"}
            </span>
            <div className="text-right">
              <p className="text-sm text-gray-500">رقم الطلب</p>
              <p className="font-bold">{orderId}</p>
            </div>
          </div>
        </Card>
        
        {/* Progress Tracker */}
        <Card className="p-4 mb-4">
          <div className="mb-2">
            <div className="flex justify-between mb-1">
              <span className="text-sm text-gray-500">
                {estimatedTime > 0 ? `الوقت المتبقي: ${estimatedTime} دقيقة` : "تم التسليم"}
              </span>
              <span className="text-sm font-bold">{progress}%</span>
            </div>
            <Progress value={progress} className="h-2" />
          </div>
          
          <div className="flex justify-between mt-4 text-center">
            <div className="flex-1">
              <div className={`w-8 h-8 mx-auto rounded-full flex items-center justify-center ${
                progress >= 30 ? "bg-[#9C3D54] text-white" : "bg-gray-200"
              }`}>
                1
              </div>
              <p className="text-xs mt-1">قيد التحضير</p>
            </div>
            <div className="flex-1">
              <div className={`w-8 h-8 mx-auto rounded-full flex items-center justify-center ${
                progress >= 60 ? "bg-[#9C3D54] text-white" : "bg-gray-200"
              }`}>
                2
              </div>
              <p className="text-xs mt-1">في الطريق</p>
            </div>
            <div className="flex-1">
              <div className={`w-8 h-8 mx-auto rounded-full flex items-center justify-center ${
                progress == 100 ? "bg-[#9C3D54] text-white" : "bg-gray-200"
              }`}>
                3
              </div>
              <p className="text-xs mt-1">تم التسليم</p>
            </div>
          </div>
        </Card>
        
        {/* Order Details */}
        <Card className="p-4 mb-4">
          <h2 className="font-bold text-lg text-right mb-4">تفاصيل الطلب</h2>
          
          <div className="space-y-2">
            {orderDetails.items.map((item, index) => (
              <div key={index} className="flex justify-between py-2 border-b">
                <div className="text-left">
                  <span>{(item.price * item.quantity).toFixed(2)} €</span>
                </div>
                <div className="text-right">
                  <span className="font-medium">{item.name}</span>
                  <span className="mx-2 text-gray-500">×{item.quantity}</span>
                </div>
              </div>
            ))}
            
            <div className="flex justify-between pt-2">
              <span className="font-bold">{orderDetails.total.toFixed(2)} €</span>
              <span className="font-bold">الإجمالي:</span>
            </div>
          </div>
        </Card>
        
        {/* Delivery Information */}
        <Card className="p-4">
          <h2 className="font-bold text-lg text-right mb-4">معلومات {orderDetails.deliveryMethod === "delivery" ? "التوصيل" : "الاستلام"}</h2>
          
          <div className="space-y-2 text-right">
            {orderDetails.deliveryMethod === "delivery" ? (
              <>
                <p><strong>العنوان:</strong> {orderDetails.address}</p>
                <p><strong>طريقة الدفع:</strong> {orderDetails.paymentMethod === "cash" ? "نقدًا عند الاستلام" : 
                                               orderDetails.paymentMethod === "card" ? "بطاقة عند الاستلام" : "دفع إلكتروني"}</p>
              </>
            ) : (
              <>
                <p><strong>عنوان المطعم:</strong> Herrenbreite 12, 06449 Aschersleben</p>
                <p><strong>طريقة الدفع:</strong> {orderDetails.paymentMethod === "cash" ? "نقدًا عند الاستلام" : 
                                               orderDetails.paymentMethod === "card" ? "بطاقة عند الاستلام" : "دفع إلكتروني"}</p>
              </>
            )}
          </div>
        </Card>
      </div>
      
      {/* Help Button */}
      <div className="p-4 bg-white border-t">
        <Link to="/support">
          <button className="w-full py-3 border border-[#9C3D54] text-[#9C3D54] rounded-md font-medium">
            هل تحتاج مساعدة؟
          </button>
        </Link>
      </div>
    </div>
  );
};

export default OrderTracking;
