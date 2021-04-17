USE [DSTraining]
GO
/****** Object:  StoredProcedure [dbo].[BLD_WRK_THESISDATABASE_20210315]    Script Date: 4/17/2021 11:55:44 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROC [dbo].[BLD_WRK_THESISDATABASE_20210315]
-- =============================================
-- Author:		Yekta Khalili
-- Create date:  
-- Description:	RAW -> WRK
-- MOD DATE:
-- =============================================

AS
BEGIN

-- =============================================
-- DROP TABLE 
-- =============================================
IF OBJECT_ID('WRK_THESISDATABASE_20210315') IS NOT NULL
DROP TABLE [WRK_THESISDATABASE_20210315]

-- =============================================
-- CREATE TABLE 
-- =============================================
	
CREATE TABLE [WRK_THESISDATABASE_20210315](		
	[InvoiceNo]	VARCHAR(1000)
	,[StockCode]VARCHAR(1000)
	,[Quantity] INT
	,[UnitPrice]FLOAT
	)

-- =============================================
-- TRUNCATE TABLE
-- =============================================
TRUNCATE TABLE [dbo].[WRK_THESISDATABASE_20210315]

-- =============================================
-- INSERT INTO
-- =============================================

INSERT INTO [WRK_THESISDATABASE_20210315](
	 [InvoiceNo]
	 ,[StockCode]
	 ,[Quantity]
	 ,[UnitPrice]
)
SELECT 
	  [InvoiceNo]
	  ,[StockCode]
	  ,[Quantity]
	  ,[UnitPrice]
FROM [dbo].[DATASET_THESIS_20210315] 

--(X rows affected)




END

/*
SELECT * FROM [dbo].[RAW_CustomerList_20210128]
*/
