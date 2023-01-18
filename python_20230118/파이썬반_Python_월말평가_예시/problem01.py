def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    max_ = scores[0]
    for i in range(1, len(scores)):
        if max_ < scores[i]:
            max_ = scores[i]
    return max_



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
