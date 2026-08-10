"""尝试破解 .pk 格式：多种解压 + 多种 XOR。目标 cForm_chs.pk / BigMapNodeData.pk。"""
import zlib, brotli, lz4.block, os, struct, sys

CFG = r"F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/Config/"

def cjk_count(buf):
    try:
        t = buf.decode("utf-8", "ignore")
    except Exception:
        return 0
    return sum(1 for ch in t if "\u4e00" <= ch <= "\u9fff")

def try_decompress(label, data):
    results = []
    # zlib at various offsets
    for off in (0, 1, 2, 4, 8, 12):
        try:
            x = zlib.decompress(data[off:])
            if cjk_count(x) > 10:
                results.append((label + f" zlib@{off}", x))
        except Exception:
            pass
    # gzip
    try:
        import gzip
        x = gzip.decompress(data)
        if cjk_count(x) > 10:
            results.append((label + " gzip", x))
    except Exception:
        pass
    # brotli
    try:
        x = brotli.decompress(data)
        if cjk_count(x) > 10:
            results.append((label + " brotli", x))
    except Exception:
        pass
    # lz4 raw (guess uncompressed up to 5MB)
    for usize in (500000, 2000000, 5000000, 20000000):
        try:
            x = lz4.block.decompress(data, uncompressed_size=usize)
            if cjk_count(x) > 10:
                results.append((label + f" lz4raw@{usize}", x))
                break
        except Exception:
            pass
    return results

def try_xor(label, data, limit=200000):
    results = []
    chunk = data[:limit]
    # single byte
    for k in range(256):
        x = bytes(c ^ k for c in chunk)
        if cjk_count(x) > 30:
            results.append((label + f" xor1@{k}", x))
    # 8-byte header repeating
    head = data[:8]
    x = bytes(chunk[i] ^ head[i % 8] for i in range(len(chunk)))
    if cjk_count(x) > 30:
        results.append((label + " xor8head", x))
    # 4-byte repeating starting from offset 0
    for kl in (4, 8, 16):
        key = data[:kl]
        x = bytes(chunk[i] ^ key[i % kl] for i in range(len(chunk)))
        if cjk_count(x) > 30:
            results.append((label + f" xor{kl}lead", x))
    return results

def main():
    targets = ["cForm_chs.pk", "BigMapNodeData.pk"]
    for tf in targets:
        p = os.path.join(CFG, tf)
        if not os.path.exists(p):
            continue
        b = open(p, "rb").read()
        head = b[:8]
        data = b[8:]
        print("="*70)
        print(tf, "size", len(b), "head", head.hex())
        # entropy of data[8:4096]
        from collections import Counter
        import math
        c = Counter(data[:4096])
        ent = -sum(n/4096*math.log2(n/4096) for n in c.values())
        print("entropy(data[:4096])", round(ent,3))
        hits = []
        hits += try_decompress(tf, data)
        hits += try_decompress(tf, b)  # with header
        hits += try_xor(tf, data)
        if hits:
            for label, x in hits[:5]:
                print(">>> MATCH", label, "cjk", cjk_count(x))
                print(x[:300])
        else:
            print("no match (decompress/xor simple)")

if __name__ == "__main__":
    main()
