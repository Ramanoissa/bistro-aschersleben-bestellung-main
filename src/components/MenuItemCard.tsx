
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { MenuItem, PriceBySize } from "@/services/menuService";

interface MenuItemCardProps {
  item: MenuItem;
  onAddToCart: (item: MenuItem) => void;
}

const MenuItemCard = ({ item, onAddToCart }: MenuItemCardProps) => {
  const formatPrice = (price: number | PriceBySize): string => {
    if (typeof price === "number") {
      return `${price.toFixed(2)} €`;
    } else {
      return `${price.small?.toFixed(2) || "-"} € / ${price.medium?.toFixed(2) || "-"} € / ${price.large?.toFixed(2) || "-"} €`;
    }
  };

  return (
    <Card className="overflow-hidden bg-white">
      <CardContent className="p-0">
        <div className="flex border-b p-4">
          <div className="flex-1 text-right">
            <h3 className="font-bold text-lg">{item.name}</h3>
            {item.allergene && (
              <p className="text-xs text-gray-500 mt-0.5">{item.allergene}</p>
            )}
            <p className="text-sm text-gray-600 mt-1">{item.description}</p>
            <div className="mt-2 flex justify-between items-center">
              <Button 
                onClick={() => onAddToCart(item)}
                className="bg-[#9C3D54] hover:bg-[#7d314a]"
              >
                Hinzufügen
              </Button>
              <span className="font-bold">{formatPrice(item.price)}</span>
            </div>
          </div>
          <div className="w-24 h-24 bg-gray-200 ml-4 rounded-md overflow-hidden flex items-center justify-center">
            {item.imageUrl ? (
              <img 
                src={item.imageUrl} 
                alt={item.name} 
                className="w-full h-full object-cover"
              />
            ) : (
              <div className="bg-gray-300 w-full h-full flex items-center justify-center text-gray-500">
                Kein Bild
              </div>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default MenuItemCard;
