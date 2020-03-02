"""
2012년 12월 31일 새벽 4시부터 지상파 아날로그 TV방송이 종료되었다. TV를 자주보는 할머니를 위해서, 상근이네 집도 디지털 수신기를 구입했다.
원래 상근이네 집에는 KBS1과 KBS2만 나왔다. 할머니는 두 방송만 시청한다. 이제 디지털 수신기와 함께 엄청난 양의 채널을 볼 수 있게 되었다.
하지만, 할머니는 오직 KBS1과 KBS2만 보려고 한다. 따라서, 상근이는 채널 리스트를 조절해 KBS1을 첫 번째로, KBS2를 두 번째로 만들려고 한다.
티비를 켜면 디지털 수신기는 시청 가능한 채널 리스트를 보여준다. 모든 채널의 이름은 서로 다르고, 항상 KBS1과 KBS2를 포함하고 있다.
상근이는 이 리모콘을 이용해서 리스트의 순서를 바꾸는 법을 알아냈다. 리스트의 왼편에는 작은 화살표가 있고, 이 화살표는 현재 선택한 채널을 나타낸다.
가장 처음에 화살표는 제일 첫 번째 채널을 가리키고 있다.
다음과 같은 네 가지 버튼을 이용해서 리스트의 순서를 바꿀 수 있다. 각각은 1번부터 4번까지 번호가 적혀져있는 버튼이다.
화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)
화살표가 채널 리스트의 범위를 넘어간다면, 그 명령은 무시한다.
현재 채널 리스트의 순서가 주어졌을 때, KBS1를 첫 번째로, KBS2를 두 번째로 순서를 바꾸는 방법을 구하는 프로그램을 작성하시오.
방법의 길이는 500보다 작아야 한다. 두 채널을 제외한 나머지 채널의 순서는 상관없다.
"""

# 채널의 수 N, 채널 리스트 C를 입력받고 KBS1, KBS2의 인덱스 번호를 저장한다.
N = int(input())
C = list(input() for _ in range(N))
idx1, idx2 = C.index("KBS1"), C.index("KBS2")

# KBS1의 위치를 찾는다.(인덱스 0번에 위치할 경우 넘어간다.)
# 해당 위치만큼 1번을 조작하여 화살표를 위치시킨다.
# 인덱스 0번까지 4번을 조작하여 KBS1을 위치시킨다.
# 실제 리스트를 이동시키지 않고 눌러야 되는 버튼만 추가한다.
# 1번을 인덱스 번호만큼 누르고, 4번을 인덱스 번호만큼 누른다.
answer = ("1" * idx1) + ("4" * idx1)

# KBS2의 위치를 찾는다.(인덱스 1번에 위치할 경우 넘어간다.)
# 1번을 인덱스 번호만큼 누르고, 4번을 (인덱스 번호 -1) 만큼 누른다.
if idx2 == 0:
    pass
else:
    # KBS2의 인덱스 번호가 KBS1의 인덱스 번호보다 작을경우 한칸씩 밀린다.
    if idx1 > idx2:
        idx2 += 1
    answer += ("1" * idx2)
    answer += ("4" * (idx2 - 1))
print(answer)