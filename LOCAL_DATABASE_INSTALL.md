# Instructions to install and run the databases locally correctly:

- create "sarah_chatbot" blank database in postgresql (code tested on pgAdmin4)
- Open Terminal, install guinicorn locally by typing pip install gunicorn on terminal
- Open IDE, open chatbot.py.
- comment the big training list (lines 48-53)
- decomment the "greetings.yml" training line (line 45)
- run chatbot.py to create the database
- go to your database, alter table properties:
-- statement:length/precision of text,search_text,in_response_to,search_in_response_to to 1,000
-- statement:length/precision of conversation,persona to 100 
-- tag: length/precision of name to 100 
- decomment the big training list (lines 48-53)
- comment the greetings training line (line 45)
- run chatbot.py to finish the training
- comment both training lists 
- run/test program typing python app.py
See APP_DEPLOY_HEROKU if you want to deploy this app online



