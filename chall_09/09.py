from pwn import *
binary = context.binary = ELF('./chall_09')
p = process(binary.path)
key = binary.string(binary.sym.key)
x = xor(key,b'\x69')
b = bytes.fromhex(x)
c = xor(b, b'\x69')
p.send(c)
#string needs to be gotten manually you can set a break point at the 
#key. You need to check the stack and get the key value
p.interactive()
#FINISHED
