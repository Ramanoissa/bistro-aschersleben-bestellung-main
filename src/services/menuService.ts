// Menu data structure for Bistro Aschersleben

export interface MenuItem {
  id: string;
  name: string;
  description: string;
  price: number | PriceBySize;
  allergene?: string;
  category: string;
  imageUrl?: string;
}

export interface PriceBySize {
  small?: number;
  medium?: number;
  large?: number;
}

export interface Category {
  id: string;
  name: string;
  imageUrl: string;
}

// Categories
export const categories: Category[] = [
  { 
    id: "drehspiess", 
    name: "Drehspieß", 
    imageUrl: "https://images.unsplash.com/photo-1633321088355-d0f81824a775?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "salate", 
    name: "Salate", 
    imageUrl: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "pizza", 
    name: "Pizza", 
    imageUrl: "https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "nudel", 
    name: "Nudeln", 
    imageUrl: "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "deutsch", 
    name: "Deutsche Küche", 
    imageUrl: "https://images.unsplash.com/photo-1600891964092-4316c288032e?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "burger", 
    name: "Burger", 
    imageUrl: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1398&auto=format&fit=crop" 
  },
  { 
    id: "kinder", 
    name: "Kinder Menü", 
    imageUrl: "https://images.unsplash.com/photo-1577303935007-0d306ee638cf?q=80&w=1470&auto=format&fit=crop" 
  },
  { 
    id: "getraenke", 
    name: "Getränke", 
    imageUrl: "https://images.unsplash.com/photo-1544145945-f90425340c7e?q=80&w=1374&auto=format&fit=crop" 
  }
];

// Menu items
export const menuItems: MenuItem[] = [
  // Drehspieß Gerichte
  {
    id: "1",
    name: "Drehspieß",
    description: "mit Fleisch, Salat & Soßen im Fladenbrot",
    price: 7.00,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://images.unsplash.com/photo-1610548806955-d9a8165fa6ce?q=80&w=1374&auto=format&fit=crop"
  },
  {
    id: "2",
    name: "Drehspieß nur Fleisch",
    description: "mit Fleisch & Soßen im Fladenbrot",
    price: 7.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://images.unsplash.com/photo-1527851095886-0c800325e84a?q=80&w=1470&auto=format&fit=crop"
  },
  {
    id: "3",
    name: "Käse Drehspieß",
    description: "mit Fleisch, Käse, Salat & Soßen im Fladenbrot",
    price: 7.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://images.unsplash.com/photo-1618160702438-9b02ab6515c9?q=80&w=1470&auto=format&fit=crop"
  },
  {
    id: "4",
    name: "Halumi Drehspieß",
    description: "mit Fleisch, Halumi, Salat & Soßen im Fladenbrot",
    price: 8.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/halumi-drehspiess.jpg"
  },
  {
    id: "5",
    name: "Hawaii Drehspieß",
    description: "mit Fleisch, Käse, Salat & Soßen im Fladenbrot",
    price: 7.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/hawaii-drehspiess.jpg"
  },
  {
    id: "6",
    name: "Mega Drehspieß",
    description: "mit Fleisch & Käse, Salat & Soßen im Fladenbrot",
    price: 7.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/mega-drehspiess.jpg"
  },
  {
    id: "7",
    name: "Big Fam Drehspieß",
    description: "mit Fleisch & Käse im Fladenbrot",
    price: 13.00,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/big-fam-drehspiess.jpg"
  },
  {
    id: "8",
    name: "Pomm Drehspieß",
    description: "mit Fleisch & Pommes im Fladenbrot",
    price: 8.00,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/pomm-drehspiess.jpg"
  },
  {
    id: "9",
    name: "Drehspieß Teller klein",
    description: "mit Fleisch, Salat, Soßen & Pommes",
    price: 9.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/drehspiess-teller-klein.jpg"
  },
  {
    id: "10",
    name: "Drehspieß Teller groß",
    description: "Mit Fleisch, Salat, Soßen & Pommes",
    price: 10.50,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/drehspiess-teller-gross.jpg"
  },
  
  // Weitere Drehspieß-Gerichte
  {
    id: "11",
    name: "Box",
    description: "mit Pommes, Fleisch & Soßen",
    price: 8.00,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/box-drehspiess.jpg"
  },
  {
    id: "12",
    name: "Drehspieß Dürüm",
    description: "mit Fleisch, Salat & Soßen in der Teigrolle",
    price: 8.00,
    allergene: "4, A, C, F, J, K, L",
    category: "drehspiess",
    imageUrl: "https://example.com/drehspiess-durum.jpg"
  },
  {
    id: "13",
    name: "Lahmacun mit Salat",
    description: "mit Salat, Käse & Soßen",
    price: 7.00,
    allergene: "A, C, F, J, K, L",
    category: "drehspiess",
    imageUrl: "https://example.com/lahmacun-salat.jpg"
  },
  {
    id: "14",
    name: "Lahmacun Drehspieß",
    description: "mit Fleisch, Salat & Soßen",
    price: 8.00,
    allergene: "4, A, C, F, J, K, i",
    category: "drehspiess",
    imageUrl: "https://example.com/lahmacun-drehspiess.jpg"
  },
  
  // Salate & Vegetarische Gerichte
  {
    id: "15",
    name: "Dürüm Vegetarisch",
    description: "mit Salat, Käse & Soßen in der Teigrolle",
    price: 7.00,
    allergene: "A, C, F, J, K, L",
    category: "salate",
    imageUrl: "https://images.unsplash.com/photo-1540420773420-3366772f4999?q=80&w=1384&auto=format&fit=crop"
  },
  {
    id: "16",
    name: "Vegetarischer Döner",
    description: "im Fladenbrot mit Käse, Salat & Soßen",
    price: 6.50,
    allergene: "A, C, F, J, K, L",
    category: "salate",
    imageUrl: "https://images.unsplash.com/photo-1551248429-40975aa4de74?q=80&w=1590&auto=format&fit=crop"
  },
  {
    id: "17",
    name: "Falafel Dürüm",
    description: "mit Falafel, Salat & Soßen in der Teigrolle",
    price: 7.50,
    allergene: "k, 4, 5, 6",
    category: "salate",
    imageUrl: "https://example.com/falafel-durum.jpg"
  },
  {
    id: "18",
    name: "Falafel Teller",
    description: "mit Salat, 10 Falafel & Soßen",
    price: 8.50,
    allergene: "k, 4, 5, 6",
    category: "salate",
    imageUrl: "https://example.com/falafel-teller.jpg"
  },
  {
    id: "19",
    name: "Gemischter Salat",
    description: "mit Soßen",
    price: 6.50,
    category: "salate",
    imageUrl: "https://example.com/gemischter-salat.jpg"
  },
  {
    id: "20",
    name: "Käse Salat",
    description: "Gemischter Salat mit Soßen & Käse",
    price: 7.00,
    category: "salate",
    imageUrl: "https://example.com/kaese-salat.jpg"
  },
  {
    id: "21",
    name: "Hawaii Salat",
    description: "gemischter Salat mit Vorderschinken, Mais, Ananas & Soßen",
    price: 8.00,
    allergene: "k, 4, 5, 6",
    category: "salate",
    imageUrl: "https://example.com/hawaii-salat.jpg"
  },
  {
    id: "22",
    name: "Thunfisch Salat",
    description: "gemischter Salat mit Thunfisch & Soßen",
    price: 8.00,
    allergene: "D",
    category: "salate",
    imageUrl: "https://example.com/thunfisch-salat.jpg"
  },
  {
    id: "23",
    name: "Halumi Salat",
    description: "gemischter Salat mit Soßen & Halumi",
    price: 8.50,
    category: "salate",
    imageUrl: "https://example.com/halumi-salat.jpg"
  },
  {
    id: "24",
    name: "Mediterran Salat",
    description: "gemischter Salat mit Vorderschinken, Peperoni & Oliven",
    price: 8.50,
    allergene: "4,5,6",
    category: "salate",
    imageUrl: "https://example.com/mediterran-salat.jpg"
  },
  {
    id: "25",
    name: "Drehspieß Salat",
    description: "gemischter Salat mit Drehspieß oder Hähnchenfleisch & Soßen",
    price: 8.50,
    allergene: "i",
    category: "salate",
    imageUrl: "https://example.com/drehspiess-salat.jpg"
  },
  
  // Pizza (repräsentative Auswahl)
  {
    id: "26",
    name: "Margherita",
    description: "mit Tomatensoßen & Käse",
    price: {
      small: 7.50,
      medium: 8.50, 
      large: 15.50
    },
    allergene: "A, G, L",
    category: "pizza",
    imageUrl: "https://images.unsplash.com/photo-1598023696416-0193a0bcd302?q=80&w=1472&auto=format&fit=crop"
  },
  {
    id: "27",
    name: "Salami",
    description: "mit Salami",
    price: {
      small: 8.00,
      medium: 9.50, 
      large: 17.00
    },
    allergene: "A, G, L, 4, 5, 6",
    category: "pizza",
    imageUrl: "https://images.unsplash.com/photo-1506354666786-959d6d497f1a?q=80&w=1470&auto=format&fit=crop"
  },
  {
    id: "30",
    name: "Hawaii",
    description: "mit Vorderschinken & Ananas",
    price: {
      small: 8.50,
      medium: 10.00, 
      large: 19.00
    },
    allergene: "A, G, L, 4, 5, 6",
    category: "pizza",
    imageUrl: "https://example.com/pizza-hawaii.jpg"
  },
  {
    id: "41",
    name: "Drehspieß Pizza",
    description: "mit Drehspießfleisch & Zwiebeln",
    price: {
      small: 9.00,
      medium: 10.50, 
      large: 19.50
    },
    allergene: "4, A, C, F, J, K, i",
    category: "pizza",
    imageUrl: "https://example.com/pizza-drehspiess.jpg"
  },
  
  // Nudelgerichte (repräsentative Auswahl)
  {
    id: "58",
    name: "Rigatoni Napoli",
    description: "mit Tomaten- oder Sahnesoßen",
    price: 8.00,
    allergene: "C, G, 3, L",
    category: "nudel",
    imageUrl: "https://images.unsplash.com/photo-1608897013039-887f21d8c804?q=80&w=1392&auto=format&fit=crop"
  },
  {
    id: "59",
    name: "Rigatoni Bolognese",
    description: "mit Hackfleischsoßen",
    price: 8.50,
    allergene: "C, G, 3, L",
    category: "nudel",
    imageUrl: "https://example.com/rigatoni-bolognese.jpg"
  },
  {
    id: "71",
    name: "Drehspieß Broccoli",
    description: "mit Drehspieß der Hähnchenfleisch, Broccoli & Sahnesoße",
    price: 9.50,
    allergene: "A, C, G, L, 3, 4, 5, 6",
    category: "nudel",
    imageUrl: "https://example.com/nudel-drehspiess-broccoli.jpg"
  },
  
  // Deutsche Küche (repräsentative Auswahl)
  {
    id: "75",
    name: "Rahmschnitzel",
    description: "mit Rahmsoße, Pommes & Salat",
    price: 10.00,
    allergene: "A, C, G, J",
    category: "deutsch",
    imageUrl: "https://images.unsplash.com/photo-1599921841143-819065a55cc6?q=80&w=1631&auto=format&fit=crop"
  },
  {
    id: "78",
    name: "Jägerschnitzel",
    description: "mit Jägersoße, Pommes & Salat",
    price: 10.00,
    allergene: "A, C, G, J",
    category: "deutsch",
    imageUrl: "https://example.com/jaegerschnitzel.jpg"
  },
  {
    id: "87",
    name: "Currywurst",
    description: "mit Pommes & Salat",
    price: 9.50,
    allergene: "C, G, J",
    category: "deutsch",
    imageUrl: "https://example.com/currywurst.jpg"
  },
  
  // Burger (repräsentative Auswahl)
  {
    id: "90",
    name: "Hamburger XXXL",
    description: "mit Eisberg, Tomaten & Zwiebeln",
    price: 7.50,
    allergene: "A, G",
    category: "burger",
    imageUrl: "https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=1530&auto=format&fit=crop"
  },
  {
    id: "91",
    name: "Cheeseburger XXXL",
    description: "mit Eisberg, Tomaten & Zwiebeln",
    price: 8.00,
    allergene: "A, G",
    category: "burger",
    imageUrl: "https://example.com/cheeseburger.jpg"
  },
  {
    id: "92",
    name: "Crispyburger XXXL",
    description: "mit Eisberg, Tomaten & Zwiebeln",
    price: 9.00,
    allergene: "A, G",
    category: "burger",
    imageUrl: "https://example.com/crispyburger.jpg"
  },
  
  // Kinder Menü
  {
    id: "97",
    name: "KiddsMenu mit Nuggets",
    description: "mit Nuggets, Pommes, Lutscher, Luftballon, Getränk & Überraschung",
    price: 8.00,
    category: "kinder",
    imageUrl: "https://images.unsplash.com/photo-1457301353672-324d6d14f471?q=80&w=1476&auto=format&fit=crop"
  },
  {
    id: "98",
    name: "KiddsMenu mit Dönerfleisch",
    description: "mit Dönerfleisch, Pommes, Lutscher, Luftballon, Getränk & Überraschung",
    price: 8.00,
    category: "kinder",
    imageUrl: "https://example.com/kiddsmenu-doener.jpg"
  },
  
  // Getränke
  {
    id: "104",
    name: "Coca-Cola",
    description: "0,33l",
    price: 2.00,
    allergene: "1, 2",
    category: "getraenke",
    imageUrl: "https://images.unsplash.com/photo-1581636625402-29b2a704ef13?q=80&w=1528&auto=format&fit=crop"
  },
  {
    id: "105",
    name: "Fanta",
    description: "0,33l",
    price: 2.00,
    allergene: "1, 5",
    category: "getraenke",
    imageUrl: "https://example.com/fanta.jpg"
  },
  {
    id: "106",
    name: "Red Bull",
    description: "0,25l",
    price: 2.50,
    allergene: "1, 2",
    category: "getraenke",
    imageUrl: "https://example.com/red-bull.jpg"
  }
];

// Get menu items by category
export const getMenuItemsByCategory = (categoryId: string): MenuItem[] => {
  return menuItems.filter(item => item.category === categoryId);
};

// Get all menu items
export const getAllMenuItems = (): MenuItem[] => {
  return menuItems;
};

// Get specific menu item by id
export const getMenuItemById = (id: string): MenuItem | undefined => {
  return menuItems.find(item => item.id === id);
};
