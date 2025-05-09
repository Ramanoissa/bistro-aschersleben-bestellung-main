
import { Card } from "@/components/ui/card";
import { Link } from "react-router-dom";
import { ArrowLeft, Copy } from "lucide-react";
import { useState } from "react";
import { useToast } from "@/components/ui/use-toast";

// Mock offers data
const offers = [
  {
    id: 1,
    title: "خصم 10% على طلبك الأول",
    code: "WELCOME10",
    validUntil: "2025-06-30",
    description: "استمتع بخصم 10% على طلبك الأول من Bistro Aschersleben",
    image: "https://images.unsplash.com/photo-1550547660-d9450f859349?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    bgColor: "#FCE7F3"
  },
  {
    id: 2,
    title: "وجبة عائلية بسعر مميز",
    code: "FAMILY25",
    validUntil: "2025-05-31",
    description: "4 برجر + 2 بطاطس كبير + 4 مشروبات بخصم 25%",
    image: "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80",
    bgColor: "#E0F2FE"
  },
  {
    id: 3,
    title: "توصيل مجاني",
    code: "FREEDEL",
    validUntil: "2025-05-20",
    description: "توصيل مجاني للطلبات التي تزيد عن 20€",
    image: "https://images.unsplash.com/photo-1595425873732-faeed679dd86?ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80",
    bgColor: "#ECFCCB"
  }
];

const Offers = () => {
  const { toast } = useToast();

  const handleCopyCode = (code) => {
    navigator.clipboard.writeText(code).then(() => {
      toast({
        title: "تم نسخ الكود",
        description: `تم نسخ الكود ${code} إلى الحافظة`,
      });
    });
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">العروض والخصومات</h1>
        <Link to="/menu">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      <div className="flex-1 p-4">
        <div className="space-y-4">
          {offers.map(offer => (
            <Card 
              key={offer.id} 
              className="overflow-hidden"
              style={{ backgroundColor: offer.bgColor }}
            >
              <div className="p-4 text-right">
                <h2 className="font-bold text-lg mb-2">{offer.title}</h2>
                <p className="text-sm text-gray-700 mb-4">{offer.description}</p>
                
                <div className="flex justify-between items-center bg-white rounded p-2 mb-2">
                  <button 
                    onClick={() => handleCopyCode(offer.code)}
                    className="text-[#9C3D54] flex items-center"
                  >
                    <Copy className="h-4 w-4 mr-1" />
                    نسخ
                  </button>
                  <span className="font-bold">{offer.code}</span>
                </div>
                
                <p className="text-xs text-gray-600">
                  صالح حتى {new Date(offer.validUntil).toLocaleDateString('ar-EG')}
                </p>
              </div>
            </Card>
          ))}
        </div>

        {/* Notification preferences */}
        <Card className="p-4 mt-6">
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <input 
                type="checkbox" 
                id="notifications" 
                className="h-5 w-5 text-[#9C3D54]"
                defaultChecked 
              />
            </div>
            <div className="text-right">
              <label htmlFor="notifications" className="font-medium cursor-pointer">
                تلقي إشعارات بالعروض الجديدة
              </label>
              <p className="text-sm text-gray-600">
                سنرسل لك إشعارات عند إضافة عروض جديدة
              </p>
            </div>
          </div>
        </Card>
      </div>
      
      {/* Navigation Footer */}
      <footer className="bg-white border-t border-gray-200 p-4 sticky bottom-0">
        <div className="flex justify-around">
          <Link to="/profile" className="flex flex-col items-center text-gray-600">
            <span>👤</span>
            <span className="text-xs">الحساب</span>
          </Link>
          <Link to="/offers" className="flex flex-col items-center text-[#9C3D54]">
            <span>🏷️</span>
            <span className="text-xs">العروض</span>
          </Link>
          <Link to="/cart" className="flex flex-col items-center text-gray-600">
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

export default Offers;
