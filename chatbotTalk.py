from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def conversacionRestaurantes(): 
    chatbot = ChatBot(
        "Jorcircuito",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
        ],
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.50,
            },
            'chatterbot.logic.MathematicalEvaluation'
        ],
        read_only = True
    )
    trainer = ListTrainer(chatbot) # bot training
    trainer.train('chatterbot.corpus.spanish')


    folder = 'training_data'
    for filename in os.listdir(folder):
        print('\n Chatbot training with '+os.path.join(folder, filename)+' file')
        training_data = open(os.path.join(folder, filename)).read().splitlines()
        trainer.train(training_data)


    print('Bienvenido al Chatbot!')
    while True:
        request = input('Tu:')
        if request == "Salir" or request == "salir":
            print("Bot: Salir")
            break
        response = chatbot.get_response(request)
        print(f'Bot: {response}')