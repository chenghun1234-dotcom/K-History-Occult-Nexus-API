import json

def generate_detailed_wars():
    data = [
        {
            "id": "K-WAR-001",
            "event_name": {"ko": "고조선-한 전쟁 (왕검성 함락)", "en": "Gojoseon-Han War (Fall of Wanggeom-seong)"},
            "location": {"name": {"ko": "왕검성 (평양 부근)", "en": "Wanggeom-seong (Pyongyang)"}, "coordinates": {"lat": 39.033, "lng": 125.75}},
            "significance": {"ko": "기원전 108년, 고대 한국 최초의 국가 고조선의 멸망과 한사군 설치.", "en": "108 BC, fall of Gojoseon, Korea's first state, and establishment of Han Commanderies."},
            "occult_factor": {"ko": "멸망 전날 밤 지하에서 들려온 울음소리와 하늘에서 떨어진 거대 운석이 왕궁을 타격했다는 설화.", "en": "Legend says wailing arose from the underground and a massive meteor struck the palace before the fall."},
            "figures": [
                {"name": {"ko": "우거왕", "en": "King Ugeo"}, "role": {"ko": "고조선의 마지막 왕", "en": "Last King of Gojoseon"}, "anecdote": {"ko": "강력한 항전 의지를 보였으나 내부 배신자에 의해 암살당함.", "en": "Assassinated by internal traitors despite strong will to resist."}},
                {"name": {"ko": "성기 장군", "en": "General Seong-gi"}, "role": {"ko": "항전 지휘관", "en": "Resistance Commander"}, "anecdote": {"ko": "왕이 죽은 후에도 끝까지 성을 지키며 항전한 충신.", "en": "A loyalist who defended the fortress to the end even after the King's death."}}
            ],
            "detailed_records": [
                {"title": {"ko": "내부의 분열 (삼로인)", "en": "Internal Betrayal (Sam-ro-in)"}, "content": {"ko": "고조선의 고위 관료들이 한나라의 회유에 넘어가 우거왕을 배신하고 탈출함.", "en": "High officials betrayed King Ugeo and defected to the Han Dynasty under inducement."}}
            ],
            "game_stats": {"strategy": 7, "difficulty": 10, "recommended_items": [{"ko": "청동거울", "en": "Bronze Mirror"}]},
            "verified": True, "is_fiction": False
        },
        {
            "id": "K-WAR-002",
            "event_name": {"ko": "고구려-수 전쟁 (살수대첩)", "en": "Goguryeo-Sui War (Battle of Salsu)"},
            "location": {"name": {"ko": "청천강 (살수)", "en": "Cheongcheon River (Salsu)"}, "coordinates": {"lat": 39.71, "lng": 125.75}},
            "significance": {"ko": "수나라 113만 대군을 격퇴하여 중국 수나라 왕조 멸망의 도화선이 됨.", "en": "Repelled 1.13 million Sui troops, leading to the eventual collapse of the Sui Dynasty."},
            "occult_factor": {"ko": "을지문덕의 부채가 한 번 흔들리면 강물이 갈라지고, 두 번 흔들리면 폭우가 쏟아졌다는 도술적 전설.", "en": "Legend says Eulji Mundeok's fan could part rivers and summon torrential rain with a single wave."},
            "figures": [
                {"name": {"ko": "을지문덕", "en": "Eulji Mundeok"}, "role": {"ko": "수수군 대총관", "en": "Grand Commander of Goguryeo"}, "anecdote": {"ko": "적장에게 '여수장우중문시'를 보내 조롱하며 심리전을 펼침.", "en": "Sent a mocking poem to General Yu Zhongwen to provoke and manipulate the enemy."}}
            ],
            "detailed_records": [
                {"title": {"ko": "청야 전술의 극치", "en": "Mastery of Scorch-Earth"}, "content": {"ko": "수나라 보급로를 완전히 차단하여 30만 별동대를 기아 상태로 몰아넣음.", "en": "Completely cut Sui supply lines, driving 300,000 elite troops into starvation."}}
            ],
            "game_stats": {"strategy": 10, "difficulty": 6, "recommended_items": [{"ko": "청야의 주문서", "en": "Scroll of Scorched Earth"}]},
            "verified": True, "is_fiction": False
        },
        {
            "id": "K-WAR-003",
            "event_name": {"ko": "고구려-당 전쟁 (안시성 전투)", "en": "Goguryeo-Tang War (Battle of Ansi)"},
            "location": {"name": {"ko": "안시성 (해성/개평)", "en": "Ansi Fortress (Haicheng)"}, "coordinates": {"lat": 40.48, "lng": 122.58}},
            "significance": {"ko": "60여 일간의 처절한 수성전 끝에 당 태종의 직접 침공을 막아냄.", "en": "Stopped Emperor Taizong's personal invasion after 60 days of brutal siege defense."},
            "occult_factor": {"ko": "당나라군이 쌓은 토산이 무너질 때 하늘에서 거대한 용의 포효가 들렸다는 기록.", "en": "Records state the roar of a giant dragon was heard from the sky when the Tang rampart collapsed."},
            "figures": [
                {"name": {"ko": "양만춘 (성주)", "en": "Yang Man-chun"}, "role": {"ko": "안시성 성주", "en": "Fortress Master"}, "anecdote": {"ko": "당 태종의 눈을 화살로 맞추어 퇴각시켰다는 민간 전승.", "en": "Folk legend says he shot Emperor Taizong in the eye with an arrow, forcing retreat."}}
            ],
            "detailed_records": [
                {"title": {"ko": "토산의 붕괴와 기습", "en": "Collapse of the Earth Rampart"}, "content": {"ko": "당나라가 3개월간 쌓은 토산이 무너지자 고구려군이 즉각 점령하여 요새화함.", "en": "When the rampart collapsed after 3 months of construction, Goguryeo troops seized and fortified it."}}
            ],
            "game_stats": {"strategy": 8, "difficulty": 9, "recommended_items": [{"ko": "궁극의 수성궁", "en": "Ultimate Siege-Defense Bow"}]},
            "verified": True, "is_fiction": False
        },
        {
            "id": "K-WAR-004",
            "event_name": {"ko": "나당 전쟁 (매소성/기벌포)", "en": "Silla-Tang War (Maeso/Gibeolpo)"},
            "location": {"name": {"ko": "매소성 (연천)", "en": "Maeso Fortress (Yeoncheon)"}, "coordinates": {"lat": 37.95, "lng": 126.9}},
            "significance": {"ko": "당나라의 20만 대군을 격파하고 한반도에서의 당 세력을 완전히 축출.", "en": "Crushed 200,000 Tang troops, completely ousting Tang forces from the peninsula."},
            "occult_factor": {"ko": "삼국 유사에 따르면 신라 병사들이 사천왕사에서 올린 비술로 당나라 함대가 침몰함.", "en": "According to Samguk Yusa, secret occult arts performed at Sacheonwang Temple sank the Tang fleet."},
            "figures": [
                {"name": {"ko": "이근행", "en": "Li Jinxing"}, "role": {"ko": "당나라 장수", "en": "Tang General"}, "anecdote": {"ko": "매소성에서 신라군에 대패하여 3만 380필의 말을 잃고 도주함.", "en": "Abandoned 30,380 horses and fled after a crushing defeat by Silla."}}
            ],
            "detailed_records": [
                {"title": {"ko": "3만 380필의 군마 노획", "en": "Capture of 30,380 Horses"}, "content": {"ko": "삼국사기 기록에 따르면 신라군이 매소성에서 노획한 전리품의 규모는 역사상 최대 수준.", "en": "Per Samguk Sagi, Silla captured more war trophies at Maeso than in any other single battle."}}
            ],
            "game_stats": {"strategy": 9, "difficulty": 8, "recommended_items": [{"ko": "사천왕의 부적", "en": "Talisman of Four Kings"}]},
            "verified": True, "is_fiction": False
        },
        {
            "id": "K-WAR-005",
            "event_name": {"ko": "여요 전쟁 (귀주대첩)", "en": "Goryeo-Khitan War (Battle of Gwiju)"},
            "location": {"name": {"ko": "귀주 (구성)", "en": "Gwiju (Kuseong)"}, "coordinates": {"lat": 39.9, "lng": 125.1}},
            "significance": {"ko": "고려를 침공한 10만 거란군 중 단 수천 명만이 살아 돌아갈 정도로 완승.", "en": "A perfect victory where only a few thousand of 100,000 Khitan invaders survived."},
            "occult_factor": {"ko": "강감찬 장군이 칼을 뽑자 갑자기 비바람의 방향이 거란군 쪽으로 바뀌었다는 '귀주의 기적'.", "en": "The 'Miracle of Gwiju' where rain and wind suddenly shifted towards the Khitan when Gang Gam-chan drew his sword."},
            "figures": [
                {"name": {"ko": "강감찬", "en": "Gang Gam-chan"}, "role": {"ko": "상원수", "en": "Grand Marshal of Goryeo"}, "anecdote": {"ko": "별의 기운을 타고난 문관 출신 장군으로, 여우의 자식이라는 설화가 있음.", "en": "A civil official general born of star energy; legends claim he was a descendant of a fox."}}
            ],
            "detailed_records": [
                {"title": {"ko": "흥화진 수공", "en": "Heunghwajin Water Tactic"}, "content": {"ko": "소가죽으로 강물을 막았다가 일시에 터뜨려 거란군의 도하를 저지함.", "en": "Blocked the river with ox hides and released it simultaneously to drown crossing Khitan troops."}}
            ],
            "game_stats": {"strategy": 10, "difficulty": 7, "recommended_items": [{"ko": "수공의 가죽", "en": "Water-Tactics Hide"}]},
            "verified": True, "is_fiction": False
        },
        {
            "id": "K-WAR-1592-UNGCHI",
            "event_name": {"ko": "임진왜란 웅치전투", "en": "Battle of Ungchi (Imjin War)"},
            "location": {"name": {"ko": "전주 웅치고개", "en": "Ungchi Pass, Jeonju"}, "coordinates": {"lat": 35.84, "lng": 127.24}},
            "significance": {"ko": "전주성을 지키기 위해 고개에서 벌인 처절한 사투. 호남 방어의 결정적 계기.", "en": "A brutal struggle at the pass to protect Jeonju Fortress, critical for Honam's defense."},
            "occult_factor": {"ko": "전사한 의병들의 영혼이 밤마다 웅치에 모여 아직도 정찰을 돌고 있다는 '망군' 전설.", "en": "Legend of the 'Spirit Army' where fallen righteous soldiers continue their patrols every night at the pass."},
            "figures": [
                {"name": {"ko": "정담 (김제군수)", "en": "Jeong Dam"}, "role": {"ko": "김제 군수", "en": "Magistrate of Gimje"}, "anecdote": {"ko": "적의 대군 앞에서 '나는 여기서 죽을 뿐이다'라며 끝까지 고개를 지킨 명장.", "en": "Repelled countless waves saying 'I will only die here' before falling heroically."}}
            ],
            "detailed_records": [
                {"title": {"ko": "조선군의 결사항전", "en": "Joseon's Final Stand"}, "content": {"ko": "화살이 다 떨어지자 돌을 던지며 저항했고, 전원이 고개 위에서 장렬히 전사함.", "en": "When arrows ran out, they threw stones and fought until every single soldier fell at the pass."}}
            ],
            "game_stats": {"strategy": 9, "difficulty": 10, "recommended_items": [{"ko": "정담의 철구", "en": "Jeong Dam's Iron Mace"}]},
            "verified": True, "is_fiction": False
        }
    ]
    with open("data/comprehensive_wars.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_detailed_wars()
