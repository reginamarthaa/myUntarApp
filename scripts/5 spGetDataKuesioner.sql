create proc [dbo].[spGetDataKuesioner]
 @PERTANYAAN varchar(max)
AS
begin

	exec('select '+@PERTANYAAN+' as Nilai,
				count('+@PERTANYAAN+') as Jumlah
		from DATA_KUESIONER
		group by '+@PERTANYAAN+'')
end