def find_msd_lsd(number):
    number_str = str(number)
    msd = number_str[0] 
    lsd = number_str[-1]  
    return msd, lsd


number = 1010101


msd, lsd = find_msd_lsd(number)


print(f"MSD: {msd}, LSD: {lsd}")