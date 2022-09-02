'''
This module contains the week class.

This class is used to structure the data in
extraction process.
'''

import datetime

class Week:
    def __init__(self, week_number, week_start, deponents):
        self.number = week_number
        self.start = week_start
        self.end = self.week_end(week_start)
        self.deponents = deponents
        self.tweets_amount = None
        self.top_10_hashtags = None
        self.info = None
        self.days = None
        self.initiate_week()

    def initiate_week(self):
        self.set_week_days()
        self.generate_info()

    def week_end(self, week_start):
        week_end = self.date_sum(self.string_to_date(week_start), 6)
        return self.date_to_string(week_end)

    def date_to_string(self, date):
        return date.strftime('%Y-%m-%d')

    def string_to_date(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%d')

    def date_sum(self, date, number):
        return date + datetime.timedelta(days=number)

    def set_week_days(self):
        self.days = []
        date = datetime.datetime.strptime(self.start, '%Y-%m-%d')
        for x in range(7):
            self.days.append(self.date_to_string(self.date_sum(date, x)))

    def generate_info(self):
        self.info = {
            'week_number': self.number,
            'start': self.start,
            'end': self.end,
            'tweets_amount': self.tweets_amount,
            'hashtags_amount': None,
            'deponents': self.deponents,
            'top_10_hashtags': self.top_10_hashtags,
            'days_info': {
                'day_1': {
                    'date': self.days[0],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_2': {
                    'date': self.days[1],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_3': {
                    'date': self.days[2],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_4': {
                    'date': self.days[3],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_5': {
                    'date': self.days[4],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_6': {
                    'date': self.days[5],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                },
                'day_7': {
                    'date': self.days[6],
                    'tweets_amount': None,
                    'hashtags_amount': None,
                    'deponents': [],
                    'top_10_hashtags': None
                }
            }
        }
        for days in self.deponents.items():
            self.info['days_info'][days[0]]['deponents'] = days[1]
