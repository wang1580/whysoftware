import re

def get_words(text):
    words = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]', text)
    return "".join(words)

def simhash(text, hash_bits=64):
    words = get_words(text)
    v = [0] * hash_bits
    for w in words:
        h = hash(w)
        for i in range(hash_bits):
            bit = (h >> i) & 1
            if bit == 1:
                v[i] += 1
            else:
                v[i] -= 1
    fingerprint = 0
    for i in range(hash_bits):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def calc_similarity(dist, bits=64):
    return (bits - dist) / bits

if __name__ == "__main__":
    import sys
    if len(sys.argv) !=4:
        print("用法：python main.py test1.txt test2.txt result.txt")
        sys.exit()
    f1_path = sys.argv[1]
    f2_path = sys.argv[2]
    out_path = sys.argv[3]

    with open(f1_path, 'r', encoding='utf-8') as f:
        t1 = f.read()
    with open(f2_path, 'r', encoding='utf-8') as f:
        t2 = f.read()

    h1 = simhash(t1)
    h2 = simhash(t2)
    dist = hamming_distance(h1,h2)
    sim = calc_similarity(dist)

    res_text = f"海明距离：{dist}\n文本相似度：{sim:.4f}\n重复率：{sim*100:.2f}%"
    print(res_text)
    with open(out_path,'w',encoding='utf-8') as f:
        f.write(res_text)
