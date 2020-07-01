import sys

print(type(sys.modules))
print(sys.modules)

import check
print(type(check))
print(id(check))
print(sys.modules)
import check
print(id(check))
