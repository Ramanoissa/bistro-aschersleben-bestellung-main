
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Link } from "react-router-dom";

const Index = () => {
  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col items-center">
      {/* Header */}
      <header className="w-full bg-[#9C3D54] text-white p-4 flex justify-center">
        <h1 className="text-2xl font-bold text-center">Bistro Aschersleben</h1>
      </header>
      
      {/* Logo Section */}
      <div className="mt-8 mb-6 flex justify-center">
        <div className="w-40 h-40 bg-white rounded-full flex items-center justify-center">
          <span className="text-[#9C3D54] text-3xl font-bold">BA</span>
        </div>
      </div>
      
      {/* Welcome Text */}
      <div className="text-center px-4 mb-8">
        <h2 className="text-xl font-bold mb-2">Willkommen bei Bistro Aschersleben</h2>
        <p className="text-gray-600">Genießen Sie köstliches Essen mit schnellem Lieferservice</p>
      </div>
      
      {/* Features Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 px-4 max-w-md mb-8">
        <Link to="/menu" className="block">
          <Card className="p-4 border-2 border-[#9C3D54] hover:bg-gray-50 transition-colors">
            <div className="flex flex-col items-center">
              <span className="text-2xl mb-2">🍕</span>
              <h3 className="font-bold text-center">Speisekarte</h3>
            </div>
          </Card>
        </Link>
        
        <Card className="p-4 border-2 border-[#9C3D54]">
          <div className="flex flex-col items-center">
            <span className="text-2xl mb-2">🛵</span>
            <h3 className="font-bold text-center">Lieferservice</h3>
          </div>
        </Card>
        
        <Card className="p-4 border-2 border-[#9C3D54]">
          <div className="flex flex-col items-center">
            <span className="text-2xl mb-2">💳</span>
            <h3 className="font-bold text-center">Online Bezahlen</h3>
          </div>
        </Card>
        
        <Link to="/profile" className="block">
          <Card className="p-4 border-2 border-[#9C3D54] hover:bg-gray-50 transition-colors">
            <div className="flex flex-col items-center">
              <span className="text-2xl mb-2">👤</span>
              <h3 className="font-bold text-center">Kundenkonto</h3>
            </div>
          </Card>
        </Link>
      </div>
      
      {/* Restaurant Info */}
      <div className="bg-white p-4 rounded-lg shadow-sm w-full max-w-md mx-4 mb-8">
        <h3 className="font-bold text-center mb-2">Öffnungszeiten</h3>
        <div className="text-center text-sm space-y-1">
          <p>Mo–Sa: 10:00 - 21:30 Uhr</p>
          <p>So: 12:00 - 21:30 Uhr</p>
          <p className="mt-2 font-medium">📞 03473-2259144</p>
          <p>📍 Carl von Ossietzky Platz 1, 06449 Aschersleben</p>
        </div>
      </div>
      
      {/* Action Buttons */}
      <div className="flex flex-col gap-3 w-full max-w-xs px-4 mb-8">
        <Button className="bg-[#9C3D54] hover:bg-[#7d314a] text-lg h-12" asChild>
          <Link to="/menu">Speisekarte ansehen</Link>
        </Button>
        
        <Button variant="outline" className="border-[#9C3D54] text-[#9C3D54] hover:bg-[#9C3D54] hover:text-white text-lg h-12" asChild>
          <Link to="/login">Anmelden</Link>
        </Button>
      </div>
      
      {/* Footer */}
      <footer className="w-full bg-gray-100 p-4 mt-auto">
        <p className="text-center text-sm text-gray-600">
          © 2025 Bistro Aschersleben - Alle Rechte vorbehalten
        </p>
      </footer>
    </div>
  );
};

export default Index;
