# analytics.py
import asyncio
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+
from typing import Dict, Any, List, Optional

import httpx
from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse

router = APIRouter()

# === КОНФИГ И ИСТОЧНИКИ ДАННЫХ ===

# Форматированный JSON Open LLM Leaderboard backend.
# URL взят из описания backend Space: /api/leaderboard/formatted. [web:128]
OPENLLM_LEADERBOARD_URL = (
    "https://open-llm-leaderboard-open-llm-leaderboard.hf.space/api/leaderboard/formatted"
)

# Таймауты и поведение при ошибках
HTTP_TIMEOUT = 20.0  # секунд


# === ГЛОБАЛЬНОЕ СОСТОЯНИЕ АНАЛИТИКИ ===

ANALYTICS_DB: Dict[str, Any] = {
    "last_updated": "11.12.2025 03:00 МСК",
    "summary": (
        "По состоянию на 11.12.2025, <b>Gemini 3 Pro</b> удерживает лидерство в глобальных "
        "рейтингах благодаря рекордам в научных бенчмарках (GPQA). "
        "Anthropic и DeepSeek продолжают ценовую конкуренцию в премиальном сегменте. "
        "В open‑source сегменте доминирует DeepSeek V3.2."
    ),
    # Отслеживаемые модели. Для некоторых добавляем ключ-идентификатор под leaderboard.
    "models": [
        {
            "rank": 1,
            "name": "Gemini 3 Pro",
            "vendor": "Google",
            "type": "Multimodal Native",
            "params": "≈2T+ (MoE)",
            "release": "18.11.2025",
            "status": "Лидер по reasoning",
            "change": "0",
            "desc": "Флагман Google. Сильнейшая на сложных задачах и научных бенчмарках.",
            "leaderboard_key": None,  # проприетарная модель, на Open LLM Leaderboard её нет
        },
        {
            "rank": 2,
            "name": "Claude 4.5 Opus",
            "vendor": "Anthropic",
            "type": "Agentic LLM",
            "params": ">1.5T (оценка)",
            "release": "24.11.2025",
            "status": "Лучший для кода и агентов",
            "change": "↑1",
            "desc": "Эталон по качеству кода и надежности цепочек рассуждений.",
            "leaderboard_key": None,
        },
        {
            "rank": 3,
            "name": "GPT-5.1 High",
            "vendor": "OpenAI",
            "type": "LLM",
            "params": "≈1.8T (оценка)",
            "release": "11.11.2025",
            "status": "Сбалансированный generalist",
            "change": "↓1",
            "desc": "Сильная модель для диалогов и креатива, немного уступает в науке.",
            "leaderboard_key": None,
        },
        {
            "rank": 4,
            "name": "Grok 4.1",
            "vendor": "xAI",
            "type": "LLM",
            "params": "≈1T",
            "release": "17.11.2025",
            "status": "Real‑time & uncensored",
            "change": "0",
            "desc": "Быстрый доступ к данным X в реальном времени, минимальная цензура.",
            "leaderboard_key": None,
        },
        {
            "rank": 5,
            "name": "DeepSeek V3.2",
            "vendor": "DeepSeek",
            "type": "MoE LLM",
            "params": "671B (39B active)",
            "release": "28.09.2025",
            "status": "Open‑source лидер",
            "change": "0",
            "desc": "Самая мощная открытая модель, выгодный инференс.",
            # Для open‑source моделей пытаемся мапиться по подстроке в поле Model/fullname. [web:106][web:108]
            "leaderboard_key": "deepseek-v3",
        },
        {
            "rank": 6,
            "name": "Kimi K2",
            "vendor": "Moonshot AI",
            "type": "LLM",
            "params": "Н/Д",
            "release": "примерно октябрь 2025 (оценка)",
            "status": "Long‑context (10M)",
            "change": "↑1",
            "desc": "Специализация на анализе сверхдлинных документов.",
            "leaderboard_key": None,
        },
        {
            "rank": 7,
            "name": "Llama 3.1‑405B",
            "vendor": "Meta",
            "type": "Dense LLM",
            "params": "405B",
            "release": "23.07.2024",
            "status": "Открытый флагман",
            "change": "↓1",
            "desc": "База для локального деплоя и файнтюнинга, уступает новым флагманам.",
            "leaderboard_key": "llama-3.1-405b",
        },
        {
            "rank": 8,
            "name": "Mistral Large 2",
            "vendor": "Mistral AI",
            "type": "LLM",
            "params": "123B",
            "release": "24.07.2024",
            "status": "Баланс цена/качество",
            "change": "0",
            "desc": "Мульти‑язычная модель с хорошим качеством кода и текста.",
            "leaderboard_key": "mistral-large-2",
        },
        {
            "rank": 9,
            "name": "Qwen3 Max",
            "vendor": "Alibaba",
            "type": "LLM",
            "params": "MoE (оценка)",
            "release": "05.11.2025",
            "status": "Enterprise‑фокус",
            "change": "NEW",
            "desc": "Ориентирована на корпоративные сценарии и RAG.",
            "leaderboard_key": "qwen3-max",
        },
        {
            "rank": 10,
            "name": "Gemini 2.5 Pro",
            "vendor": "Google",
            "type": "Multimodal",
            "params": "Н/Д",
            "release": "примерно апрель 2025 (по публичным источникам)",
            "status": "Предыдущее поколение",
            "change": "↓2",
            "desc": "Стабильное поколение, актуально за счет цены.",
            "leaderboard_key": None,
        },
    ],
    "news": [
        {
            "date": "10.12.2025",
            "title": "Gemini 3 Pro обновляет рекорд GPQA",
            "text": "Модель побила свой же рекорд в экспертных задачах GPQA, усилив отрыв от конкурентов."
        },
        {
            "date": "09.12.2025",
            "title": "Снижение цен на Claude 4.5 Opus",
            "text": "Anthropic уменьшили стоимость токенов на ~20% для крупных клиентов, реагируя на демпинг DeepSeek."
        },
        {
            "date": "10.12.2025",
            "title": "Анонс Llama 4 Small",
            "text": "Meta тизерит мультимодальную Llama 4 Small с релизом в январе 2026 года."
        },
        {
            "date": "08.12.2025",
            "title": "Grok 4.1 в Tesla Optimus",
            "text": "Облегченная версия Grok 4.1 используется в голосовом модуле робота Optimus Gen 3."
        },
    ],
}


# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ FETCH И АНАЛИТИКИ ===

async def fetch_openllm_leaderboard() -> Optional[Dict[str, Any]]:
    """
    Загружает форматированный JSON Open LLM Leaderboard.
    Если запрос не удался, возвращает None, чтобы не ломать дашборд. [web:106][web:128]
    """
    try:
        async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as client:
            resp = await client.get(OPENLLM_LEADERBOARD_URL)
            resp.raise_for_status()
            return resp.json()
    except Exception:
        return None


def find_lb_row_for_model(
    leaderboard_models: List[Dict[str, Any]],
    tracked: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    """
    Пытаемся сопоставить tracked‑модель строке из leaderboard:
    - если есть leaderboard_key, ищем по подстроке в 'Model' / 'fullname';
    - иначе пытаемся матчить по имени (подстрока).
    """
    key = tracked.get("leaderboard_key")
    name = tracked["name"].lower()

    for row in leaderboard_models:
        model_field = str(row.get("Model", "")).lower()
        fullname = str(row.get("fullname", "")).lower()

        if key:
            if key.lower() in model_field or key.lower() in fullname:
                return row
        else:
            if name.split()[0] in model_field or name.split()[0] in fullname:
                return row
    return None


def update_from_leaderboard(lb_data: Any):
    """
    Обновляет ранги на основе данных Open LLM Leaderboard.
    lb_data ожидается как список словарей (response API).
    """
    # API возвращает сразу список моделей, либо структуру, которую нужно проверить
    models_list = []
    if isinstance(lb_data, list):
        models_list = lb_data
    elif isinstance(lb_data, dict) and "models" in lb_data:
        models_list = lb_data["models"]
    elif isinstance(lb_data, dict) and "data" in lb_data:  # Иногда бывает обернуто в 'data'
        models_list = lb_data["data"]

    if not models_list:
        return

    # Сортировка по среднему скору (Average ⬆️) по убыванию
    sorted_lb = sorted(
        models_list,
        key=lambda m: m.get("Average ⬆️") if isinstance(m.get("Average ⬆️"), (int, float)) else 0.0,
        reverse=True,
    )

    # Карта: id строки -> глобальный ранг в leaderboard
    lb_rank_by_id: Dict[int, int] = {}
    for idx, row in enumerate(sorted_lb, start=1):
        lb_rank_by_id[id(row)] = idx

    prev_ranks = {m["name"]: m.get("rank", None) for m in ANALYTICS_DB["models"]}

    # Собираем новости о движении
    today = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%d.%m.%Y")
    movement_news: List[Dict[str, str]] = []

    for tracked in ANALYTICS_DB["models"]:
        row = find_lb_row_for_model(sorted_lb, tracked)
        if not row:
            # Для проприетарных моделей/отсутствующих на LB оставляем старые значения
            continue

        new_rank = lb_rank_by_id[id(row)]
        old_rank = prev_ranks.get(tracked["name"])
        tracked["rank"] = new_rank

        # Определяем изменение позиции
        if old_rank is None:
            tracked["change"] = "NEW"
            movement_news.append({
                "date": today,
                "title": f"{tracked['name']} появилась в Open LLM Leaderboard",
                "text": f"Модель впервые зафиксирована в таблице с позицией #{new_rank}."
            })
        else:
            diff = old_rank - new_rank
            if diff > 0:
                tracked["change"] = f"↑{diff}"
                movement_news.append({
                    "date": today,
                    "title": f"{tracked['name']} поднимается в рейтинге",
                    "text": f"Модель поднялась с #{old_rank} до #{new_rank} в Open LLM Leaderboard."
                })
            elif diff < 0:
                tracked["change"] = f"↓{abs(diff)}"
                movement_news.append({
                    "date": today,
                    "title": f"{tracked['name']} теряет позиции",
                    "text": f"Модель опустилась с #{old_rank} до #{new_rank} в Open LLM Leaderboard."
                })
            else:
                # Без изменений
                if tracked.get("change") not in ("NEW",):
                    tracked["change"] = "0"

        # При желании можно подтягивать короткий статус по типу/среднему скору
        avg = row.get("Average ⬆️")
        if isinstance(avg, (int, float)):
            tracked["status"] = f"{tracked['status']} (средний балл на Open LLM Leaderboard: {avg:.2f})"

    # Обновляем блок новостей: добавляем свежие новости на первое место
    if movement_news:
        # Ограничим суммарное количество до 10, чтобы не разрасталось бесконечно
        ANALYTICS_DB["news"] = movement_news + ANALYTICS_DB["news"]
        ANALYTICS_DB["news"] = ANALYTICS_DB["news"][:10]


# === ОБНОВЛЕНИЕ АНАЛИТИКИ РАЗ В СУТКИ (3:00 МСК) ===

def generate_daily_summary(models: List[Dict[str, Any]]) -> str:
    """
    Генерирует текст саммари на основе текущих рангов.
    """
    # Находим лидеров
    sorted_models = sorted(models, key=lambda m: m["rank"])
    leader = sorted_models[0]

    # Ищем тех, кто вырос (change содержит '↑' или 'NEW')
    risers = [m["name"] for m in models if "↑" in str(m.get("change", "")) or "NEW" in str(m.get("change", ""))]

    # Формируем текст
    today = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%d.%m.%Y")
    summary = f"По состоянию на {today}, **{leader['name']}** удерживает лидерство в глобальном рейтинге. "
    if risers:
        summary += f"Заметный рост показывают: **{', '.join(risers)}**. "
    else:
        summary += "В топе сохраняется стабильность, значительных изменений позиций за сутки не зафиксировано. "
    summary += "Конкуренция в open-source сегменте продолжает усиливаться."
    return summary


async def refresh_analytics_data():
    tz = ZoneInfo("Europe/Moscow")
    now_str = datetime.now(tz).strftime("%d.%m.%Y %H:%M МСК")

    print("[Analytics] Refreshing data...")
    lb_data = await fetch_openllm_leaderboard()

    if lb_data:
        try:
            # 1. Обновляем ранги и новости
            update_from_leaderboard(lb_data)
            print("[Analytics] Leaderboard updated successfully.")
        except Exception as e:
            print(f"[Analytics] Error processing leaderboard: {e}")
    else:
        print("[Analytics] Failed to fetch leaderboard data.")

    # 2. ВАЖНО: Перегенерируем саммари на основе новых данных!
    ANALYTICS_DB["summary"] = generate_daily_summary(ANALYTICS_DB["models"])

    # 3. Обновляем штамп времени
    ANALYTICS_DB["last_updated"] = now_str


def seconds_until_next_3_msk() -> float:
    tz_msk = ZoneInfo("Europe/Moscow")
    now = datetime.now(tz=tz_msk)
    target_today = datetime.combine(now.date(), time(3, 0), tzinfo=tz_msk)
    if now >= target_today:
        target_today = target_today + timedelta(days=1)
    return (target_today - now).total_seconds()


async def analytics_scheduler_loop():
    """
    Бесконечный планировщик: ждёт до следующего 3:00 МСК, обновляет данные, повторяет цикл. [web:22][web:23][web:26]
    """
    while True:
        delay = seconds_until_next_3_msk()
        await asyncio.sleep(delay)
        await refresh_analytics_data()


def init_analytics_scheduler(app: FastAPI):
    @app.on_event("startup")
    async def _start_scheduler():
        asyncio.create_task(analytics_scheduler_loop())


# === РОУТ /analytics (рендер HTML‑дашборда) ===

@router.get("/analytics", response_class=HTMLResponse)
async def analytics_page():
    now_str = datetime.now().strftime("%d.%m.%Y")
    summary = ANALYTICS_DB["summary"]
    last_updated = ANALYTICS_DB["last_updated"]

    # Таблица
    rows_html = ""
    for m in ANALYTICS_DB["models"]:
        change_class = (
            "change-up" if "↑" in str(m.get("change", "")) or "NEW" in str(m.get("change", ""))
            else "change-down" if "↓" in str(m.get("change", ""))
            else "change-neutral"
        )

        rows_html += f"""
        <tr>
            <td>{m['rank']}</td>
            <td><strong>{m['name']}</strong><br><small>{m['vendor']}</small></td>
            <td>{m['type']}</td>
            <td>{m['params']}</td>
            <td>{m['release']}</td>
            <td>{m['status']}</td>
            <td class="{change_class}">{m['change']}</td>
        </tr>
        """

    # Новости
    news_html = ""
    for n in ANALYTICS_DB["news"]:
        news_html += f"""
        <div class="news-item">
            <div class="news-date">{n['date']}</div>
            <div class="news-title">{n['title']}</div>
            <div class="news-text">{n['text']}</div>
        </div>
        """

    # HTML страницы
    page = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Analytics Dashboard</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
                background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
                color: #e0e0e0;
                padding: 20px;
                line-height: 1.6;
            }}
            .container {{ max-width: 1400px; margin: 0 auto; }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 10px;
                background: linear-gradient(90deg, #00d4ff, #00ff88);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            .summary {{
                background: rgba(255,255,255,0.05);
                border-left: 4px solid #00d4ff;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
                font-size: 1.05rem;
            }}
            .last-updated {{
                color: #888;
                font-size: 0.9rem;
                margin-bottom: 30px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: rgba(255,255,255,0.03);
                border-radius: 8px;
                overflow: hidden;
                margin-bottom: 40px;
            }}
            th, td {{
                padding: 15px;
                text-align: left;
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }}
            th {{
                background: rgba(0,212,255,0.1);
                color: #00d4ff;
                font-weight: 600;
                text-transform: uppercase;
                font-size: 0.85rem;
            }}
            tr:hover {{ background: rgba(255,255,255,0.05); }}
            .change-up {{ color: #00ff88; font-weight: bold; }}
            .change-down {{ color: #ff4444; font-weight: bold; }}
            .change-neutral {{ color: #888; }}
            .news-section {{ margin-top: 40px; }}
            .news-section h2 {{
                font-size: 1.8rem;
                margin-bottom: 20px;
                color: #00ff88;
            }}
            .news-item {{
                background: rgba(255,255,255,0.05);
                padding: 15px;
                margin-bottom: 15px;
                border-radius: 8px;
                border-left: 3px solid #00ff88;
            }}
            .news-date {{
                color: #888;
                font-size: 0.85rem;
                margin-bottom: 5px;
            }}
            .news-title {{
                font-weight: bold;
                font-size: 1.1rem;
                margin-bottom: 8px;
                color: #00d4ff;
            }}
            .news-text {{ color: #ccc; }}
            @media (max-width: 768px) {{
                h1 {{ font-size: 1.8rem; }}
                table {{ font-size: 0.85rem; }}
                th, td {{ padding: 10px 8px; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 AI Models Analytics Dashboard</h1>
            <div class="last-updated">Последнее обновление: {last_updated}</div>
            
            <div class="summary">{summary}</div>

            <h2 style="color: #00d4ff; margin-top: 30px; margin-bottom: 15px;">Топ‑10 моделей на сегодня</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Модель</th>
                        <th>Тип</th>
                        <th>Параметры</th>
                        <th>Релиз / Апдейт</th>
                        <th>Текущий статус</th>
                        <th>Изм.</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>

            <div class="news-section">
                <h2>📰 Последние новости</h2>
                {news_html}
            </div>
        </div>
    </body>
    </html>
    """

    return page
