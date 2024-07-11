def solution(spell, dic):
    # dic의 요소 중복 제거 'soo' -> {'s', 'o'}
    for d in dic:
        spell_match_count = 0
        for s in spell:
            if s in set(d):
                spell_match_count += 1
        if spell_match_count == len(spell):
            return 1
                
    return 2