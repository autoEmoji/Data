# import os
# import pandas as pd
#
# class EmojiDict(object):
#
#     def __init__(self):
#         # this function creates the emoji dictionary
#
#
#
#         #loads the emoji table in the data folder in the package
#         file_path = os.path.dirname(os.path.abspath(__file__))
#         emoji_key = pd.read_csv(file_path + '/data/' + 'emoji_table.txt', encoding='utf-8', index_col=0)
#
#         #loads the diversity table
#         diversity_df = pd.read_csv(file_path + '/data/' + 'diversity_table.txt', encoding='utf-8', index_col=0)
#
#         #intialize emoji count
#         emoji_key['count'] = 0
#         emoji_dict = emoji_key['count'].to_dict()
#         emoji_dict_total = emoji_key['count'].to_dict()
#
#         #initialize diversity analysis
#         diversity_df['count'] = 0
#         diversity_keys = diversity_df['count'].to_dict().keys()
#         human_emoji = []
#
#         for emoji in diversity_keys:
#
#             emoji = emoji.replace(u'\U0001f3fb', '')
#             emoji = emoji.replace(u'\U0001f3fc', '')
#             emoji = emoji.replace(u'\U0001f3fd', '')
#             emoji = emoji.replace(u'\U0001f3fe', '')
#             emoji = emoji.replace(u'\U0001f3ff', '')
#
#             human_emoji.append(emoji)
#
#         human_emoji_unique = list(set(human_emoji))
#         human_emoji_dict = {}
#
#         for emoji in human_emoji_unique:
#
#             human_emoji_dict[emoji] = 0
#
#         #self define
#         self.dict = emoji_dict
#         self.dict_total = emoji_dict_total
#         self.emoji_list = emoji_dict.keys()
#         self.baskets = []
#         self.total_emoji = 0
#         self.total_indiv_emoji = 0
#
#         self.skin_tones = ['\U0001f3fb', '\U0001f3fc', '\U0001f3fd', '\U0001f3fe', '\U0001f3ff']
#         self.skin_tones_dict = {'human_emoji': 0, '\U0001f3fb':0, '\U0001f3fc':0, '\U0001f3fd': 0, '\U0001f3fe':0, '\U0001f3ff':0}
#         self.human_emoji = human_emoji_unique
#         self.human_emoji_dict = human_emoji_dict
#
#
#
#     def add_emoji_count(self, text):
#
#         # this function clears emojis from the string and return 1 to indicate
#         # that there were emojis in the string
#         # if there were no emojis the function returns 0
#
#         for emoji in self.human_emoji:
#             if emoji in text:
#                 for tone in self.skin_tones:
#                     em_tn = emoji+tone
#                     if em_tn in text:
#                         self.total_indiv_emoji = 1
#                         pos = text.find(em_tn)
#                         while (pos >0):
#                             text = text[:pos] + " " + text[pos+len(em_tn):]
#                             pos = text.find(em_tn)
#
#         for emoji in self.emoji_list:
#             if emoji in text:
#                 pos = text.find(emoji)
#                 while (pos >0):
#                     text = text[:pos] + " " + text[pos+len(emoji):]
#                     pos = text.find(emoji)
#                 self.total_indiv_emoji = 1
#
#         ret_val = self.total_indiv_emoji
#         self.total_indiv_emoji = 0
#         return ret_val, text
