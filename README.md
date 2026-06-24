# 🏪 Sistema de Gestión Minimarket

Sistema web completo para administrar un minimarket: inventario, ventas (POS), caja, fiados, reportes, costos y carga masiva de inventario leyendo facturas electrónicas SII (PDF).

## Módulos

- **Dashboard** — ventas del día, utilidad, stock bajo, top productos, gráfico 7 días.
- **Punto de venta (POS)** — búsqueda por nombre o código de barras (compatible con lector), carrito, métodos de pago (efectivo, débito, crédito, transferencia, fiado).
- **Inventario** — productos con costo, precio, margen, stock, stock mínimo, categorías.
- **Facturas / Carga masiva** — sube PDFs de facturas SII; el sistema extrae los productos (XML embebido del DTE o texto) y actualiza el inventario tras tu revisión.
- **Fiados** — clientes, deuda por cobrar, historial de compras y abonos.
- **Caja** — apertura con monto inicial, movimientos de ingreso/egreso, cierre con conteo físico y arqueo (esperado vs real).
- **Reportes** — por rango de fechas: ventas, costo, utilidad bruta, ventas por método de pago, productos más vendidos.
- **Usuarios** — perfiles **administrador** y **vendedor común** con permisos diferenciados.

## Roles

| Función | Vendedor | Administrador |
|---|---|---|
| POS / vender | ✅ | ✅ |
| Ver ventas y caja | ✅ | ✅ |
| Fiados y abonos | ✅ | ✅ |
| Crear/editar productos | ❌ | ✅ |
| Cargar facturas | ❌ | ✅ |
| Reportes | ❌ | ✅ |
| Gestionar usuarios | ❌ | ✅ |

## Uso local

```bash
pip install -r requirements.txt
python app.py
```

Abre http://localhost:5000

**Usuarios demo:** `admin / admin123` · `vendedor / vend123`
(cambia estas contraseñas en Usuarios apenas entres).

## Despliegue en la nube (acceso remoto)

### Opción A — Render (gratis, recomendado)
1. Sube esta carpeta a un repositorio de GitHub.
2. En [render.com](https://render.com) → New → Blueprint → conecta el repo.
   El archivo `render.yaml` lo configura automáticamente.
3. Listo: tendrás una URL pública `https://minimarket-xxxx.onrender.com`.

> Nota: en plan gratuito de Render, SQLite se reinicia en cada deploy. Para datos
> persistentes, agrega un disco persistente o cambia a PostgreSQL definiendo la
> variable `DATABASE_URL` (la app ya la lee).

### Opción B — Railway / Fly.io / cualquier host con Procfile
El `Procfile` ya define `gunicorn wsgi:app`.

### Variables de entorno
- `SECRET_KEY` — clave de sesión (obligatoria en producción).
- `DATABASE_URL` — opcional; usa PostgreSQL si la defines, ej:
  `postgresql://usuario:pass@host:5432/minimarket`

## Carga de facturas — cómo funciona

1. Ve a **Facturas / Carga** y sube uno o varios PDF.
2. El parser intenta, en orden:
   - Leer el **XML DTE embebido** en el PDF (factura electrónica SII) → máxima precisión.
   - Leer XML inline en el texto.
   - **Heurística de texto** (factura impresa / escaneada con texto).
3. Revisa la pantalla de extracción: por cada ítem decides **sumar a existente**,
   **crear nuevo** o **ignorar**, ajustas costo y precio de venta.
4. Confirmas y el inventario se actualiza (suma stock, actualiza costos).

## Stack

Flask · SQLAlchemy · SQLite (o PostgreSQL) · pdfplumber + pikepdf para lectura de PDF · Chart.js.

## Estructura

```
app.py              rutas y lógica
models.py           modelos de base de datos
factura_parser.py   lectura de facturas SII (PDF)
templates/          vistas HTML
wsgi.py / Procfile  despliegue
```
