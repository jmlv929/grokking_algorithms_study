


def cal_longest_subsequence(s1, s2):
    cell = [[0 for j in range(len(s2) + 1) ] for i in range(len(s1) +1 )]  # 表格的最上方 左方都加上0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) +1 ):
            if s1[i-1] == s2[j-1]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell



if __name__ == "__main__":
    s1 = 'fosh'  #用户输入
    s2 = 'fort'
    s3 = 'fish' #正确的 单词       输入s1 s2 找出 最长公共子序列
    s4 = 'fooosh'

    print(' %s 与 %s 的 最长公共子序列的网格为：' % (s1, s2))
    print(cal_longest_subsequence(s1, s2))

    print(' %s 与 %s 的 最长公共子序列的网格为：' % (s1, s3))
    print(cal_longest_subsequence(s1, s3))

    print(' %s 与 %s 的 最长公共子序列的网格为：' % (s1, s4))
    print(cal_longest_subsequence(s1, s4))

