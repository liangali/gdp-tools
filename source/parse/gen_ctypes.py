from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer
import xml.etree.ElementTree as ET

out_txt = []
removed_str = '()/\\ ,[]'
tree = ET.parse('img_state.xml')
root = tree.getroot()

out_txt.append('from .base import *\n')
out_txt.append('class %s(PStruct):'%root[0].get('Name'))
out_txt.append('    _fields_ = [')

print(root[0].get('Name'))

for child in root:
    print(child.tag, child.attrib)

for DWord in root.iter('DWord'):
    print(DWord.tag, DWord.attrib)
    out_txt.append('        # %s %s'%(DWord.tag, DWord.get('Name')))
    for BitField in DWord.iter('BitField'):
        print('   ', BitField.tag, BitField.get('Name'), BitField.get('LowBit'), BitField.get('HighBit'))
        if '..' in DWord.get('Name'):
            lo = int(DWord.get('Name').split('..')[0])
            hi = int(DWord.get('Name').split('..')[1])
            name = 'DW%s'%DWord.get('Name').replace('..', '_')
            out_txt.append('        ("%s", c_uint32*%d)'%(name, hi-lo+1))
            pass
        else:
            bit_len = 0
            if BitField.get('LowBit') != None and BitField.get('HighBit') != None:
                hi = int(BitField.get('HighBit'))
                lo = int(BitField.get('LowBit'))
                bit_len = hi-lo+1
            elif BitField.get('Bits') != None:
                print('####', BitField.get('Bits'))
                if ':' in BitField.get('Bits'):
                    hi = int(BitField.get('Bits').split(':')[0])
                    lo = int(BitField.get('Bits').split(':')[1])                
                    bit_len = hi-lo+1
                else:
                    bit_len = 1
            name = BitField.get('Name').replace(' ', '_')
            for s in removed_str:
                name = name.replace(s, '')
            out_txt.append('        ("%s", c_uint32, %d)'%(name, bit_len))
            pass

out_txt.append('    ]\n')
with open('out.py', 'wt') as f:
    f.writelines('\n'.join(out_txt))

print('done')