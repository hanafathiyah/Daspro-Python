def hashing(password):

    sum = 0
    for i in range(len(password)):
        data_hash = ord(password[i]) * 2**(i)
        sum += data_hash
    
    hasil_hash = sum % 26

    return hasil_hash



