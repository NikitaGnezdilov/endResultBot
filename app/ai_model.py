import logging
from fuzzywuzzy import process
from . import words

def recognize(data):
    logging.info(f"Recognize input: {data}")

    # Используем fuzzy поиск для поиска ближайшего совпадения
    possible_keys = list(words.data_set.keys())
    best_match, match_confidence = process.extractOne(data, possible_keys)

    if match_confidence < 70:  # Если совпадение менее 70%, возвращаем ошибку
        return "Извините, я не понял ваш запрос."

    logging.info(f"Best match: {best_match} (confidence: {match_confidence})")

    # Получаем ответ из словаря
    answer = words.data_set.get(best_match, "Извините, я не смог обработать ваш запрос.")

    logging.info(f"Recognize response: {answer}")

    return answer