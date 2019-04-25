import glob
import re

from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

from paperbook import PaperBook

class AozoraParser:
    def __init__(self):
        pass
    

    def __get_text(self, soup: BeautifulSoup) -> str:
        try:
            text = soup.find(class_='main_text').text
        except AttributeError:
            text = soup.find('body').text
        return text


    def __cleaning(self, text: str) -> str:
        '''
        remove ruby & full space
        '''
        text = re.sub(r'(（.*）)|　', '', text)
        return text


    def parse(self, file_obj: str, encode_type: str=None) -> PaperBook:
        '''
        file_obj: file object
        '''
        soup = BeautifulSoup(file_obj, fromEncoding=encode_type)
        text = self.__get_text(soup)
        text = self.__cleaning(text)
        return PaperBook(body=text)

