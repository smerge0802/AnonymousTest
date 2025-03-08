import time
from capture_screen import capture_screen, preprocess_image
from digit_recognition import extract_digits, construct_fixed_grid, check_digit_balance
from solver import find_solution
from automation import execute_drag

def validate() :
    print("📝\t검증 중...")
    image = capture_screen()
    processed_image = preprocess_image(image)
    digit_data = extract_digits(processed_image)
    grid = construct_fixed_grid(digit_data)

    solution = find_solution(grid)
    if len(solution) == 0 :
        print("☑️\t가능한 조합이 존재하지 않습니다!")
    else :
        print("🆘\t가능한 조합이 존재합니다!")
        execute_drag(solution)

def main():
    time.sleep(2) # 사용자가 화면을 준비할 시간 제공
    image = capture_screen()
    processed_image = preprocess_image(image)
    digit_data = extract_digits(processed_image)
    # check_digit_balance(digit_data)
    grid = construct_fixed_grid(digit_data)

    solution = find_solution(grid)
    execute_drag(solution)

    validate()

if __name__ == "__main__":
    main()
