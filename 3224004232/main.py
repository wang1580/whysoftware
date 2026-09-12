# main.py
import sys
import jieba

def get_simhash(text: str, hash_bits=64) -> int:
    """
    计算文本simhash指纹
    :param text: 原始文本
    :param hash_bits: 指纹位数，默认64位
    :return: simhash整数值
    """
    # 分词
    words = jieba.lcut(text)
    # 初始化向量
    v = [0] * hash_bits
    for word in words:
        h = hash(word)
        for i in range(hash_bits):
            bit = (h >> i) & 1
            if bit:
                v[i] += 1
            else:
                v[i] -= 1
    # 生成指纹
    fingerprint = 0
    for i in range(hash_bits):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint

def hamming_distance(hash1: int, hash2: int) -> int:
    """计算两个64位哈希的海明距离"""
    return bin(hash1 ^ hash2).count("1")

def calc_similarity(hamming_dist: int, bits=64) -> float:
    """根据海明距离计算相似度（0~1），保留两位小数"""
    sim = 1 - hamming_dist / bits
    return round(sim, 2)

def read_file(file_path: str) -> str:
    """读取文本文件，异常处理：文件不存在、编码错误"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{file_path}")
    except UnicodeDecodeError:
        raise Exception(f"文件编码错误，无法读取：{file_path}")

def write_result(file_path: str, rate: float):
    """把重复率写入结果文件"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{rate:.2f}")
    except Exception as e:
        raise Exception(f"写入文件失败：{str(e)}")

def main():
    # 命令行参数校验
    if len(sys.argv) != 4:
        print("参数错误！使用方式：python main.py 原文路径 抄袭文件 输出文件")
        sys.exit(1)
    orig_path = sys.argv[1]
    copy_path = sys.argv[2]
    ans_path = sys.argv[3]
    try:
        orig_text = read_file(orig_path)
        copy_text = read_file(copy_path)
        hash_orig = get_simhash(orig_text)
        hash_copy = get_simhash(copy_text)
        dist = hamming_distance(hash_orig, hash_copy)
        repeat_rate = calc_similarity(dist)
        write_result(ans_path, repeat_rate)
    except Exception as e:
        print(f"程序异常：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
