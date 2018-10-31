"""
CP1404 Practical 10 - Ryan Honorica
Wikipedia interface code.
"""

import wikipedia


def main():
    print("Wikipedia Search")
    article_title_input = input('Title: ')
    article = wikipedia.page(article_title_input)
    while article_title_input.strip() != '':
        try:
            print('Title of Article: {}'.format(article.title.strip()))
            print('Article Summary: {}'.format(article.summary.strip()))
            print(article.url.strip())
        except wikipedia.exceptions.DisambiguationError as disambiguation_error:
            print(article_title_input + ' refers to a disambiguation page. Which page do you wish to choose instead?')
            for error_index, title in enumerate(disambiguation_error.options):
                print(str(error_index + 1) + '.', title)
            article_title_input = disambiguation_error.options[get_int('Which page: ', 1, len(disambiguation_error.options)) - 1]
            article = wikipedia.page(article_title_input)
            print('Title of Article: {}'.format(article.title.strip()))
            print('Article Summary: {}'.format(article.summary.strip()))
            print(article.url.strip())
        article_title_input = input('Title: ')
        article = wikipedia.page(article_title_input)


def get_int(prompt, min_num=1, max_num=float('inf')):
    valid_input = False
    menu_option = input(prompt)
    while not valid_input:
        if menu_option == int(menu_option):
            if menu_option < min_num or menu_option > max_num:
                print('Input must be > {}  and < {}'.format(min_num, max_num))
            else:
                valid_input = True
        elif menu_option.isdigit() is False:
            print('Input must be an integer')
        if not valid_input:
            print(prompt)
    return menu_option




main()