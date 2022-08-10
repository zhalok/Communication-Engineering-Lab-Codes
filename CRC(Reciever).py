def CRC_reciever(crc, encoded):
    crc_len = len(crc)
    enconded_len = len(encoded)
    i = 0
    while(i <= enconded_len-crc_len):
        for j in range(crc_len):
            encoded[i+j] = '0' if encoded[i+j] == crc[j] else '1'
        while(i < enconded_len and encoded[i] != '1'):
            i += 1

    sub_enc = encoded[enconded_len-crc_len::1]
    for i in sub_enc:
        if(i != '0'):
            print("Error in message")
            return

    print("No error")


encoded = "101101110011"
crc = "1101"


CRC_reciever(list(crc), list(encoded))
