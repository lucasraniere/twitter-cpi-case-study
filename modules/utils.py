import os, re

def hello_world():
    print('Hello World')


def load_week_list(data_path):
    DATA_PATH = data_path
    week_list = [week_dir for week_dir in os.listdir(DATA_PATH) if os.path.isdir(DATA_PATH+week_dir) and not week_dir.endswith('.ipynb_checkpoints')]
    week_list.sort()
    week_list.remove('week_pr_01')
    week_list.insert(week_list.index('week_12')+1, 'week_pr_01')
    week_list.remove('week_pr_02')
    week_list.insert(week_list.index('week_pr_01')+1, 'week_pr_02')
    week_list.remove('week_pr_03')
    week_list.insert(week_list.index('week_17')+1, 'week_pr_03')
    week_list.remove('week_pr_04')
    week_list.insert(week_list.index('week_21')+1, 'week_pr_04')
    return week_list
