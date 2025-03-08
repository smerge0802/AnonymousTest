from itertools import product
from math import pow, sqrt
import heapq
from constant import APPLE_SIZE, GRID_COLS, GRID_ROWS

# 사용 가능한 숫자 조합 (합이 10이 되는 조합들)
VALID_COMBINATIONS = {tuple(sorted(map(int, list(str(num))))) for num in [
    19, 28, 37, 46, 55,   # 2개 조합
    118, 127, 136, 145, 226, 235, 244, 334,  # 3개 조합
    1117, 1126, 1135, 1144, 1225, 1234, 1333, 2224, 2233,  # 4개 조합
    11116 , 11125 , 11134 , 11224 , 11233, 12223, 22222, # 5개 조합
    111115, 111124, 111133, 111223, 112222, # 6개 조합
    1111114, 1111123, 1111222, # 7개 조합
    11111113, 11111122, # 8개 조합
    111111112, # 9개 조합
    1111111111 # 10개 조합
]}

def get_numbers_in_box(grid, r1, c1, r2, c2):
    """주어진 좌표 범위 안에 있는 숫자 리스트를 반환"""
    numbers = []
    coords = []
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] and grid[r][c][0] is not None:  # 빈칸이 아닐 경우
                numbers.append(grid[r][c][0])  # 숫자 값
                coords.append((r, c, grid[r][c][1], grid[r][c][2]))  # (row, col, x, y)
    return numbers, coords

def find_solution(grid):
    print("🤔\t전략 수립 중...")
    solution = []

    while True:
        best_choice = None
        heap = []
        
        # 🔹 1. 가능한 직사각형 드래그 박스 탐색
        for r1, c1 in product(range(GRID_ROWS), range(GRID_COLS)):  # 시작점 (r1, c1)
            for r2, c2 in product(range(r1, GRID_ROWS), range(c1, GRID_COLS)):  # 끝점 (r2, c2)
                numbers, coords = get_numbers_in_box(grid, r1, c1, r2, c2)
                sorted_numbers = tuple(sorted(numbers))

                # 🔸 유효한 조합인지 확인 & 중복 선택 방지
                if sorted_numbers in VALID_COMBINATIONS:
                    priority = (-max(numbers), len(numbers))  # ❗ 큰 숫자 포함 조합 우선, 만약 똑같으면 길이가 더 짧은거
                    heapq.heappush(heap, (priority, coords))
    
        # 🔹 2. 가장 좋은 드래그 박스를 선택
        if heap:
            _, best_choice = heapq.heappop(heap)
        else:
            break  # 더 이상 선택할 수 있는 조합이 없으면 종료

        # 🔸 드래그 시작 (x1, y1) ~ 끝 (x2, y2)
        x_coords = [x for _, _, x, _ in best_choice]  # x 좌표들
        y_coords = [y for _, _, _, y in best_choice]  # y 좌표들

        x1, x2 = min(x_coords), max(x_coords) + APPLE_SIZE
        y1, y2 = min(y_coords), max(y_coords) + APPLE_SIZE

        solution.append((x1, y1, x2, y2))  # 드래그 경로 추가

        # 선택된 숫자들을 기록 (중복 선택 방지)
        for r, c, _, _ in best_choice:
            grid[r][c][0] = None

    return solution