
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowLeft, ShoppingCart } from "lucide-react";
import { Link } from "react-router-dom";
import { useToast } from "@/components/ui/use-toast";
import { categories, getMenuItemsByCategory } from "@/services/menuService";
import { addToCart } from "@/services/cartService";
import MenuItemCard from "@/components/MenuItemCard";

const Menu = () => {
  const [selectedCategory, setSelectedCategory] = useState(categories[0].id);
  const [cartCount, setCartCount] = useState(0);
  const { toast } = useToast();

  const filteredItems = getMenuItemsByCategory(selectedCategory);
  
  const handleAddToCart = (item) => {
    addToCart(item);
    setCartCount(prev => prev + 1);
    toast({
      title: "تمت الإضافة إلى السلة",
      description: `تمت إضافة ${item.name} إلى سلة التسوق`,
    });
  };

  return (
    <div className="min-h-screen bg-[#FFFBF0] flex flex-col">
      {/* Header */}
      <header className="bg-[#9C3D54] text-white p-4 sticky top-0 z-10 flex justify-between items-center">
        <Link to="/cart">
          <div className="relative">
            <ShoppingCart className="h-6 w-6" />
            {cartCount > 0 && (
              <span className="absolute -top-2 -right-2 bg-[#E89005] text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                {cartCount}
              </span>
            )}
          </div>
        </Link>
        <h1 className="text-xl font-bold text-center">Bistro Aschersleben</h1>
        <Link to="/">
          <ArrowLeft className="h-6 w-6" />
        </Link>
      </header>
      
      {/* Categories */}
      <div className="p-4 overflow-x-auto">
        <div className="flex space-x-4 space-x-reverse flex-row-reverse">
          {categories.map(category => (
            <button
              key={category.id}
              className={`flex flex-col items-center px-2 py-1 rounded-lg ${
                selectedCategory === category.id ? "bg-[#9C3D54] text-white" : "bg-white text-[#9C3D54] border border-[#9C3D54]"
              }`}
              onClick={() => setSelectedCategory(category.id)}
            >
              <div className="w-16 h-16 rounded-full overflow-hidden mb-1">
                <img 
                  src={category.imageUrl} 
                  alt={category.name}
                  className="w-full h-full object-cover"
                />
              </div>
              <span className="text-xs whitespace-nowrap">{category.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Menu Items */}
      <div className="flex-1 p-4">
        <h2 className="text-xl font-bold mb-4 text-right">
          {categories.find(c => c.id === selectedCategory)?.name}
        </h2>
        
        <div className="grid grid-cols-1 gap-4">
          {filteredItems.map(item => (
            <MenuItemCard 
              key={item.id} 
              item={item} 
              onAddToCart={handleAddToCart} 
            />
          ))}
        </div>
      </div>

      {/* Restaurant Info */}
      <div className="bg-white p-4 border-t border-gray-200">
        <h3 className="font-bold text-center mb-2">Öffnungszeiten & Lieferzeiten</h3>
        <div className="text-center text-sm space-y-1">
          <p>Mo–Sa: 10:00 - 21:30 Uhr</p>
          <p>So: 12:00 - 21:30 Uhr</p>
          <p>📞 03473-2259144</p>
          <p>📍 Carl von Ossietzky Platz 1, 06449 Aschersleben</p>
        </div>
      </div>

      {/* Navigation Footer */}
      <footer className="bg-white border-t border-gray-200 p-4 sticky bottom-0">
        <div className="flex justify-around">
          <Link to="/profile" className="flex flex-col items-center text-gray-600">
            <span>👤</span>
            <span className="text-xs">Konto</span>
          </Link>
          <Link to="/offers" className="flex flex-col items-center text-gray-600">
            <span>🏷️</span>
            <span className="text-xs">Angebote</span>
          </Link>
          <Link to="/cart" className="flex flex-col items-center text-gray-600">
            <span>🛒</span>
            <span className="text-xs">Warenkorb</span>
          </Link>
          <Link to="/menu" className="flex flex-col items-center text-[#9C3D54]">
            <span>🍔</span>
            <span className="text-xs">Speisekarte</span>
          </Link>
        </div>
      </footer>
    </div>
  );
};

export default Menu;
