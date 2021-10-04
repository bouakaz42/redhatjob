from bs4 import BeautifulSoup
import requests
# Create your views here.
#الرابط المراد 
session = requests.session()
# link = 'https://giga.egybest.org/movies/2020'
# egy_best_link = 'https://giga.egybest.org'

# page = session.get(link )
# soup = BeautifulSoup(page.content, 'lxml')
# for movies in soup.select("div" , attrs={'class':'movies'}):
#     for movie in movies.find_all("a" , {'class':'movie'}):
    # extract movie url
        # print(movie['href'])
     # to extract titles from movie
    #     for title in movie.find_all("span" , {'class':'title'}):
    #     #   print(title.text)
    # #   to extract pic url 
    #     for pic_url in movie.find_all("img"):
    #     #   print(pic_url['src'])

def get_watch(searched_movie):
    strmov = str(searched_movie.replace(' ','+'))
    search_url = 'https://arabseed.onl:2053/find/?find={}'.format(strmov)
    searched_page = session.get(search_url)
    searched_page_soup = BeautifulSoup(searched_page.content, 'html.parser')
    result = searched_page_soup.find("div" , {'class':'MovieBlock'})
    result_movie = result.find('a')['href']
    movie_page = session.get(result_movie)
    movie_page_soup = BeautifulSoup(movie_page.content, 'html.parser')
    movie_page_wtch = movie_page_soup.find('a' , {'class':'watchBTn'})['href']
    movie_page_down = movie_page_soup.find('a' , {'class':'downloadBTn'})['href']
    movie_wtch = session.get(movie_page_wtch)
    movie_wtch_soup = BeautifulSoup(movie_wtch.content, 'html.parser')
    get_watch_url = movie_wtch_soup.find('li' , {'class':'HoverAfter active'}).find('noscript').find('iframe')['src']
    watch_session= session.get(get_watch_url)
    watch_soup = BeautifulSoup(watch_session.content, 'html.parser')
    find_src = watch_soup.find('source')['src']
    
    return find_src



def get_watch_fasel(searched_movie):
    strmov = str(searched_movie.replace(' ','+'))
    search_url = 'https://www.faselhd.pro/?s={}'.format(strmov)
    searched_page = session.get(search_url)
    searched_page_soup = BeautifulSoup(searched_page.content, 'html.parser')
    result = searched_page_soup.find("div" , {'class':'postDiv'})
    result_movie = result.find('a')['href']
    movie_page = session.get(result_movie)
    movie_page_soup = BeautifulSoup(movie_page.content, 'html.parser')
    movie_page_wtch = movie_page_soup.find('a' , {'class':'watchBTn'})['href']
    movie_page_down = movie_page_soup.find('a' , {'class':'downloadBTn'})['href']
    movie_wtch = session.get(movie_page_wtch)
    movie_wtch_soup = BeautifulSoup(movie_wtch.content, 'html.parser')
    get_watch_url = movie_wtch_soup.find('li' , {'class':'HoverAfter active'}).find('noscript').find('iframe')['src']
    watch_session= session.get(get_watch_url)
    watch_soup = BeautifulSoup(watch_session.content, 'html.parser')
    find_src = watch_soup.find('source')['src']
    
    return find_src


# get_nonscript = get_watch_url.find_all('noscript')
# watch_bar = movie_page_soup.find('iframe')['src']
# source = watch_bar.find('source')['src']




# # find main movies div
# all_mv= soup.find_all("div" , class_='movies')
# #extract every childern span [hold movie] from parent div   , mov_pic_url , mov_url
# for mov in all_mv :
#   b = mov.find_all("a",class_="movie")
#   #extract url and img src and
#   for singmov in b :
#       print(singmov['href'])
#       title = singmov.find_all("span" , class_="title")
#       image = singmov.find_all("img")
#       for tit in title : 
#           print(tit.text)
#       for img in image:
#           print(img['src'])
      


# https://hola.egybest.ltd/api?call=FUUUchZMUcUFUcEFEXrKdcUrfEUUrKFFCcFcUchZsUcUFUcEEEFErfEUEWcFcUcdPnUcUFUchEZIqXhrdPwszUcFcUcDiNfhZdDXcUFEKfEEEKFEUEdfEEFhFcUcUmEUcUFUchEZskWUwjhhchLxDrUskrsUcFcUcsZWcUFUciZWZsZXewFrUcFcUclWUcUFUcPWEEWDKFsWUcUf&auth=e7c5ea19a4b7ac76d236975317c8174f&v=1

# https://hola.egybest.ltd/vs-mirror/vidstream.online/v/90pGSKKmm9/?vclid=2eecd360758464f054c8e15ac659dafb80eddeca064959f5af0a87e8HyyybMAKybyuybOWSRCQOzMAYmNybubybXmOUbyuybrHjnnjGzDNcwivOSYyWUbubybNMhybyuybOWSmjByYdOObOfDwzymjzmybyt


'''

    {'__cf_bm': 'QFVNmLLP2FN2iWW7E9MT2EnvVbUDFRBSRzWh1EdgIrE-1631462684-0-AR6/Yn7kES2tCH5+xxsw36si9tliMYvs/BvVIEe9r5PriMv1RIB4sATzuRwuBj3OzAOx257YkPQ2VqI6EmCRLU4=', 'eda33681': 'qeeeARZzweAeOeAqMiuizsxiHCoKzOKvVxOnAOAeAFVhCiNAeOxUbxxxUOxbxLbOKxxOAeAsZReAeOeACTrivOwxVADjKKivxiNAeb-f868a5cbff33a6c9107cb702dcb41305', '1c2e36f8': 'CNNNagAseNaNhNaPssCaCBCyChnjnwahaNamAgNaNhNaWsWrCjiSoUhkhjscVVgCNahaNatiLRjraNhCyXCCCyhCXCVXhUCNNX-59b284565326ba824c684477ec3a32ec', 'PSSID': 'zxhmHQhUtUodPyBA3NGc7fQxjeQXuOma8Ww%2CRY4CxyvnKT5tJydENb9Fli5oYuKAfe0X6SazPbWS9TcITpXRnwNny47trDhLtK2bcrTGBTrpeb73M0OdrKdV946NV83e'}

'''