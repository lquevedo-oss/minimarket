"""
Carga masiva de productos de prueba.
Ejecutar en Render Shell: python seed_test.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import Categoria, Producto

CATS_EXTRA = ["Alcoholes", "Pastas y Fideos", "Conservas", "Jugos y Bebidas", "Panadería"]

# (nombre, categoría, unidad, costo, precio, stock, stock_min)
PRODUCTOS = [
    # ── Alcoholes ──────────────────────────────────────────────────────
    ("Cerveza Cristal Lata 500ml",          "Alcoholes", "un",     750,  990, 48, 6),
    ("Cerveza Escudo Botella 1L",            "Alcoholes", "un",    1100, 1490, 36, 6),
    ("Cerveza Corona 355ml",                 "Alcoholes", "un",    1200, 1590, 24, 4),
    ("Cerveza Heineken 330ml",               "Alcoholes", "un",    1400, 1890, 18, 4),
    ("Cerveza Kunstmann Torobayo 500ml",     "Alcoholes", "un",    1800, 2390, 12, 3),
    ("Cerveza Austral Calafate 330ml",       "Alcoholes", "un",    1600, 2190, 12, 3),
    ("Cerveza Cusqueña 330ml",               "Alcoholes", "un",    1500, 1990, 12, 3),
    ("Sidra El Vergel 1L",                   "Alcoholes", "un",    2200, 2890,  8, 2),
    ("Vino Gato Cabernet 1L",               "Alcoholes", "un",    2800, 3690, 24, 4),
    ("Vino Gato Blanco 1L",                 "Alcoholes", "un",    2800, 3690, 18, 4),
    ("Vino Frontera Tinto 750ml",           "Alcoholes", "un",    3200, 4290, 12, 3),
    ("Vino Cono Sur Bicicleta 750ml",       "Alcoholes", "un",    4200, 5490,  8, 2),
    ("Vino Casillero del Diablo 750ml",     "Alcoholes", "un",    5500, 7290,  6, 2),
    ("Pisco Control Especial 750ml",         "Alcoholes", "un",    5500, 7290,  8, 2),
    ("Pisco Los Andes 750ml",               "Alcoholes", "un",    4200, 5590,  6, 2),
    ("Ron Flor de Caña 750ml",              "Alcoholes", "un",    8500,10990,  3, 2),
    ("Vodka Absolut 750ml",                 "Alcoholes", "un",    9000,11990,  3, 1),
    ("Whisky Old Times 750ml",              "Alcoholes", "un",    6500, 8590,  2, 2),  # ← stock bajo
    ("Baileys Irish Cream 700ml",           "Alcoholes", "un",   12000,15990,  2, 2),  # ← stock bajo

    # ── Pastas y Fideos ────────────────────────────────────────────────
    ("Fideos Carozzi Spaghetti 500g",       "Pastas y Fideos", "un",  650,  890, 60, 10),
    ("Fideos Carozzi Tallarín 500g",        "Pastas y Fideos", "un",  650,  890, 48, 10),
    ("Fideos Carozzi Corbata 500g",         "Pastas y Fideos", "un",  680,  890, 24,  6),
    ("Fideos Carozzi Codo 500g",            "Pastas y Fideos", "un",  680,  890, 24,  6),
    ("Fideos Don Vittorio Spaghetti 400g",  "Pastas y Fideos", "un",  590,  790, 36,  8),
    ("Fideos Don Vittorio Penne 400g",      "Pastas y Fideos", "un",  590,  790, 30,  8),
    ("Fideos San Remo Lasagna 250g",        "Pastas y Fideos", "un",  890, 1190, 12,  4),
    ("Fideos Instantáneos Yatekomo Pollo",  "Pastas y Fideos", "un",  350,  490, 48,  8),
    ("Fideos Instantáneos Yatekomo Res",    "Pastas y Fideos", "un",  350,  490, 36,  8),
    ("Fideos Instantáneos Yatekomo Marisco","Pastas y Fideos", "un",  380,  490,  3,  8),  # ← stock bajo

    # ── Abarrotes ──────────────────────────────────────────────────────
    ("Arroz Doña Rosa 1kg",                 "Abarrotes", "un",  1100, 1490, 80, 15),
    ("Arroz SOS 1kg",                       "Abarrotes", "un",  1200, 1590, 60, 12),
    ("Azúcar Iansa 1kg",                    "Abarrotes", "un",   890, 1190, 50, 10),
    ("Azúcar Iansa 2kg",                    "Abarrotes", "un",  1690, 2190, 30,  6),
    ("Aceite Cuisine & Co 1L",              "Abarrotes", "un",  2400, 3190, 36,  6),
    ("Aceite Chef 1L",                      "Abarrotes", "un",  2200, 2890, 24,  5),
    ("Sal Lobos 1kg",                       "Abarrotes", "un",   290,  390, 40,  8),
    ("Harina Selecta 1kg",                  "Abarrotes", "un",   790, 1090, 30,  6),
    ("Harina Selecta 2kg",                  "Abarrotes", "un",  1490, 1990, 18,  4),
    ("Milo 400g",                           "Abarrotes", "un",  2800, 3690, 12,  3),
    ("Nescafé Classic 170g",                "Abarrotes", "un",  3200, 4290, 12,  3),
    ("Nescafé Tarro 200g",                  "Abarrotes", "un",  3800, 4990,  4,  4),  # ← stock bajo
    ("Té Supremo 100 bolsitas",             "Abarrotes", "un",  1200, 1590, 18,  4),
    ("Café Presto 170g",                    "Abarrotes", "un",  2400, 3190,  6,  3),
    ("Maicena Carozzi 200g",                "Abarrotes", "un",   490,  690, 20,  4),
    ("Vinagre Cuisine & Co 500ml",          "Abarrotes", "un",   490,  690, 15,  3),
    ("Salsa de Tomate Carozzi 200g",        "Abarrotes", "un",   590,  790, 24,  5),

    # ── Lácteos ────────────────────────────────────────────────────────
    ("Leche Soprole Entera 1L",             "Lácteos", "un",   990, 1290, 60, 10),
    ("Leche Loncoleche 1L",                 "Lácteos", "un",   950, 1290, 48, 10),
    ("Leche Descremada Soprole 1L",         "Lácteos", "un",  1050, 1390, 24,  6),
    ("Leche Condensada Nestlé 397g",        "Lácteos", "un",  1400, 1890, 12,  3),
    ("Mantequilla Soprole 200g",            "Lácteos", "un",  1400, 1890, 24,  5),
    ("Mantequilla President 200g",          "Lácteos", "un",  1600, 2190, 12,  3),
    ("Crema Soprole 200ml",                 "Lácteos", "un",  1200, 1590, 18,  4),
    ("Yogurt Yoplait Frutilla 165g",        "Lácteos", "un",   390,  590, 36,  8),
    ("Yogurt Colun Natural 1kg",            "Lácteos", "un",  1800, 2390, 12,  4),
    ("Queso Gauda Colun 200g",             "Lácteos", "un",  1600, 2190, 18,  4),
    ("Queso Mantecoso Colun 200g",         "Lácteos", "un",  1500, 1990,  3,  4),  # ← stock bajo
    ("Quesillo Colun 240g",                "Lácteos", "un",  1200, 1590,  8,  3),

    # ── Conservas ──────────────────────────────────────────────────────
    ("Atún Real 170g",                      "Conservas", "un",   890, 1190, 48,  8),
    ("Atún Cuisine & Co 80g",               "Conservas", "un",   590,  790, 60, 10),
    ("Tomate Perita La Cocinera 400g",      "Conservas", "un",   590,  790, 36,  6),
    ("Tomate Triturado Cuisine & Co 400g",  "Conservas", "un",   550,  750, 30,  6),
    ("Choclo en Lata Cuisine & Co 400g",    "Conservas", "un",   590,  790, 24,  5),
    ("Arvejas Cuisine & Co 300g",           "Conservas", "un",   550,  750, 18,  4),
    ("Sardinas Colo Colo 120g",             "Conservas", "un",   590,  790, 24,  5),
    ("Espárragos Cuisine & Co 325g",        "Conservas", "un",  1200, 1590,  4,  4),  # ← stock bajo
    ("Champiñones en Lata 400g",            "Conservas", "un",   890, 1190, 12,  3),

    # ── Jugos y Bebidas ────────────────────────────────────────────────
    ("Coca-Cola 1.5L",                      "Jugos y Bebidas", "un",   990, 1290, 60, 10),
    ("Coca-Cola 500ml",                     "Jugos y Bebidas", "un",   650,  890, 72, 12),
    ("Pepsi 1.5L",                          "Jugos y Bebidas", "un",   890, 1190, 36,  8),
    ("Fanta Naranja 500ml",                 "Jugos y Bebidas", "un",   650,  890, 36,  8),
    ("Sprite 500ml",                        "Jugos y Bebidas", "un",   650,  890, 36,  8),
    ("Agua Mineral Cachantun 1.5L",         "Jugos y Bebidas", "un",   490,  690, 48, 10),
    ("Agua Mineral Cachantun 500ml",        "Jugos y Bebidas", "un",   290,  390, 60, 12),
    ("Jugo Andina 1L Naranja",              "Jugos y Bebidas", "un",   790, 1090, 24,  6),
    ("Jugo Andina 1L Manzana",              "Jugos y Bebidas", "un",   790, 1090, 18,  5),
    ("Jugo Watt's 1L Durazno",              "Jugos y Bebidas", "un",   850, 1190, 18,  5),
    ("Néctar Watt's 200ml Piña",            "Jugos y Bebidas", "un",   290,  390, 48, 10),
    ("Red Bull 250ml",                      "Jugos y Bebidas", "un",  1400, 1890, 18,  4),
    ("Monster Energy 500ml",               "Jugos y Bebidas", "un",  1600, 2190,  4,  4),  # ← stock bajo
    ("Bebida Terma 500ml",                  "Jugos y Bebidas", "un",   790, 1090, 12,  3),
    ("Gatorade Limón 500ml",               "Jugos y Bebidas", "un",   950, 1290, 12,  3),

    # ── Snacks ─────────────────────────────────────────────────────────
    ("Papas Fritas Lays Natural 180g",      "Snacks", "un",  1200, 1590, 30,  6),
    ("Papas Fritas Lays BBQ 180g",         "Snacks", "un",  1200, 1590, 24,  6),
    ("Papas Fritas Pringles Original 124g", "Snacks", "un",  1800, 2390, 18,  4),
    ("Galletas Oreo 119g",                  "Snacks", "un",   890, 1190, 36,  8),
    ("Galletas Tritón 210g",               "Snacks", "un",   650,  890, 30,  6),
    ("Galletas Soda Carozzi 215g",         "Snacks", "un",   590,  790, 24,  5),
    ("Maní Tostado 500g",                  "Snacks", "un",   990, 1390, 18,  4),
    ("Almendras Tostadas 100g",            "Snacks", "un",  1400, 1890, 12,  3),
    ("Chocolate Sahne Nuss 150g",          "Snacks", "un",  1600, 2190, 12,  3),
    ("Chocolate Super 8 300g",             "Snacks", "un",  1800, 2390, 12,  3),
    ("Caramelos Mentos Menta",             "Snacks", "un",   290,  390, 48, 10),
    ("Chicle Trident Menta 14g",           "Snacks", "un",   390,  590, 36,  8),

    # ── Aseo ───────────────────────────────────────────────────────────
    ("Detergente Bold 800g",               "Aseo", "un",  2400, 3190, 18,  4),
    ("Detergente Omo 800g",                "Aseo", "un",  2600, 3490, 12,  3),
    ("Jabón Dove 90g",                     "Aseo", "un",   890, 1190, 24,  5),
    ("Jabón Lux 90g",                      "Aseo", "un",   590,  790, 36,  8),
    ("Shampoo Head & Shoulders 375ml",     "Aseo", "un",  3200, 4290,  6,  2),
    ("Shampoo Pantene 400ml",              "Aseo", "un",  3500, 4590,  2,  3),  # ← stock bajo
    ("Papel Higiénico Elite Pack x4",      "Aseo", "un",  1400, 1890, 24,  5),
    ("Toallas Nova Pack x100",             "Aseo", "un",  1200, 1590, 18,  4),
    ("Desodorante Rexona 150ml",           "Aseo", "un",  2800, 3690,  8,  3),
    ("Pasta Dental Colgate 90g",           "Aseo", "un",  1200, 1590, 12,  3),

    # ── Cigarros ───────────────────────────────────────────────────────
    ("Cigarrillos Marlboro x20",           "Cigarros", "cajita", 2800, 3490, 30,  5),
    ("Cigarrillos Belmont x20",            "Cigarros", "cajita", 2400, 2990, 24,  5),
    ("Cigarrillos Camel x20",              "Cigarros", "cajita", 2600, 3290, 18,  4),
    ("Cigarrillos Lucky Strike x20",       "Cigarros", "cajita", 2500, 3190,  3,  4),  # ← stock bajo
    ("Cigarrillos Viceroy x20",            "Cigarros", "cajita", 2200, 2790, 12,  3),

    # ── Panadería ──────────────────────────────────────────────────────
    ("Pan Molde Bimbo 500g",               "Panadería", "un",  1200, 1590, 12,  3),
    ("Pan Molde Ideal 500g",               "Panadería", "un",  1100, 1490, 12,  3),
    ("Pan de Hamburguesa x6",              "Panadería", "un",  1400, 1890,  8,  2),
    ("Pan Pita x4",                        "Panadería", "un",   890, 1190,  8,  2),
    ("Hallullas x6",                       "Panadería", "un",   790, 1090,  1,  3),  # ← stock bajo
]

with app.app_context():
    # Crear categorías extras
    for nombre in CATS_EXTRA:
        if not Categoria.query.filter_by(nombre=nombre).first():
            db.session.add(Categoria(nombre=nombre))
    db.session.commit()

    # Insertar productos (evita duplicados)
    n = 0
    for nombre, cat_nombre, unidad, costo, precio, stock, stock_min in PRODUCTOS:
        if Producto.query.filter_by(nombre=nombre).first():
            continue
        cat = Categoria.query.filter_by(nombre=cat_nombre).first()
        db.session.add(Producto(
            nombre=nombre,
            categoria_id=cat.id if cat else None,
            unidad=unidad, costo=costo, precio=precio,
            stock=stock, stock_min=stock_min,
        ))
        n += 1
    db.session.commit()
    print(f"✓ {n} productos cargados correctamente.")
    total = Producto.query.filter_by(activo=True).count()
    print(f"  Total productos en BD: {total}")
