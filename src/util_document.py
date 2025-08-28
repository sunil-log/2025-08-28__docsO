from datetime import datetime
from pathlib import Path


class Document:
	"""
	Document 클래스는 문서 제목과 태그를 입력받아, 특정 디렉토리에 관련된 Markdown 파일을 생성하는 기능을 제공합니다.

	Attributes:
	- doc_title (str): 문서의 제목
	- tags (str): 문서의 태그들(콤마로 구분)
	- processed_tags (list): process_tags 메서드를 통해 변환된 태그 리스트
	- docsO_dir (str): Obsidian 문서가 저장될 상위 디렉토리 경로
	- current_dir (str): 현재 시간을 기반으로 생성한 디렉토리 이름
	- dir_path (Path): 생성할 디렉토리의 전체 경로

	Methods:
	- generate_doc_title_date(): 현재 날짜와 doc_title을 결합하여 제한된 길이의 문자열을 반환
	- create_dir(): doc_title_date를 이름으로 하는 디렉토리를 생성
	- create_page(): 생성된 디렉토리에 Markdown 파일을 작성
	- process_tags(): 입력된 태그들을 가공하여 리스트로 반환
	"""


	def __init__(self):
		"""
		Document 클래스 초기화

		Parameters:
		- doc_title (str): 문서의 제목
		- tags (str): 문서의 태그들, 콤마로 구분
		"""

		self.tags = 'tag1, tag2'
		self.processed_tags = self.process_tags()

		self.docsO_dir = "/home/sac/Dropbox/Obsidian/docsO"

		self.current_dir = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
		self.today = datetime.now().strftime('%Y-%m-%d')
		self.time = datetime.now().strftime('%H-%M-%S')
		self.dir_path = Path(f"{self.docsO_dir}/{self.current_dir}")

		self.doc_title = f"result, project, {self.today}, untitled ({self.time})"



	def create_dir(self):
		"""
		doc_title_date를 이름으로 하는 디렉토리를 생성.
		이미 존재한다면 프로그램을 종료한다.
		"""

		if self.dir_path.exists():
			print(f"디렉토리 '{self.dir_path}' 이미 존재합니다.")
			sys.exit()
		else:
			self.dir_path.mkdir()

	def create_page(self):
		"""
		doc_title_date.md 파일을 생성하고 기본 정보를 쓴다.
		"""
		md_file_path = self.dir_path / f"{self.doc_title}.md"

		d = {
			"Title": self.doc_title,
			"Created Time": datetime.now(),
			"tags": self.processed_tags,
			"Previous Page": "empty",
			"Next Page": "empty",
		}

		# 딕셔너리를 YAML 스타일 문자열로 변환
		d_yaml = "---\n" + "\n".join([f"{key}: {value}" for key, value in d.items()]) + "\n---\n"

		# dataview script
		dv1 = """\n```table-of-contents\nmaxLevel: 2\n```\n\n\n\nWrite Contents Here!\n\n\n\n```dataview\nTABLE FROM #stared\n```\n\n```dataview\nTABLE dateformat(file.mtime, "dd.MM.yyyy - HH:mm") AS "Last modified" FROM "" SORT file.mtime DESC LIMIT 10\n```"""

		with md_file_path.open('w') as f:
			f.write(d_yaml)
			f.write(dv1)

	def process_tags(self):
		"""
		입력된 태그를 콤마로 분리하고, 공백은 '-'로 대체한 후, 모든 문자를 소문자로 바꾼 리스트로 반환한다.
		맨 앞이나 맨 뒤에 있는 '-'는 제거한다.

		Returns:
		- processed_tags (list): 처리된 태그 리스트
		"""
		processed_tags = []
		for tag in self.tags.split(','):
			tag = tag.replace(' ', '-').lower()
			tag = tag.strip('-')
			processed_tags.append(tag)
		return processed_tags



