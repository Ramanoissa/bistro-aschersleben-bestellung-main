
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowLeft, LogOut, Map, ShoppingBag, User, Edit } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";

const Profile = () => {
  // Mock user data - in a real app this would come from authentication
  const [user] = useState({
    name: "محمد أحمد",
    email: "mohamed@example.com",
    phone: "+49123456789"
  });
  
  const navigate = useNavigate();
  const { toast } = useToast();

  // Mock order history
  const [orders] = useState([
    {
      id: "123456",
      date: "2025-05-08",
      status: "delivered",
      total: 18.96
    },
    {
      id: "123455",
      date: "2025-05-03",
      status: "delivered",
      total: 14.50
    }
  ]);

  const handleLogout = () => {
    toast({
      title: "تم تسجيل الخروج",
      description: "نتمنى رؤيتك مرة أخرى قريبًا",
    });
    navigate("/");
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">الملف الشخصي</h1>
        <Link to="/menu">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      <div className="flex-1 p-4">
        {/* User Profile Card */}
        <Card className="p-4 mb-4">
          <div className="flex justify-between items-center mb-4">
            <Button variant="ghost" size="icon" className="text-gray-500">
              <Edit className="h-5 w-5" />
            </Button>
            <div className="flex items-center">
              <div className="text-right ml-4">
                <h2 className="font-bold text-lg">{user.name}</h2>
                <p className="text-sm text-gray-600">{user.email}</p>
                <p className="text-sm text-gray-600">{user.phone}</p>
              </div>
              <div className="w-12 h-12 bg-[#9C3D54] text-white rounded-full flex items-center justify-center">
                <User className="h-6 w-6" />
              </div>
            </div>
          </div>
        </Card>
        
        {/* Order History */}
        <h2 className="font-bold text-lg text-right mb-2">سجل الطلبات</h2>
        <Card className="mb-4">
          {orders.length > 0 ? (
            <div className="divide-y">
              {orders.map(order => (
                <Link key={order.id} to={`/order-tracking/${order.id}`}>
                  <div className="p-4 flex justify-between items-center hover:bg-gray-50">
                    <div>
                      <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded">
                        تم التسليم
                      </span>
                    </div>
                    <div className="text-right">
                      <p className="font-medium">طلب #{order.id}</p>
                      <p className="text-sm text-gray-600">{order.date}</p>
                      <p className="font-bold">{order.total.toFixed(2)} €</p>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          ) : (
            <div className="p-4 text-center">
              <p>لا يوجد طلبات سابقة</p>
            </div>
          )}
        </Card>
        
        {/* Saved Addresses */}
        <h2 className="font-bold text-lg text-right mb-2">العناوين المحفوظة</h2>
        <Card className="mb-4">
          <div className="p-4 flex justify-between items-center">
            <Button variant="ghost" size="icon">
              <Edit className="h-5 w-5" />
            </Button>
            <div className="text-right">
              <p className="font-medium">المنزل</p>
              <p className="text-sm text-gray-600">Herrenbreite 12, 06449 Aschersleben</p>
            </div>
          </div>
        </Card>
        
        {/* Actions */}
        <div className="space-y-2">
          <Button variant="outline" className="w-full justify-start border-gray-300" asChild>
            <Link to="/addresses">
              <Map className="mr-2 h-5 w-5" />
              إدارة العناوين
            </Link>
          </Button>
          
          <Button variant="outline" className="w-full justify-start border-gray-300" asChild>
            <Link to="/orders">
              <ShoppingBag className="mr-2 h-5 w-5" />
              جميع الطلبات
            </Link>
          </Button>
          
          <Button 
            variant="outline" 
            className="w-full justify-start border-gray-300 text-red-500 hover:text-red-600 hover:border-red-200"
            onClick={handleLogout}
          >
            <LogOut className="mr-2 h-5 w-5" />
            تسجيل الخروج
          </Button>
        </div>
      </div>
      
      {/* Navigation Footer */}
      <footer className="bg-white border-t border-gray-200 p-4 sticky bottom-0">
        <div className="flex justify-around">
          <Link to="/profile" className="flex flex-col items-center text-[#9C3D54]">
            <span>👤</span>
            <span className="text-xs">الحساب</span>
          </Link>
          <Link to="/offers" className="flex flex-col items-center text-gray-600">
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

export default Profile;
