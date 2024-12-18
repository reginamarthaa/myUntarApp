CREATE PROC [dbo].[spDeleteDataKuesionerMahasiswa]
	@NIM VARCHAR(10)

AS
BEGIN
	IF EXISTS (
		SELECT 1
		FROM DATA_KUESIONER
		WHERE NIM = @NIM
	)
	BEGIN
		DELETE FROM DATA_KUESIONER WHERE NIM = @NIM
	END

	IF EXISTS (
		SELECT 1
		FROM MAHASISWA
		WHERE NIM = @NIM
	)
	BEGIN
		DELETE FROM MAHASISWA WHERE NIM = @NIM
	END

END