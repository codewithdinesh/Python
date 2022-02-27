# Program to convert bits to Bytes,KiloBytes, MegaBytes, GigaBytes, TeraBytes.

bits = int(input("Enter Bits: "))
# 1 Bit = 8 Bytes
bytes = bits/8

# 1 kb = 1024 Bytes or 8 ratio to 3
kb = bits/1024*8

# 1 Mb = 1024 kb or 8 ratio to 6
mb = bits/(1024*1024*8)

# 1 Gb = 1024 Mb or 8 ratio to 9
gb = bits/(1024*1024*1024*8)

# 1 Tb = 1024 Gb or 8 ratio to 12
tb = bits/(1024*1024*1024*1024*8)

print("In Bytes: ", bytes)
print("In KiloBytes: ", kb)
print("In MegaBytes: ", mb)
print("In GigaBytes: ", gb)
print("In TeraBytes: ", tb)
