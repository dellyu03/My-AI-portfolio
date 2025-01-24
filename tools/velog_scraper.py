from bs4 import BeautifulSoup
import requests
from typing import Dict, Optional
from pydantic import BaseModel


class VelogContent(BaseModel):
    """벨로그 컨텐츠를 담는 Pydantic 모델"""
    title: str
    content: str
    error: Optional[str] = None


class VelogScraperTool:
    """벨로그 게시글 스크래핑을 위한 도구"""

    def __init__(self):
        """스크래퍼 초기화"""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()

    def _clean_text(self, text: str) -> str:
        """텍스트 정제"""
        return ' '.join(text.split())

    def _extract_content(self, soup: BeautifulSoup) -> Dict:
        """페이지에서 컨텐츠 추출"""
        try:
            # 제목 추출
            title_elem = soup.select_one('.head-wrapper h1')
            if not title_elem:
                raise ValueError("제목을 찾을 수 없습니다")
            title = title_elem.text.strip()

            # 본문 추출
            content_elem = soup.select_one('.sc-eGRUor.gdnhbG.atom-one')
            if not content_elem:
                raise ValueError("본문을 찾을 수 없습니다")
            
            # 본문의 모든 텍스트 추출
            content = content_elem.get_text(separator='\n', strip=True)

            return {
                "title": self._clean_text(title),
                "content": content
            }
            
        except Exception as e:
            return {"error": f"컨텐츠 추출 실패: {str(e)}"}

    def scrape(self, url: str) -> VelogContent:
        """벨로그 글 스크래핑 실행"""
        try:
            # 페이지 요청
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # 컨텐츠 추출
            soup = BeautifulSoup(response.text, 'html.parser')
            content = self._extract_content(soup)
            
            # 에러 확인
            if "error" in content:
                return VelogContent(
                    title="",
                    content="",
                    error=content["error"]
                )
            
            return VelogContent(**content)
            
        except requests.RequestException as e:
            return VelogContent(
                title="",
                content="",
                error=f"요청 실패: {str(e)}"
            )


if __name__ == "__main__":
    # 테스트
    scraper = VelogScraperTool()
    test_url = "https://velog.io/@endmoseung/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85%EC%97%90%EC%84%9C-%EB%94%94%EC%9E%90%EC%9D%B8%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%B4%EB%9E%80"
    result = scraper.scrape(test_url)
    
    if result.error:
        print(f"Error: {result.error}")
    else:
        print(f"제목: {result.title}")
        print("\n--- 본문 미리보기 ---")
        print(f"{result.content[:500]}...")