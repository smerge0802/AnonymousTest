# 🍏 fruit-box-bot

이 프로젝트는 **"Fruit Box" 게임 자동화를 위한 Python 기반의 봇**입니다.  
스크린 캡처, 숫자 인식, 자동 드래그를 통해 게임을 자동으로 진행합니다.
게임은 [해당 링크](https://www.gamesaien.com/game/fruit_box_a/)에서 플레이할 수 있습니다.

---

## 📂 프로젝트 구조

### 📁 `img/`

- **숫자 인식용 학습 데이터 및 샘플 이미지 저장 폴더**
- `digit_recognition.py`에서 사용됩니다.

### 📝 주요 코드 파일

| 파일명                     | 설명                                               |
| -------------------------- | -------------------------------------------------- |
| **`main.py`**              | 🚀 프로젝트의 실행 진입점                          |
| **`automation.py`**        | 🎮 게임 자동 플레이 로직                           |
| **`capture_screen.py`**    | 🖥️ 게임 화면을 캡처하는 모듈                       |
| **`constant.py`**          | ⚙️ 프로젝트 전역 설정 값 저장 (예: 해상도, 딜레이) |
| **`digit_recognition.py`** | 🔢 숫자를 인식하고 그리드 데이터를 변환            |
| **`solver.py`**            | 🧠 최적의 드래그 경로를 계산하는 알고리즘          |

---

## 🚀 실행 방법

1️⃣ 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

2️⃣ `main.py`를 실행하여 자동화 봇을 시작합니다.

```bash
python main.py
```

---

## ⚙️ 주요 기능

✅ **스크린 캡처:** `capture_screen.py`를 이용해 게임 화면을 캡처  
✅ **숫자 인식:** `digit_recognition.py`에서 OCR을 통해 숫자를 인식  
✅ **경로 계산:** `solver.py`에서 최적의 드래그 경로 탐색  
✅ **자동 실행:** `automation.py`에서 마우스 이벤트를 통해 게임 진행

---

🚀 **이제 `python main.py`를 실행하고 사과 게임을 자동으로 플레이하세요!** 🎮
