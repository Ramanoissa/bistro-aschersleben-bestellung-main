
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { ArrowLeft } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";

const Signup = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!name || !email || !phone || !password) {
      toast({
        title: "خطأ",
        description: "الرجاء إدخال جميع البيانات المطلوبة",
        variant: "destructive",
      });
      return;
    }
    
    if (password !== confirmPassword) {
      toast({
        title: "خطأ",
        description: "كلمات المرور غير متطابقة",
        variant: "destructive",
      });
      return;
    }
    
    setIsLoading(true);
    
    // Simulate registration
    setTimeout(() => {
      setIsLoading(false);
      toast({
        title: "تم إنشاء الحساب بنجاح",
        description: "مرحبًا بك في بسترو اشرسلیبن",
      });
      navigate("/menu");
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 flex justify-between items-center">
        <div className="w-6"></div>
        <h1 className="text-xl font-bold text-center">إنشاء حساب</h1>
        <Link to="/">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      {/* Signup Form */}
      <div className="flex-1 p-4 flex flex-col justify-center">
        <Card className="p-6 max-w-md mx-auto w-full">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2 text-right">
              <label htmlFor="name" className="block font-medium">
                الاسم الكامل
              </label>
              <Input
                id="name"
                type="text"
                placeholder="محمد أحمد"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="text-right"
                dir="rtl"
              />
            </div>
            
            <div className="space-y-2 text-right">
              <label htmlFor="email" className="block font-medium">
                البريد الإلكتروني
              </label>
              <Input
                id="email"
                type="email"
                placeholder="your@email.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="text-right"
                dir="rtl"
              />
            </div>
            
            <div className="space-y-2 text-right">
              <label htmlFor="phone" className="block font-medium">
                رقم الهاتف
              </label>
              <Input
                id="phone"
                type="tel"
                placeholder="+49123456789"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                className="text-right"
                dir="rtl"
              />
            </div>
            
            <div className="space-y-2 text-right">
              <label htmlFor="password" className="block font-medium">
                كلمة المرور
              </label>
              <Input
                id="password"
                type="password"
                placeholder="********"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="text-right"
                dir="rtl"
              />
            </div>
            
            <div className="space-y-2 text-right">
              <label htmlFor="confirmPassword" className="block font-medium">
                تأكيد كلمة المرور
              </label>
              <Input
                id="confirmPassword"
                type="password"
                placeholder="********"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="text-right"
                dir="rtl"
              />
            </div>
            
            <Button
              type="submit"
              className="w-full bg-[#9C3D54] hover:bg-[#7d314a] h-12 text-lg mt-6"
              disabled={isLoading}
            >
              {isLoading ? "جاري إنشاء الحساب..." : "إنشاء حساب"}
            </Button>
          </form>
          
          <div className="mt-6 text-center">
            <p className="text-gray-600">
              لديك حساب بالفعل؟{" "}
              <Link to="/login" className="text-[#9C3D54] font-medium hover:underline">
                تسجيل الدخول
              </Link>
            </p>
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Signup;
