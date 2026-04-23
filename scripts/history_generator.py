import json
import random

# Template for Shamanic/Occult Interpretation
OCCULT_TEMPLATES = [
    {"ko": "기이한 빛이 밤하늘을 덮었으며, 이를 목격한 자들은 원인 모를 열병에 시달림.", "en": "A strange light covered the night sky; witnesses suffered from an unknown fever."},
    {"ko": "땅에서 솟아오른 검은 그림자들이 행인들의 발목을 잡았다는 괴담이 실록에 기록됨.", "en": "Shadows rising from the ground grabbed the ankles of passersby according to official records."},
    {"ko": "특정 구역에 진입 시 나침반(지남반)이 거꾸로 회전하며 도깨비의 장난이 시작됨.", "en": "Compasses rotate backward upon entering specific zones, signaling Dokkaebi mischief."}
]

def generate_dark_history(count=10):
    data_list = []
    for i in range(1, count + 1):
        event_id = f"K-CHRON-{1400 + i}"
        occult = random.choice(OCCULT_TEMPLATES)
        
        entry = {
            "id": event_id,
            "event_name": {
                "ko": f"조선왕조실록 미스터리 사건 {i}호",
                "en": f"Joseon Chronicle Mystery Case #{i}"
            },
            "location": {
                "name": {"ko": "한양 도성 근방", "en": "Vicinity of Hanyang Fortress"},
                "coordinates": {"lat": 37.566 + (i * 0.01), "lng": 126.978 + (i * 0.01)}
            },
            "significance": {
                "ko": "조선 초기 기록된 기이한 천문 현상 또는 괴생명체 출현 기록.",
                "en": "Records of strange celestial phenomena or creature sightings in early Joseon."
            },
            "occult_factor": occult,
            "game_stats": {
                "strategy": random.randint(5, 10),
                "difficulty": random.randint(5, 10),
                "recommended_items": [{"ko": "사인검", "en": "Four Tigers Sword"}]
            },
            "verified": i % 2 == 0, # Simulating verification check
            "is_fiction": i % 2 != 0
        }
        data_list.append(entry)
    
    with open("data/history_data.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated {count} records in data/history_data.json")

if __name__ == "__main__":
    generate_dark_history(50)
