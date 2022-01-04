# About 
An API that provides replies to the message passed to the API. 

# API Schema
Route: ```/api/chatbot/query/``` \
Method: ```POST``` \
Headers: ```Content-Type: application/json```  
Input: ```message``` Input is taken in form of JSON object. \
Output: ```solutions``` Output provided as JSON object.
Status Code: ```200```

# How to use?
- Go to the API link:  https://cureya-chatbot.herokuapp.com/api/chatbot/query/ or localhost:3000/api/chatbot/query
- Send a POST request with body layout as: 
```
{
    "message": "Some message here"
}
```
as a JSON object.

- The API will evaluate the correct response and send the reply as: 
```
{
    "solutions": ["All", "Solutions", "Are", "Sent"]
}
```
as a JSON object.

# Editing the API code
1) Clone the Repo.
2) Install ```requirements.txt```.
3) Go to the ```chatbot_api``` folderand locate ```views.py```. 
4) Import required script at the top of the file that will generate the replies.
5) The class ```BotSolutions``` contains the API code. 
6) ```data``` variable contains the message sent in ```string```format. The ```data``` variable can be sent to the script directly and stored in ```solutions``` variable.
7) Pass the ```solutions``` variable to the JSONResponse.



