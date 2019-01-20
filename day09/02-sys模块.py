import sys
import time

# print(sys.path)
# print(sys.version)
# print(sys.platform)

# print(sys.argv)

# sys.stdout.write('#')
# sys.stdout.write('#')

for i in range(60):
    sys.stdout.write('#')
    time.sleep(.1)
    sys.stdout.flush()