import argparse
from util_document import Document
from utils.control_ubuntu.clipboard import copy_to_clipboard
from pathlib import Path

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Create a new document page and a symbolic link.")
	parser.add_argument('--tags', type=str, default='tag1, tag2', help='Comma-separated tags for the document.')
	parser.add_argument('--obsidian-dir', type=str, default="/home/sac/Dropbox/Obsidian/docsO",
	                    help='The base directory for Obsidian documents.')
	parser.add_argument('--downloads-dir', type=str, default="/home/sac/Downloads",
	                    help='The directory to create a symbolic link in.')
	args = parser.parse_args()

	# 1. prefix 선택
	prefix_choice = input("Select a prefix:\n1: result, project\n2: memo\nEnter number: ")
	if prefix_choice == '1':
		prefix = "result, project"
	elif prefix_choice == '2':
		prefix = "memo"
	else:
		print("Invalid selection. Exiting.")
		exit()

	# 2. title 입력
	title = input("Enter title (press Enter for 'untitled'): ")
	if not title.strip():
		title = None

	# make a page
	document = Document(
		title=title,
		tags=args.tags,
		obsidian_dir=args.obsidian_dir,
		prefix=prefix
	)
	document.create_dir()
	document.create_page()

	print(f"새로운 페이지: {document.doc_title}")
	print(f"처리된 태그: {document.processed_tags}")

	# copy to clipboard
	copy_to_clipboard(f"[[{document.doc_title}]]")
	print(f"[[{document.doc_title}]] copied to clipboard")

	# 지정된 파일에 [[title]] 추가 - "# New" 라인 다음에 삽입
	dashboard_path = "/home/sac/Dropbox/Obsidian/docsO/2024-11-02-17-17-38/dashboard, memo.md"
	try:
		with open(dashboard_path, "r") as dashboard_file:
			lines = dashboard_file.readlines()
		
		# "# New" 라인을 찾아서 그 다음에 새 링크 삽입
		new_lines = []
		inserted = False
		for line in lines:
			new_lines.append(line)
			if line.strip() == "# New" and not inserted:
				new_lines.append(f"[[{document.doc_title}]]\n")
				inserted = True
		
		# "# New" 라인을 찾지 못한 경우 맨 끝에 추가
		if not inserted:
			new_lines.append(f"\n[[{document.doc_title}]]")
		
		with open(dashboard_path, "w") as dashboard_file:
			dashboard_file.writelines(new_lines)
		
		print(f"Inserted after '# New' in dashboard: {dashboard_path}")
	except FileNotFoundError:
		print(f"Error: Dashboard file not found at {dashboard_path}")

	# 심볼릭 링크를 생성할 경로와 원본 디렉토리 경로를 정의합니다.
	downloads_dir = Path(args.downloads_dir)
	original_dir_path = document.dir_path

	# title이 없는 경우 'untitled'를 사용합니다.
	link_title = title if title else "untitled"
	symlink_name = f"{original_dir_path.name}__{link_title}"
	symlink_path = downloads_dir / symlink_name

	# 심볼릭 링크를 생성합니다.
	symlink_path.symlink_to(original_dir_path)
	print(f"Symbolic link created: {symlink_path} -> {original_dir_path}")