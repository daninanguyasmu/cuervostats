import json
import pandas as pd
import streamlit as st

with open('categories.json', 'r', encoding='utf-8') as ps:
    data = json.load(ps)


def match_data_recovery(match_name, category, division, datetime):
    return [match_name, category, division, datetime]

def players_recovery(category_name, division):
    for cat in data:
        if cat.get('category') == category_name and cat.get('division') == division:
                return cat.get('players')
    return {}

def stats_to_excel(stats, match_info):
    df = pd.DataFrame(stats)
    m_date = str(match_info['datetime']).replace(":", "-")
    df.to_excel(f'{match_info['name']}--{match_info['category']} {match_info['division']}--{m_date}.xlsx', index=False)
    return f'{match_info['name']}--{match_info['category']} {match_info['division']}--{m_date}.xlsx'
