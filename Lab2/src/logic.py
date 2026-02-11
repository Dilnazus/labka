# src/logic.py

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'rules.json')

def load_rules():
    with open(RULES_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_rules(data):
    rules = load_rules()
    
    # Hard filter: проверка контактов
    if rules['critical_rules']['must_have_contacts'] and not data['has_contacts']:
        return "⛔️ Критическая ошибка: Нет контактов кандидата"
    
    # Проверка опыта
    if data['experience_months'] < rules['thresholds']['min_experience']:
        return "❌ Отказ: Опыт меньше минимально требуемого"
    if data['experience_months'] > rules['thresholds']['max_experience']:
        return "❌ Отказ: Опыт превышает допустимый максимум"
    
    # Проверка навыков
    for skill in data['skills']:
        if skill in rules['lists']['forbidden_skills']:
            return f"⚠️ Предупреждение: Найден запрещенный навык ({skill})"
    for req_skill in rules['lists']['required_skills']:
        if req_skill not in data['skills']:
            return f"❌ Отказ: Отсутствует необходимый навык ({req_skill})"
    
    return f"✅ Успех: Кандидат соответствует сценарию '{rules['scenario_name']}'"
