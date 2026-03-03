from functools import cache

G = {k[:-1]:v for k,*v in map(str.split, open('text'))}

@cache
def count(here, dac, fft):
    match here:
        case 'out': return dac and fft
        case 'dac': dac = True
        case 'fft': fft = True

    return sum(count(next, dac, fft) for next in G[here])

print(count('you', 1, 1), count('svr', 0, 0))