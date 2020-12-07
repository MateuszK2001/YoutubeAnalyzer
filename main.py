import time

import config
import files_manager
import yt_api
import yt_scraper

config.load()
files_manager.load()

print()
print()
print(f"{'#' * 15} Filmy {'#' * 15}")
print()
print()

"""
Pobieranie informacji o filmach za pomoca scrapowania
"""
for link in files_manager.MOVIES_LINKS_LIST:
    movie = yt_scraper.get_movie_data(link)
    print('-' * 30)
    print(movie)
    print()
    # jezeli cos sie zjebie to odkomentowac
    # time.sleep(3)


print()
print()
print(f"{'#' * 15} Kanały {'#' * 15}")
print()
print()
"""
Pobieranie informacji o kanałach za pomocą scrapowania
"""
for link in files_manager.CHANNELS_LINKS_LIST:
    channel = yt_scraper.get_channel_data(link)
    print('-' * 30)
    print(channel)
    print()
    # jezeli cos sie zjebie to odkomentowac
    # time.sleep(3)

"""
Pobieranie informacji o filmach za pomocą api
"""
# ids = [yt_api.link_to_video_id(link) for link in files_manager.MOVIES_LINKS_LIST]
# for movie in yt_api.get_movies_data(ids):
#     print('-'*30)
#     print(movie)
#     print()


"""
Z youtube api odnośnie kanałów jest taki problem, że trzeba znać id kanału.
Sama nazwa/link nie wystarczy, dlatego lepiej w przypadku kanałów używać scrapowania.
Można by też użyć search z api, ale zużywa to dużo punktów 100, gdzie inne zapytania biorą tylko 1 pkt.
Do tego search jest nieprecyzyjne.
W pliku są podane linku więc w przykładzie stworzyłem tablicę na sztywno
"""
# ids = ['UCdfRZ1u4b1pT68er47tb5vA', 'UCkC9YgH_FlqOhOIoTDFt4CA', 'UCJlMkkOVNbLY9QJPo24-plQ', 'UC7RswyY8VfbSdikz_8wdp3w', 'UCweCc7bSMX5J4jEH7HFImng', 'UC0e3QhIYukixgh5VVpKHH9Q']
# for channel in yt_api.get_channel_data(ids):
#     print('-'*30)
#     print(channel)
#     print()
#     print()
