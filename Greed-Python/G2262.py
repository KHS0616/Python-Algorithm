"""
월드시에서는 매년 n명의 사람들이 모여 월드 크래프트라는 게임의 토너먼트 대회를 치른다. 
이 게임은 특성상 실력만이 승패를 좌우하기 때문에, 아무리 실력이 엇비슷한 사람이 시합을 치러도 랭킹이 높은 사람이 반드시 이기게 된다. 
따라서 월드시에서는 게임을 흥미진진하게 만들기 위해서, 부전승을 여러 번 만들더라도 각 시합에 임하는 선수들의 랭킹 차이를 비슷하게 만들려고 한다.

토너먼트를 만들 때에는 이미 추첨이 된 순서대로 선수들을 배치하고, 왼쪽에서 오른쪽의 순서가 어긋나지 않도록 시합을 정한다. 
물론 부전승을 임의로 만들 수 있지만, 토너먼트가 꼬여서는 안 된다. 또한, 각 시합에 임하는 두 선수의 랭킹의 차이의 합이 최소가 되도록 하려 한다.
"""
# 선수 수와 각각의 랭크를 입력 받음
# 정답을 출력하기 위한 변수 선언
n, rank = int(input()), list(map(int, input().split(" ")))
answer = 0

while(len(rank)-1):
    # 순위가 제일 낮은 선수를 찾는다.
    min_index = rank.index(max(rank))
    # 왼쪽 끝인 경우이거나 오른쪽 끝인 경우 무조건 반대쪽이랑 매칭
    if min_index == 0:
        diff = abs(rank[min_index] - rank[min_index + 1])
    elif min_index == len(rank)-1:
        diff = abs(rank[min_index] - rank[min_index -1])
    # 그렇지 않은 경우 왼쪽, 오른쪽 순으로 비교해서 매칭
    else:
        diff = min(abs(rank[min_index] - rank[min_index -1]), abs(rank[min_index] - rank[min_index + 1]))

    # 순위 차이 계산
    answer += diff
    # 순위가 제일 낮은 선수 리스트에서 제거
    del rank[min_index]

# 결과 출력
print(answer) 