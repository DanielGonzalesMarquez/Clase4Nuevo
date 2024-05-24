Use kaggle
go

--en caso no exista la tabla netflix
if not exists (select*from sys.tables where object_id = object_id(N'dbo.netflix') and type = 'U')
	CREATE TABLE NETFLIX (
	show_id varchar(20),
	type_show varchar(20),
	title varchar(max),
	director varchar(max),
	cast_show varchar(max),
	country varchar(200),
	date_show varchar(50),
	release_year varchar(10),
	rating varchar(10)
	)
--si existe se trunca
truncate table dbo.netflix

--ingestar dataset
bulk insert dbo.netflix
from 'URL DE LA DATASET'
WITH
(
	FIRSTROW = 2, --EMPEIZA EN LA 2DA FILA (LA PRIMERA ES CABECERA)
	FIELDTERMINATOR = ',', --SEPARADOR DE COLUMNAS
	ROWTERMINATOR =´'0x0a' --Hace referencia al salto de línea
)

GO	