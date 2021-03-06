import os
import random
import time
from typing import List, Tuple
from urllib.request import urlopen

GAME_SERVER = os.getenv('GAME_SERVER', 'https://contest.gbc-2020.tenka1.klab.jp')
TOKEN = os.getenv('TOKEN', '98f3b387b30e2b488df7abd2a9d21eda')


def call_api(x) -> str:
    with urlopen(f'{GAME_SERVER}{x}') as res:
        return res.read().decode()


def calc_score(stage: List[List[int]], num_claim: List[List[int]], my_claim: List[List[int]]) -> float:
    visited = [[False for _ in range(20)] for _ in range(20)]

    def f(r, c) -> Tuple[float, int]:
        if r < 0 or r >= 20 or c < 0 or c >= 20 or my_claim[r][c] == 0 or visited[r][c]:
            return 1e+300, 0
        visited[r][c] = True
        r1 = stage[r][c] / num_claim[r][c]
        r2 = 1
        for r3, r4 in (f(r+1, c), f(r-1, c), f(r, c+1), f(r, c-1)):
            r1 = min(r1, r3)
            r2 += r4
        return r1, r2

    score = 0.0
    for i in range(20):
        for j in range(20):
            x, y = f(i, j)
            score += x * y
    return score

def max_val_pos(candidate,stage: List[List[int]], num_claim: List[List[int]]):
    ans = candidate[0]
    ma = 0
    for i in candidate:
        if ma < stage[i[0]][i[1]]/(num_claim[i[0]][i[1]]+1):
            ma = stage[i[0]][i[1]]/(num_claim[i[0]][i[1]]+1)
            ans = i
    return ans

def minpoint(stage: List[List[int]], num_claim: List[List[int]]):
    ans = [[stage[i][j]//max(1,num_claim[i][j]) for j in range(20)]for i in range(20)]
    print(ans)
    

        



def main():
    while True:

        #ゲーム開始
        game_resp = call_api('/api/game')
        game_id, remaining_ms = list(map(int, game_resp.split()))
        if game_id < 0:
            break

        stage_resp = call_api(f'/api/stage/{game_id}').split('\n')
        assert stage_resp[0] == '20'
        stage = [list(map(int, x.split(' '))) for x in stage_resp[1:21]]

        print(stage)

        #1ゲーム中のループ
        while True:
            areas_resp = call_api(f'/api/areas/{TOKEN}/{game_id}').split('\n')
            if areas_resp[0] == 'too_many_request':
                time.sleep(0.1)
                continue
            assert areas_resp[0] == 'ok'
            num_claim = [list(map(int, x.split(' '))) for x in areas_resp[1:21]]
            my_claim = [list(map(int, x.split(' '))) for x in areas_resp[21:41]]

            score = calc_score(stage, num_claim, my_claim)
            print(f'game_id: {game_id}  score: {score} time:{remaining_ms}')

            candidate = []
            for i in range(20):
                for j in range(20):
                    if my_claim[i][j] == 0:
                        candidate.append((i, j))

            assert len(candidate) > 0

            #ここだけ変える
            r, c = max_val_pos(candidate,stage,num_claim)

            claim_resp = call_api(f'/api/claim/{TOKEN}/{game_id}/{r}-{c}-1').split('\n')[0]
            if claim_resp == 'game_finished':
                break
            assert claim_resp == 'ok'

        #ゲーム終了時のスコア
        print(f'game_id: {game_id}  score: {score} time:{remaining_ms}')
        minpoint(stage,num_claim)
        #同じゲーム途中だったら待つだけ（エラー帽子）
        while int(call_api('/api/game').split()[0]) == game_id:
            time.sleep(0.1)


if __name__ == "__main__":
    main()
