CREATE SCHEMA LOGS
GO

CREATE TABLE LOGS.RUN_TIMES(
	ID uniqueidentifier PRIMARY KEY DEFAULT NEWID(),
	JOB_START datetime,
	JOB_END datetime,
	WORK_ITEMS int
)
GO


DECLARE @Counter INT 
SET @Counter=1
WHILE ( @Counter <= 100)
BEGIN
	INSERT INTO LOGS.RUN_TIMES 
	(JOB_START, JOB_END, WORK_ITEMS) VALUES
	(DATEADD(SECOND,CAST((RAND() * -10000) as int),GETDATE()), DATEADD(SECOND,CAST((RAND() * 10000) as int),GETDATE()), CAST((RAND() * 10000) as int))

	SET @Counter = @Counter + 1

END
