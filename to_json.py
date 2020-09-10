import json
from langdetect import detect


class ToJson:

    def get_json(self, data):
        # -1 is full_description, -2 is short_description, -3 is headline
        if (data[-1] or data[-2]) and data[-3] and detect(data[-3]) == 'en':
            return json.dumps({
                'link': data[0],
                'categories': data[1],
                'date_published': data[2],
                'date_modified': data[3],
                'headline': data[4],
                'short_description': data[5],
                'full_description': data[6]
            }, ensure_ascii=False, indent=4)
