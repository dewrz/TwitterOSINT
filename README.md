# TwitterOSINT
Utilizing python and the Twitter API to parse data for OSINT.

This script was written in python while taking advantage of the Twitter API to pull data and output it to a CSV file for reconnaissance purposes when completing a penetration test. You will need to sign up for a Twitter Developer account so you can utilize the API key, access and bearer tokens to authenticate with the API. You can sign up for a Twitter Developers account <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">here</a>.

<h3>Modules Used:</h3>
1. tweepy<br>
2. config<br>
3. csv<br>
4. pandas<br>

<h3>The Process:</h3>
• First you create a configuration file where you can store your keys and token.
<a href="https://imgur.com/aHmJgUy"><img src="https://i.imgur.com/aHmJgUy.jpg" title="source: imgur.com" /></a><br>
• Next we will create a new file, import the modules we will be using in this script and define a function for client authentication.<br>
<a href="https://imgur.com/kmw0Gkr"><img src="https://i.imgur.com/kmw0Gkr.jpg" title="source: imgur.com" /></a>
• Our next step is to define a function to parse the user data. We do this by first getting the user ID and then use that ID to pull the user's tweets.
<a href="https://imgur.com/T8RsA5T"><img src="https://i.imgur.com/T8RsA5T.jpg" title="source: imgur.com" /></a>
• We then create a data frame to clean up the data and output it to a CSV file.
<a href="https://imgur.com/4Ha956W"><img src="https://i.imgur.com/4Ha956W.jpg" title="source: imgur.com" /></a>
• For fun I created a with open statement that searches the CSV file for a list of strings. 
<a href="https://imgur.com/arJpgwl"><img src="https://i.imgur.com/arJpgwl.jpg" title="source: imgur.com" /></a>


<h3>Lessons Learned:</h3>
• When using the Tweepy module, you have to make sure you are using the right parameters per client Method. You can find the <a href="https://docs.tweepy.org/en/stable/client.html"> Tweepy documentation here.</a>
<br>
<br>
• When using the standard Twitter developer account you are limited to the amount of data you can parse montly. You can apply for an elevated or academic account which raises that ceiling. 


