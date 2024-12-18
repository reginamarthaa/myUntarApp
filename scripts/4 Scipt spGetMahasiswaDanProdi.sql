CREATE PROC [spGetMahasiswaDanProdi]
	@NIM VARCHAR(10),
	@NAMA VARCHAR(50),
	@NAMA_FAKULTAS VARCHAR(50),
	@NAMA_PROGRAM_STUDI VARCHAR(50)
AS
BEGIN
	DECLARE @WhereCond AS VARCHAR(MAX);
	DECLARE @Query AS VARCHAR(MAX);

	IF (@NAMA != '')
	BEGIN
		SET @WhereCond = ' m.NAMA like ''' + @NAMA + ''''
	END

	IF (@NAMA_PROGRAM_STUDI != '' AND @WhereCond IS NOT NULL)
	BEGIN
		SET @WhereCond = @WhereCond + ' AND  p.NAMA_PROGRAM_STUDI like ''' + @NAMA_PROGRAM_STUDI + ''''
	END
	ELSE IF (@NAMA_PROGRAM_STUDI != '')
	BEGIN
		SET @WhereCond = ' p.NAMA_PROGRAM_STUDI like ''' + @NAMA_PROGRAM_STUDI + ''''
	END

	IF (@NAMA_FAKULTAS != '' AND @WhereCond IS NOT NULL)
	BEGIN
		SET @WhereCond = @WhereCond + ' AND  p.NAMA_FAKULTAS like ''' + @NAMA_FAKULTAS + ''''
	END
	ELSE IF (@NAMA_FAKULTAS != '')
	BEGIN
		SET @WhereCond = ' p.NAMA_FAKULTAS like ''' + @NAMA_FAKULTAS + ''''
	END

	IF (@NIM != '' AND @WhereCond IS NOT NULL)
	BEGIN
		SET @WhereCond = @WhereCond + ' AND  m.NIM like ''' + @NIM + ''''
	END
	ELSE IF (@NIM != '')
	BEGIN
		SET @WhereCond = ' m.NIM like ''' + @NIM + ''''
	END

	set @Query =
		'select NIM, NAMA, NAMA_FAKULTAS, NAMA_PROGRAM_STUDI
		from MAHASISWA m
		join PROGRAM_STUDI p 
		on m.PROGRAM_STUDI_ID = p.PROGRAM_STUDI_ID '
	
	IF(@WhereCond IS NOT NULL)
	BEGIN
		SET @Query = @Query + 'WHERE ' + @WhereCond;
	END

	print (@Query);
	EXEC (@Query);	
END
