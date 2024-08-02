n = int(input("시험본 과목 개수: "))
scores_str = input("각 과목의 시험 성적: ").split(" ")

scores = []
for s in scores_str:
    scores.append(int(s))
    
max_scores = max(scores)
hap = 0
for score in scores:
    hap += (score/max_scores*100)

print(hap/n)