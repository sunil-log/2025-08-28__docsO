#!/bin/bash

# --- 1. 백업 코멘트 입력받기 ---
# 사용자에게 백업에 대한 설명을 입력받습니다.
# 입력이 없으면 "no_comment"로 기본값을 설정합니다.
read -p "백업에 대한 코멘트를 입력하세요 (예: refactor_main_logic): " comment
comment=${comment:-no_comment}

# --- 2. 파일명 및 경로 설정 ---
# YYYY-MM-DD_HH-MM-SS 형식으로 현재 날짜와 시간을 가져옵니다.
current_datetime=$(date +%Y-%m-%d_%H-%M-%S)
# 최종 백업 파일명을 형식에 맞게 조합합니다.
zip_filename="backup_${current_datetime}_${comment}.zip"
# 백업 파일을 저장할 디렉터리를 지정합니다. (없으면 생성)
output_dir="./backups"
mkdir -p "$output_dir"
zip_filepath="${output_dir}/${zip_filename}"


# --- 3. 백업할 파일 목록 정의 ---
# 'git ls-files'를 사용하여 Git이 추적하는 모든 파일 목록을 가져옵니다.
# 이 방법은 .gitignore에 명시된 불필요한 파일(예: venv, __pycache__, 로그)을
# 자동으로 제외하므로, 순수 소스 코드만 백업하는 데 가장 효과적입니다.
files_to_backup=$(git ls-files)


# --- 4. ZIP 압축 실행 ---
# 정의된 파일 목록을 사용하여 ZIP 파일을 생성합니다.
# -@ 옵션은 표준 입력으로부터 파일 목록을 읽어 처리합니다.
echo "$files_to_backup" | zip -@ "$zip_filepath"

# --- 5. 완료 메시지 출력 ---
# 성공적으로 백업이 완료되었음을 사용자에게 알립니다.
echo ""
echo "✅ 백업이 성공적으로 완료되었습니다."
echo "   - 파일: ${zip_filepath}"
echo ""
