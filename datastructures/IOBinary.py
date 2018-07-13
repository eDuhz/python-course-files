__author__= 'eduh'
#with open('binary', 'bw') as bin_file:
#    bin_file.write(bytes(range(17)))
#
#with open('binary', 'br') as binFile:
#    for b in binFile:
#        print(b)

a = 65334   #FF FE
b = 65335   #FF FF
c = 65336   #00 01 00 00
x = 2998302 #02 2D C0 1E

with open('binary2', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(2,'big'))
    bin_file.write(c.to_bytes(4,'big'))
    bin_file.write(x.to_bytes(4,'big'))
    bin_file.write(x.to_bytes(4,'little'))

with open('binary2', 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    f = int.from_bytes(bin_file.read(2), 'big')
    g = int.from_bytes(bin_file.read(4), 'big')
    h = int.from_bytes(bin_file.read(4), 'big')
    i = int.from_bytes(bin_file.read(4), 'little')
    print('{0}\n{1}\n{2}\n{3}\n{4}'.format(e,f,g,h,i))
