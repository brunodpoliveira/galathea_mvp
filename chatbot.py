from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
import spacy

spacy.load('pt_core_news_sm')
# --------------------------------------
# Instantiate agent
"""
BestMatch = selects response by best known match to statement
response_selection_method has 3 options:
get_first_response,get_most_frequent_response or get_random_response
statement_comparison_function has 4 options:
read options and explanations here: https://chatterbot.readthedocs.io/en/stable/comparisons.html#statement-comparison
default_response is a response in case the bot doesn't know what to say
maximum_similarity_threshold:
maximum amount of similarity between 2 statement required before the search process is halted(default:0.95)
"""
bot = ChatBot('Sarah',
              read_only=False,
              response_selection_method=get_first_response,
              logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
                               "response_selection_method": 'chatterbot.response_selection.get_first_response',
                               "statement_comparison_function": 'chatterbot.comparisons.SynsetDistance',
                               'default_response': 'Ainda não sei responder essa frase.',
                               'maximum_similarity_threshold': 0.95
                               }],
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='postgresql://postgres:postgres@localhost/sarah_chatbot',)

              # local - dev config
# database_uri='postgresql://postgres:postgres@localhost/sarah_chatbot',)

# --------------------------------------

# Corpus Trainer
corpus_trainer = ChatterBotCorpusTrainer(bot)

# use this line and comment out the complete pack if
# you feel like doing some quick testing

corpus_trainer.train('data/greetings.yml')
"""
corpus_trainer.train('data/botprofile.yml', 'data/compliment.yml', 'data/context_free_br.yml', 'data/conversations.yml',
                     'data/emotion.yml', 'data/food.yml', 'data/games.yml', 'data/health.yml',
                     'data/literature.yml', 'data/money.yml', 'data/movies.yml', 'data/psychology.yml',
                     'data/sports.yml', 'data/suggestions.yml')
"""


# --------------------------------------
# Conversation Loop - terminal only


def conversation():
    while True:
        try:
            question = input('Usuário: ')
            answer = bot.get_response(question)
            if answer.confidence > 0.5:
                print('Sarah: ', answer)
                print('confidence', answer.confidence)
            else:
                print('Sarah: ', 'Ainda não sei responder essa frase')
                print('confidence', answer.confidence)
        # CONTROL+D to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


"""          
if __name__ == "__main__":
    conversation()
"""

# --------------------------------------
# type python chatbot.py to train the chatbot database
