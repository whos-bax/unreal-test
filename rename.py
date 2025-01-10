import os
import shutil


# 파일이 저장된 폴더 경로
name="scenario_3"
folder_path = f"/Users/whosbax/Documents/GitHub/unreal-test/cesium1/Saved/MovieRenders/{name}"  # 이미지가 있는 폴더 경로를 입력하세요.
output_folder = f"/Users/whosbax/Documents/GitHub/unreal-test/cesium1/Saved/MovieRenders/{name}"  # 결과 파일들이 저장될 상위 폴더 경로

# 파일 이름 변경 및 이동 함수
def rename_and_move_files(folder_path, output_folder):
    files = sorted(os.listdir(folder_path))  # 파일 목록 정렬
    counters = {"day": 1, "night": 1, "hl": 1}  # 카테고리별 카운터 초기화
    categories = ["day", "night", "hl"]  # 카테고리 목록

    # 카테고리별 폴더 생성
    for category in categories:
        category_folder = os.path.join(output_folder, f"{name}_{category}")
        os.makedirs(category_folder, exist_ok=True)

    # sample_videos 폴더 생성
    sample_videos_folder = os.path.join(output_folder, "sample_videos")
    os.makedirs(sample_videos_folder, exist_ok=True)

    for filename in files:
        # 기존 파일 경로
        old_file_path = os.path.join(folder_path, filename)

        if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")) or "video" in filename.lower():
            # 영상 파일 이동
            new_file_path = os.path.join(sample_videos_folder, filename)
            shutil.move(old_file_path, new_file_path)
            print(f"Moved video file: {filename} -> {new_file_path}")

        elif filename.endswith(".png"):  # .png 파일만 처리
            # 파일 이름에 따라 카테고리 결정
            if "day" in filename.lower():
                category = "day"
                new_filename = f"{name}_day_{counters[category]:010d}.png"
            elif "night" in filename.lower():
                category = "night"
                new_filename = f"{name}_night_{counters[category]:010d}.png"
            elif "hl" in filename.lower():  # hl 포함
                category = "hl"
                new_filename = f"{name}_hl_{counters[category]:010d}.png"
            else:
                # 카테고리에 속하지 않는 경우 스킵
                print(f"Skipped: {filename}")
                continue

            # 카운터 증가
            counters[category] += 1

            # 새로운 파일 경로 및 이동할 폴더 설정
            new_file_path = os.path.join(output_folder, f"{name}_{category}", new_filename)

            # 파일 이름 변경 및 이동
            shutil.move(old_file_path, new_file_path)
            print(f"Renamed and Moved: {filename} -> {new_file_path}")

# 실행
rename_and_move_files(folder_path, output_folder)