


def clean_json_content(content):
	"""
	주어진 JSON 내용에서 tab, new line, 마지막 ','를 제거한다.

	Parameters:
		content (str): 원본 JSON 문자열

	Returns:
		str: 정리된 JSON 문자열
	"""
	# tab과 new line 제거
	cleaned_content = content.replace("\t", "").replace("\n", "")

	# 마지막 ',' 제거
	if cleaned_content[-2] == ',':
		cleaned_content = cleaned_content[:-2] + "}"

	return cleaned_content


def read_and_clean_json_file(file_path):
	"""
	JSON 파일을 읽고, 특정 문자를 제거한 뒤 딕셔너리로 반환한다.

	Parameters:
		file_path (str): 읽을 JSON 파일의 경로

	Returns:
		dict: 정리된 JSON 파일의 내용을 담은 딕셔너리
	"""
	with open(file_path, 'r', encoding='utf-8') as f:
		raw_content = f.read()

	# JSON 내용 정리
	cleaned_content = clean_json_content(raw_content)

	# 정리된 내용을 딕셔너리로 변환
	data = json.loads(cleaned_content)
	return data
