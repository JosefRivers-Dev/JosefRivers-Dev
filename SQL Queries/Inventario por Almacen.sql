-- Nombre: Inventario por Ubicacion

SELECT o.ItemCode, o.ItemName, WhsCode,

-- Se genera una variable donde se la asigna el nombre del almacen

(CASE WHEN WhsCode = 'ALC' THEN 'CALIDAD Y DESARROLLO'
WHEN WhsCode = 'ALCM' THEN 'COMPONENTES PARA MAQUILA'
WHEN WhsCode = 'ALDC' THEN 'DEVOLUCION DE CLIENTE'
WHEN WhsCode = 'ALDP' THEN 'DEVOLUCION DE PROVEEDORES'
WHEN WhsCode = 'ALEE' THEN 'EXPOS Y EVENTOS'
WHEN WhsCode = 'ALIN' THEN 'INSUMOS'
WHEN WhsCode = 'ALM' THEN 'MERMA'
WHEN WhsCode = 'ALMQI' THEN 'MAQUILA INTERNA (WIP)'
WHEN WhsCode = 'ALPE' THEN 'PEDIDOS ESPECIALES'
WHEN WhsCode = 'ALPM' THEN 'MAYOREO'
WHEN WhsCode = 'ALPO' THEN 'ONLINE'
WHEN WhsCode = 'ALPRO' THEN 'PROMOCIONALES'
WHEN WhsCode = 'ALQ' THEN 'CUARENTENA'
WHEN WhsCode = 'ALR' THEN 'RECIBO'
WHEN WhsCode = 'ALMQE' THEN 'MAQUILA EXTERNA (WIP)'
ELSE '' END) Almacen, s.OnHand, s.IsCommited, s.OnHand - s.IsCommited disponible 
 

FROM OITW s INNER JOIN OITM o ON s.ItemCode = o.ItemCode