import sys

def simhash(text):
    """
    对输入中文文本生成64位simhash指纹
    :param text: 原始输入文本字符串
    :return: 64bit整数指纹
    """
    # 清洗中文标点
    words = text.replace("，", " ").replace("。", " ").replace("；", " ").replace("：", " ").split()
    v = [0] * 64
    for word in words:
        h = hash(word)
        for i in range(64):
            bit = (h >> i) & 1
            if bit == 1:
                v[i] += 1
            else:
                v[i] -= 1
    fingerprint = 0
    for i in range(64):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint

def hamming_distance(h1, h2):
    """计算两个指纹的海明距离"""
    xor = h1 ^ h2
    return bin(xor).count("1")

def calc_similarity(d):
    """由海明距离计算相似度百分比"""
    return ((64 - d) / 64) * 100

def main():
    # 接收3个命令行参数：原文、抄袭文件、输出结果文件
    if len(sys.argv) != 4:
        print("用法：python main.py 原文文件路径 抄袭文件路径 输出结果文件路径")
        return

    file_origin = sys.argv[1]
    file_copy = sys.argv[2]
    file_output = sys.argv[3]

    # 捕获原文文件不存在异常
    try:
        with open(file_origin, "r", encoding="utf-8") as f:
            text_origin = f.read().strip()
    except FileNotFoundError:
        print(f"错误：文件 {file_origin} 不存在！")
        return
    # 捕获抄袭文件不存在异常
    try:
        with open(file_copy, "r", encoding="utf-8") as f:
            text_copy = f.read().strip()
    except FileNotFoundError:
        print(f"错误：文件 {file_copy} 不存在！")
        return

    # 判断文本全为空
    if len(text_origin.strip()) == 0 or len(text_copy.strip()) == 0:
        print("错误：文本内容不能为空！")
        return

    # 计算指纹、海明距离、重复率
    f1 = simhash(text_origin)
    f2 = simhash(text_copy)
    dist = hamming_distance(f1, f2)
    similarity = calc_similarity(dist)

    # ✅核心：把重复率写入第三个输出文件，保留2位小数
    with open(file_output, "w", encoding="utf-8") as out_f:
        out_f.write(f"{similarity:.2f}")

    print(f"海明距离：{dist}")
    print(f"重复率：{similarity:.2f}%")

if __name__ == "__main__":
    main()
