import json
from typing import Dict, List, Generator, Optional

class ChangeFilter:
    """
    변화량 기반 필터링 클래스
    - param별 마지막 값을 기억하고
    - 임계값(threshold) 이상 차이나면 결과로 내보냄
    """

    def __init__(self, threshold: float):
        self.threshold = threshold
        self.last_values: Dict[str, float] = {}

    def process(self, entry: Dict[str, float]) -> Optional[Dict[str, float]]:
        """
        개별 데이터 한 건 처리
        entry 예시: {"param": "A", "time": 0.01, "value": 100.2}
        변화량이 threshold 이상이면 그대로 반환, 아니면 None
        """
        param = entry["param"]
        value = entry["value"]

        if param not in self.last_values:
            self.last_values[param] = value
            return entry

        delta = abs(value - self.last_values[param])
        if delta >= self.threshold:
            self.last_values[param] = value
            return entry
        return None

    def process_stream(self, data: List[Dict[str, float]]) -> List[Dict[str, float]]:
        """리스트 형태의 입력 처리"""
        result = []
        for entry in data:
            filtered = self.process(entry)
            if filtered:
                result.append(filtered)
        return result

    def stream_generator(self, data: List[Dict[str, float]]) -> Generator[Dict[str, float], None, None]:
        """제너레이터 버전 (대용량 실시간 스트림용)"""
        for entry in data:
            filtered = self.process(entry)
            if filtered:
                yield filtered
# === 테스트용 실행 ===
if __name__ == "__main__":
    data = [
        {"param": "A", "time": 0.01, "value": 100.0},
        {"param": "A", "time": 0.02, "value": 100.0},
        {"param": "A", "time": 0.03, "value": 100.6},
    ]

    cf = ChangeFilter(threshold=0.2)
    print(json.dumps(cf.process_stream(data), indent=2))