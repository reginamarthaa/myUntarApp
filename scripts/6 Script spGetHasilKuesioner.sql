create proc [spGetHasilKuesioner]
AS
begin
	select CASE 
			WHEN hasil = 1 THEN 'Tertarik'
			WHEN hasil = 0 THEN 'Ragu-ragu'
			WHEN hasil = 2 THEN 'Tidak teratrik'
			ELSE 'Tidak Diketahui'
		END AS Label,
		count(hasil) as Jumlah
	from DATA_KUESIONER
	group by hasil
	--FOR JSON auto
end