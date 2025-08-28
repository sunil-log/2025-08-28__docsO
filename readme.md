# docsO

`docsO`는 Obsidian 문서 생성을 자동화하는 도구입니다. 사용자가 지정한 제목, 태그, 접두사를 기반으로 특정 구조를 갖춘 Markdown 파일을 생성하고, 관련 디렉토리 및 심볼릭 링크를 자동으로 관리하여 문서 작업을 효율적으로 만들어 줍니다.

## 주요 기능

  * **템플릿 기반 문서 생성**: 지정된 형식에 따라 YAML frontmatter와 dataview 스크립트가 포함된 Markdown 파일을 생성합니다.
  * **자동 디렉토리 관리**: 현재 시간을 기준으로 고유한 디렉토리를 생성하여 문서를 체계적으로 관리합니다.
  * **태그 자동 처리**: 콤마로 구분된 태그를 입력하면, 공백을 하이픈(-)으로 바꾸고 소문자로 변환하는 등 정해진 형식으로 자동 처리합니다.
  * **클립보드 연동**: 생성된 문서의 링크(`[[문서 제목]]`)를 클립보드에 자동으로 복사하여 다른 문서에서 바로 참조할 수 있도록 돕습니다.
  * **심볼릭 링크 생성**: Downloads 폴더에 문서 디렉토리로 바로 갈 수 있는 심볼릭 링크를 생성하여 접근성을 높입니다.
  * **백업 스크립트**: `git`이 추적하는 모든 파일을 zip 형식으로 압축하여 간편하게 백업할 수 있는 셸 스크립트를 제공합니다.

## 파일 구성

  * **`src/docsO-create.py`**: 메인 실행 스크립트입니다. 사용자로부터 접두사, 제목, 태그 등의 정보를 입력받아 문서를 생성합니다.
  * **`src/util_document.py`**: `Document` 클래스가 정의된 모듈입니다. 실제 디렉토리와 Markdown 파일을 생성하는 핵심 로직을 포함합니다.
  * **`src/utils/control_ubuntu/clipboard.py`**: `xclip`을 이용해 생성된 문서 링크를 클립보드에 복사하는 유틸리티 함수를 제공합니다.
  * **`backup_git.sh`**: `git ls-files` 명령어로 추적되는 모든 파일을 zip으로 압축하여 백업하는 셸 스크립트입니다.

## 사용법

### 요구 사항

  * Python 3
  * `xclip`: 클립보드 연동 기능을 사용하기 위해 필요합니다. Ubuntu에서는 다음 명령어로 설치할 수 있습니다.
    ```bash
    sudo apt-get update
    sudo apt-get install xclip
    ```

### 실행

1.  터미널에서 `src` 디렉토리로 이동합니다.

2.  아래 명령어를 실행합니다.

    ```bash
    python docsO-create.py --tags "태그1, 태그2"
    ```

      * `--tags`: 문서에 추가할 태그를 콤마로 구분하여 입력합니다. (기본값: 'tag1, tag2')
      * `--obsidian-dir`: Obsidian 문서가 저장될 기본 디렉토리를 지정합니다. (기본값: "/home/sac/Dropbox/Obsidian/docsO")
      * `--downloads-dir`: 심볼릭 링크를 생성할 디렉토리를 지정합니다. (기본값: "/home/sac/Downloads")

3.  스크립트가 실행되면 접두사(prefix)를 선택하라는 메시지가 나타납니다.

    ```
    Select a prefix:
    1: result, project
    2: memo
    Enter number:
    ```

4.  문서 제목을 입력합니다. 제목을 입력하지 않고 Enter를 누르면 'untitled'로 자동 설정됩니다.

    ```
    Enter title (press Enter for 'untitled'):
    ```

5.  실행이 완료되면 지정된 경로에 문서와 디렉토리가 생성되고, 문서 링크가 클립보드에 복사됩니다.

### 백업

프로젝트의 루트 디렉토리에서 아래 명령어를 실행하면 `backups` 폴더 안에 압축 파일이 생성됩니다.

```bash
./backup_git.sh
```