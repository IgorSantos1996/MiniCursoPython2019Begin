times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flmanengo', 'Vasco', 'Chapecoense',
        'Atlético-mg','Botafogo','Atlético-pr','Bahia','São Paulo',
        'Fluminense','Fortaleza','Goiás','Avaí','Ceará','Fortaleza','CSA')

print(f'Os 5 primeiros times são: {times[0:5]}')
print("-=" * 30)
print(f'Os ultimos 4 times são : {times[-4:0]}  ')
print("-=" * 30)
print(f'Times em ordem alfabéticas: {sorted(times)}')
print("-=" * 30)
print(f'O São Paulo está no {times.index("São Paulo")+1}ª posição')

