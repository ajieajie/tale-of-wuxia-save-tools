import struct

# Try to figure out the .pk file encryption
pk_path = 'F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/Config/EffectText.pk'

with open(pk_path, 'rb') as f:
    data = f.read()

print(f"File size: {len(data)} bytes")
print(f"Header (first 32 bytes hex): {data[:32].hex()}")
print(f"Header (first 32 bytes): {data[:32]}")

# Try 1: XOR with the 16-byte header key
key = data[:16]
decrypted = bytes([data[i] ^ key[i % 16] for i in range(16, min(len(data), 160))])
print(f"\nXOR with header key (first 144 bytes after header):")
print(f"Hex: {decrypted[:32].hex()}")
try:
    print(f"Text: {decrypted[:100].decode('utf-8', errors='replace')}")
except:
    pass

# Try 2: Check if it's a known archive format after the header
# Check for ZIP signature (PK\x03\x04)
for sig_name, sig in [('ZIP', b'PK\x03\x04'), ('GZIP', b'\x1f\x8b'), ('TAR', b'ustar'), ('RAR', b'Rar!')]:
    pos = data.find(sig)
    if pos >= 0:
        print(f"\nFound {sig_name} signature at offset {pos}")

# Try 3: Maybe the header is a hash, and the actual data starts at offset 16 or 32
for offset in [16, 32, 64, 128, 256]:
    chunk = data[offset:offset+16]
    print(f"\nAt offset {offset}: {chunk.hex()} | {''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)}")

# Try 4: Check if it's AES encrypted (look for patterns)
# If AES-CBC with a known IV, the first 16 bytes might be the IV
# Let's check entropy of the data
import math
from collections import Counter
counter = Counter(data[16:1024+16])
entropy = -sum(count/1024 * math.log2(count/1024) for count in counter.values())
print(f"\nEntropy of first 1KB after header: {entropy:.2f} bits/byte")
# High entropy (>7.5) suggests encryption or compression

# Try 5: Maybe it's just compressed (zlib/gzip/deflate) after the header
import zlib
for offset in [0, 16, 32]:
    try:
        decompressed = zlib.decompress(data[offset:])
        print(f"\nZlib decompression successful at offset {offset}! Size: {len(decompressed)}")
        print(f"First 100 bytes: {decompressed[:100]}")
        break
    except:
        pass
    try:
        decompressed = zlib.decompress(data[offset:], -15)  # raw deflate
        print(f"\nRaw deflate decompression successful at offset {offset}! Size: {len(decompressed)}")
        print(f"First 100 bytes: {decompressed[:100]}")
        break
    except:
        pass

# Try 6: Simple byte-level analysis
# Check if there's a pattern in the first few hundred bytes
print(f"\nFirst 64 bytes as decimal: {list(data[:64])}")
