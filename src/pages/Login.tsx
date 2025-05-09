
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { ArrowLeft } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!email || !password) {
      toast({
        title: "خطأ",
        description: "الرجاء إدخال البريد الإلكتروني وكلمة المرور",
        variant: "destructive",
      });
      return;
    }
    
    setIsLoading(true);
    
    // Simulate authentication
    setTimeout(() => {
      setIsLoading(false);
      toast({
        title: "تم تسجيل الدخول بنجاح",
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
        <h1 className="text-xl font-bold text-center">تسجيل الدخول</h1>
        <Link to="/">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      {/* Login Form */}
      <div className="flex-1 p-4 flex flex-col justify-center">
        <Card className="p-6 max-w-md mx-auto w-full">
          <form onSubmit={handleSubmit} className="space-y-6">
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
            
            <div className="text-left">
              <Link to="/reset-password" className="text-[#9C3D54] text-sm hover:underline">
                نسيت كلمة المرور؟
              </Link>
            </div>
            
            <Button
              type="submit"
              className="w-full bg-[#9C3D54] hover:bg-[#7d314a] h-12 text-lg"
              disabled={isLoading}
            >
              {isLoading ? "جاري تسجيل الدخول..." : "تسجيل الدخول"}
            </Button>
          </form>
          
          <div className="mt-6 text-center">
            <p className="text-gray-600">
              ليس لديك حساب؟{" "}
              <Link to="/signup" className="text-[#9C3D54] font-medium hover:underline">
                إنشاء حساب جديد
              </Link>
            </p>
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Login;
