SELECT T1.Address, T1.CardCode, T0.[CardName], T2.[SlpName], T3.[TrnspName], T1.Street, T1.Block, T1.ZipCode, T1.City, T1.County, T1.Country, T1.State, T1.LicTradNum, T1.CreateDate, T1.CreateTS 
FROM OCRD T0  
INNER JOIN CRD1 T1 ON T0.[CardCode] = T1.[CardCode] 
INNER JOIN OSLP T2 ON T0.[SlpCode] = T2.[SlpCode] 
INNER JOIN OSHP T3 ON T0.[ShipType] = T3.[TrnspCode] 
WHERE T1.CardCode LIKE 'CM%'