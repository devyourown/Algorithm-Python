def find_team_leader(team_leader, x):
    if team_leader[x] != x:
        team_leader[x] = find_team_leader(team_leader, team_leader[x])
    return team_leader[x]

def is_same_team(team_leader, a, b):
    a = find_team_leader(team_leader, a)
    b = find_team_leader(team_leader, b)
    if a == b:
        return True
    else :
        return False

def union_team(team_leader, a, b):
    a = find_team_leader(team_leader, a)
    b = find_team_leader(team_leader, b)
    if a < b:
        team_leader[b] = a
    else :
        team_leader[a] = b

N, M = map(int, input().split())
team_leader = [0] * (N+1)
for i in range(1, N+1):
    team_leader[i] = i

for i in range(M):
    operator, student_1, student_2 = map(int, input().split())
    if operator == 0:
        union_team(team_leader, student_1, student_2)
    else :
        if is_same_team(team_leader, student_1, student_2):
            print("YES")
        else:
            print("NO")
