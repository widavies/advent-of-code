# Every packet has a header
# 000:000:
# VER:TID

# Stored in big endian format

# Type id = 5: literal value
# - pad until with leading zero until length is multiple of four bits
# - broken into groups of four bits
# - each group is prefixed with 1 except the last bit

#