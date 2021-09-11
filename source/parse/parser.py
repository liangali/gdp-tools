cmd_struct = {}
stag = '		union {'
etag = '		}'

with open('tmp.txt', 'rt') as f:
    start, union_list, ln = False, [], 0
    for line in f:
        ln += 1
        if start == True:
            union_list.append(line.strip('\t\n'))
            if line.startswith(etag):
                
                start = False
                cmd_struct[ln] = union_list
        else:
            if line.startswith(stag):
                start = True
                union_list = [stag]
            else:
                continue
            
# print(cmd_struct)

for k, v in cmd_struct.items():
    print('\n'.join(v), '\n\n')

print('done')
