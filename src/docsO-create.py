import argparse
from util_document import Document
from utils.control_ubuntu.clipboard import copy_to_clipboard
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a new document page and a symbolic link.")
    parser.add_argument('--tags', type=str, default='tag1, tag2', help='Comma-separated tags for the document.')
    parser.add_argument('--obsidian-dir', type=str, default="/home/sac/Dropbox/Obsidian/docsO", help='The base directory for Obsidian documents.')
    parser.add_argument('--downloads-dir', type=str, default="/home/sac/Downloads", help='The directory to create a symbolic link in.')
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

    # 심볼릭 링크를 생성할 경로와 원본 디렉토리 경로를 정의합니다.
    downloads_dir = Path(args.downloads_dir)
    original_dir_path = document.dir_path
    symlink_path = downloads_dir / original_dir_path.name

    # 심볼릭 링크를 생성합니다.
    symlink_path.symlink_to(original_dir_path)
    print(f"Symbolic link created: {symlink_path} -> {original_dir_path}")