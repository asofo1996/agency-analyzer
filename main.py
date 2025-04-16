from fastapi import FastAPI, Query
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/crawl-agency")
def crawl_agency(url: str = Query(..., example="https://www.ablelab.co.kr")):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else "제목 없음"
        h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]

        return {
            "agency_name": title,
            "positioning": h1_tags[0] if h1_tags else "분석 실패",
            "key_services": ["예시 서비스 A", "예시 서비스 B"],
            "content_structure": "페이지 흐름 분석 결과",
            "branding_style": "깔끔한 이미지 기반",
            "strengths": ["이해하기 쉬움"],
            "weaknesses": ["모바일 최적화 부족"]
        }

    except Exception as e:
        return {"error": str(e)}
