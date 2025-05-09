
import { MenuItem } from "./menuService";

export interface CartItem {
  id: string;
  menuItemId: string;
  name: string;
  description: string;
  price: number;
  quantity: number;
  options?: {
    name: string;
    choice: string;
    extraPrice: number;
  }[];
  notes?: string;
}

export interface Cart {
  items: CartItem[];
  totalPrice: number;
  itemCount: number;
}

// Initialize empty cart
let cart: Cart = {
  items: [],
  totalPrice: 0,
  itemCount: 0
};

// Add item to cart
export const addToCart = (menuItem: MenuItem, quantity: number = 1, options?: any[], notes?: string): void => {
  const itemPrice = typeof menuItem.price === 'number' 
    ? menuItem.price 
    : (menuItem.price.small || 0);
    
  const optionsWithPrice = options?.map(option => ({
    name: option.name,
    choice: option.choice,
    extraPrice: option.extraPrice || 0
  })) || [];
  
  const extraPrice = optionsWithPrice.reduce((total, option) => total + option.extraPrice, 0);
  
  const cartItem: CartItem = {
    id: `${menuItem.id}-${Date.now()}`, // Unique ID for the cart item
    menuItemId: menuItem.id,
    name: menuItem.name,
    description: menuItem.description,
    price: itemPrice + extraPrice,
    quantity,
    options: optionsWithPrice,
    notes
  };
  
  cart.items.push(cartItem);
  updateCartTotals();
};

// Remove item from cart
export const removeFromCart = (cartItemId: string): void => {
  cart.items = cart.items.filter(item => item.id !== cartItemId);
  updateCartTotals();
};

// Update item quantity
export const updateItemQuantity = (cartItemId: string, quantity: number): void => {
  const item = cart.items.find(item => item.id === cartItemId);
  if (item) {
    item.quantity = quantity;
    updateCartTotals();
  }
};

// Clear cart
export const clearCart = (): void => {
  cart = {
    items: [],
    totalPrice: 0,
    itemCount: 0
  };
};

// Get cart
export const getCart = (): Cart => {
  return cart;
};

// Update cart totals
const updateCartTotals = (): void => {
  cart.itemCount = cart.items.reduce((count, item) => count + item.quantity, 0);
  cart.totalPrice = cart.items.reduce((total, item) => total + (item.price * item.quantity), 0);
};
