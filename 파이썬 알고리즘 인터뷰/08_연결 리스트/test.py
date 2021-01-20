a = '1->2->2->1'

print(a.split('->'))
print(a)
'1->2'
b = a.split('->')

if b == b[::-1]:
    print('yeah')