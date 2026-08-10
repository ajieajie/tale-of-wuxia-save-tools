"""用 UnityPy 扫描 resources.assets，找出包含角色/武功/秘籍映射的配置表 TextAsset。"""
import sys, os
from UnityPy import load

ASSETS = r"F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/YoungHero_Data/resources.assets"

KEYWORDS = ["荆棘", "龙墨", "谷月轩", "血刀经", "正气决", "正气诀",
            "林冲策马鞭", "水浒英雄掌", "秘籍"]

def main():
    env = load(ASSETS)
    total = 0
    textassets = []
    for obj in env.objects:
        total += 1
        if obj.type.name != "TextAsset":
            continue
        try:
            data = obj.read()
        except Exception as e:
            continue
        name = data.name if hasattr(data, "name") else ""
        script = getattr(data, "m_Script", b"")
        if isinstance(script, (bytes, bytearray)):
            try:
                text = script.decode("utf-8", errors="ignore")
            except Exception:
                continue
        elif isinstance(script, str):
            text = script
        else:
            continue
        if not text:
            continue
        found = [k for k in KEYWORDS if k in text]
        if found:
            textassets.append((name, len(text), found, text))
    print("total objects:", total, "matched TextAssets:", len(textassets))
    for name, ln, found, text in textassets:
        print("="*80)
        print("NAME:", name, "len:", ln, "keywords:", found)
        # 打印匹配行上下文
        for k in found:
            idx = 0
            while True:
                i = text.find(k, idx)
                if i == -1:
                    break
                ctx = text[max(0,i-80):i+120].replace("\n"," ")
                print(f"  [{k}] ...{ctx}...")
                idx = i + 1
                if idx > 200000:
                    break
    # 如果太大，只保存首个匹配到文件
    if textassets:
        out = textassets[0][3]
        with open("extracted_npcdata.txt","w",encoding="utf-8") as f:
            f.write(out)
        print("saved first match -> extracted_npcdata.txt")

if __name__ == "__main__":
    main()
