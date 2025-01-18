SELECT isnull(T6.baseref,'') as 'No. OV', T0.cardcode 'No.Cliente', T2.SlpCode 'Cod_vendedor', T0.Doctotal 'TotalFactura', T0.Docnum 'No.Factura', T1.seriesname 'Serie', T3.[ItemCode] 'SKU', T3.[Quantity] 'Cantidad', T3.[LineTotal] 'TotalLinea', T0.DocDate 'FechaFactura', T5.ItmsGrpNam as 'Categoría', T4.U_Codigo as 'Segmento', 

CASE T1.SeriesName 
WHEN 'Online' THEN 'Online' 
WHEN 'Mayoreo' THEN 'Mayoreo' 
WHEN 'PedEsp' THEN 'PedidosEspeciales' END AS 'Tipo de Venta', 

CASE T3.[TaxCode] 
WHEN 'IVAC16' THEN T3.[LineTotal] 
WHEN 'IVAC0' THEN T3.[LineTotal] END AS 'Total Linea', 

CASE T3.[TaxCode] 
WHEN 'IVAC16' THEN (T3.LineTotal-T3.Quantity*T3.GrossBuyPr) 
WHEN 'IVAC0' THEN T3.LineTotal-T3.Quantity*T3.GrossBuyPr END AS 'Total Ganancia' 

FROM OINV T0  INNER JOIN NNM1 T1 ON T0.[Series] = T1.[Series] 

INNER JOIN OSLP T2 ON T0.[SlpCode] = T2.[SlpCode] 
INNER JOIN INV1 T3 ON T0.[DocEntry] = T3.[DocEntry] 
inner join OITM T4 ON T4.itemcode=T3.Itemcode 
inner join OITB T5 ON T5.ItmsGrpCod=T4.ItmsGrpCod 
left join DLN1 T6 ON t6.ObjType=t3.basetype and t6.DocEntry=t3.baseentry and t6.LineNum=t3.BaseLine 

WHERE T0.CANCELED = 'N' AND T0.DocDate >= '20240601' 

UNION ALL SELECT isnull(T6.baseref,'') as 'No. OV', T0.cardcode 'No.Cliente', T2.SlpCode 'Cod_vendedor', -T0.Doctotal 'TotalFactura', T0.Docnum 'No.Factura', T1.seriesname 'Serie', T3.[ItemCode] 'SKU', -T3.[Quantity] 'Cantidad', -T3.[LineTotal] 'TotalLinea', T0.DocDate 'FechaFactura', T5.ItmsGrpNam as 'Categoría', T4.U_Codigo as 'Segmento',

CASE T1.SeriesName 
WHEN 'Online' THEN 'Online' 
WHEN 'Mayoreo' THEN 'Mayoreo' 
WHEN 'PedEsp' THEN 'PedidosEspeciales' END AS 'Tipo de Venta', 

CASE T3.[TaxCode] 
WHEN 'IVAC16' THEN (-T3.[LineTotal]) 
WHEN 'IVAC0' THEN -T3.[LineTotal] END AS 'Total Linea', 

CASE T3.[TaxCode] 
WHEN 'IVAC16' THEN (-T3.LineTotal-T3.Quantity*T3.GrossBuyPr) 
WHEN 'IVAC0' THEN (-T3.LineTotal-T3.Quantity*T3.GrossBuyPr) END AS 'Total Ganancia' 

FROM ORIN T0 INNER JOIN NNM1 T1 ON T0.[Series] = T1.[Series] 

INNER JOIN OSLP T2 ON T0.[SlpCode] = T2.[SlpCode] 
INNER JOIN RIN1 T3 ON T0.[DocEntry] = T3.[DocEntry] 
inner join OITM T4 ON T4.itemcode=T3.Itemcode 
inner join OITB T5 ON T5.ItmsGrpCod=T4.ItmsGrpCod 
left join DLN1 T6 ON t6.ObjType=t3.basetype and t6.DocEntry=t3.baseentry and t6.LineNum=t3.BaseLine 

WHERE T0.CANCELED = 'N' AND T0.DocDate >= '20240601'