from util_document import Document
from util_sac.control_ubuntu.clipboard import copy_to_clipboard
from pathlib import Path # 👈 1. Path 객체를 사용하기 위해 import 합니다.


if __name__ == '__main__':

	# make a page
	document = Document()
	document.create_dir()
	document.create_page()

	print(f"새로운 페이지: {document.doc_title}")
	print(f"처리된 태그: {document.processed_tags}")

	# copy to clipboard
	copy_to_clipboard(f"[[{document.doc_title}]]")
	print(f"[[{document.doc_title}]] copied to clipboard")
 
	# 👇 2. 아래 코드를 추가합니다.
	# 심볼릭 링크를 생성할 경로와 원본 디렉토리 경로를 정의합니다.
	downloads_dir = Path("/home/sac/Downloads")
	original_dir_path = document.dir_path
	symlink_path = downloads_dir / original_dir_path.name

	# 심볼릭 링크를 생성합니다.
	symlink_path.symlink_to(original_dir_path)
	print(f"Symbolic link created: {symlink_path} -> {original_dir_path}")
