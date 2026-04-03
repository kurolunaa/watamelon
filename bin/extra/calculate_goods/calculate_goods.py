# the purpose of this is to just give me number
def calculate_goods(extravagant_salvaged_necklace, extravagant_salvaged_earring, extravagant_salvaged_bracelet, extravagant_salvaged_ring, salvaged_necklace, salvaged_earring, salvaged_bracelet, salvaged_ring):
    return (extravagant_salvaged_necklace * 34500) + (extravagant_salvaged_earring * 30000) + (extravagant_salvaged_bracelet * 28500) + (extravagant_salvaged_ring * 27000) + (salvaged_necklace * 13000) + (salvaged_earring * 10000) + (salvaged_bracelet * 9000) + (salvaged_ring * 8000) 

# the purpose of this is to send as a string, i'm too lazy to rewrite this and it serves its purpose so idgaf
def formatGoods(extravagant_salvaged_necklace, extravagant_salvaged_earring, extravagant_salvaged_bracelet, extravagant_salvaged_ring, salvaged_necklace, salvaged_earring, salvaged_bracelet, salvaged_ring):
    output = ""

    if (extravagant_salvaged_necklace > 0):
        output += f"{extravagant_salvaged_necklace}x Extravagant Salvaged Necklaces = {extravagant_salvaged_necklace * 34500:,d} gil\n"
    if (extravagant_salvaged_earring > 0):
        output += f"{extravagant_salvaged_earring}x Extravagant Salvaged Earrings = {extravagant_salvaged_earring * 30000:,d} gil\n"
    if (extravagant_salvaged_bracelet > 0):
        output += f"{extravagant_salvaged_bracelet}x Extravagant Salvaged Bracelets = {extravagant_salvaged_bracelet * 28500:,d} gil\n"
    if (extravagant_salvaged_ring > 0):
        output += f"{extravagant_salvaged_ring}x Extravagant Salvaged Rings = {extravagant_salvaged_ring * 27000:,d} gil\n"
    if (salvaged_necklace > 0):
        output += f"{salvaged_necklace}x Salvaged Necklaces = {salvaged_necklace * 13000:,d} gil\n"
    if (salvaged_earring > 0):
        output += f"{salvaged_earring}x Salvaged Earrings = {salvaged_earring * 10000:,d} gil\n"
    if (salvaged_bracelet > 0):
        output += f"{salvaged_bracelet}x Salvaged Bracelets = {salvaged_bracelet * 9000:,d} gil\n"
    if (salvaged_ring > 0):
        output += f"{salvaged_ring}x Salvaged Rings = {salvaged_ring * 8000:,d} gil\n"
        
    if output == "":
        output = "subs made no money :("
        return output

    output += f"Total amount obtained on this trip: **{((extravagant_salvaged_necklace * 34500) + 
                                                        (extravagant_salvaged_earring * 30000) + 
                                                        (extravagant_salvaged_bracelet * 28500) + 
                                                        (extravagant_salvaged_ring * 27000) + 
                                                        (salvaged_necklace * 13000) + 
                                                        (salvaged_earring * 10000 ) + 
                                                        (salvaged_bracelet * 9000) + 
                                                        (salvaged_ring * 8000)):,d} gil**"
    
    return output