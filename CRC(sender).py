def CRC_sender(msg, divisor):

    msg_len = len(msg)
    divisor_len = len(divisor)
    encoded = []
    encoded += (msg)
    for i in range(divisor_len-1):
        encoded.append('0')
    encoded_len = len(encoded)

    i = 0
    while i <= (encoded_len-divisor_len):
        for j in range(divisor_len):
            encoded[i+j] = '0' if encoded[i+j] == divisor[j] else '1'
        while i < encoded_len and encoded[i] != '1':
            i += 1

    msg += (encoded[(encoded_len-divisor_len+1)::1])
    _msg = ""
    for i in msg:
        _msg += i
    return _msg


# msg = list(input("Enter binary message\n"))
# divisor = list(input("Enter the divisor\n"))
msg = list("101101110")
divisor = list("1101")
print(CRC_sender(msg, divisor))
