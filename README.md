# ML Simulator

A machineLearning playground/simulator where one can analyze different datasets graphically and statistically and apply various classification and regression models. It will be capable of determining the best suitable algorithm for any case and applying it. One may also select the preferred algorithm for predictions and compare the efficiencies of different algorithms. Theidea is simple, you have a dataset but don't have knowledge about models, also doesn't care how to do the stuff but is only concerned about the results. Don't worry we have got the solution, upload your models and we will run through our black box formula and give you the best of the results which would take hours of human efforts.
Basically, our platforms notify the users when their hude data sets are trained and ready for users. In case of failure it notifies the users regarfing the same. The messaging services publishes mesages on channels. Any user who are subscribed to these services are therefore notifies regarding same.
Messaging services that we use is by [Ably](https://www.ably.io/)

Tech Stack: ReactJs(Frontend), Flask (Backend), Python Libraries (SKlearn, Pandas, Numpy, NLTK,Spacy), GIT, Messaging Service API (ABLY)

Built During Hack-A-BIT 2.0 

## How To Use Our Platform

1. Clone the repo `https://github.com/hackabit19/skilled_Noobs.git`.
2. Change the directory 
``` bash
    $ cd skilled_Noobs
```
3. Run the command 
```bash 
    $ pip install -r requirements.txt
```
3. Start the server
```
    $ flask run
```

NOTE: To run the ably's services follow the following steps:

1. Go to [Ably.co](https://www.ably.io/).
2. Sign Up and Create a new App icon on top-right.
3. Fll in all the details and propagate to API keys.
3. Use your API key to replace in code snippet
```javascript
    var apiKey = "Your-API-Key";
    var realtime = new Ably.Realtime(apiKey);
```
4. Boom you are ready to use our service with messaging service.A machineLearning playground/simulator where one can analyze different datasets graphically and statistically and apply various classification and regression models. It will be capable of determining the best suitable algorithm for any case and applying it. One may also select the preferred algorithm for predictions and compare the efficiencies of different algorithms. Theidea is simple, you have a dataset but don't have knowledge about models, also doesn't care how to do the stuff but is only concerned about the results. Don't worry we have got the solution, upload your models and we will run through our black box formula and give you the best of the results which would take hours of human efforts.

Tech Stack: ReactJs(Frontend), Flask (Backend), Python Libraries (SKlearn, Pandas, Numpy, NLTK,Spacy), GI

## Code Explaination

 ```javascript
    var channel = realtime.channels.get("hack");
    channel.publish("update", { team: "Data uploaded and run Succesfully." });
 ```
**It publisshes mesaages to "hack" channel about data is uploaded, ran and results are ready to be analysed by user.**

```javascript
    var channe2 = realtime.channels.get("fail");
    channel.publish("update", { team: "Data uploaded failed" });
  ```
**It publishes messages to "fail" channel about data failure of data uploadation.**

```javascript
    var channe3 = realtime.channels.get("hack");
    channe3.subscribe(function(msg) {
      alert("Following messaged Received: " + JSON.stringify(msg.data));
    });
```
**The users are subscribed to channel hack to receive messages.**


## Walkthrough

1. Click on the choose file on the top to upload the dataset
2. Click Upload to visualise the dataset.
3. Also, switch tables to get a in-depth picture of the dataset.
4. Get notify, when the dataset is ready to be visualize.

NOTE: We have, our train.csv file for the demo purpose.

## Contributors

Built with :purple_heart: by team ***skilled_Noobs***
1. [Harshit Singh](https://github.com/helios1101)
2. [Aayushi Dwivedi](https://github.com/qwerty1706)
3. [Rithik Sharma](https://github.com/RSH04)
