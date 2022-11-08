# TwitterOSINT
Utilizing python and the Twitter API to parse data for OSINT.

This script was written in python while taking advantage of the Twitter API to pull data and output it to a CSV file for reconnaissance purposes when completing a penetration test. You will need to sign up for a Twitter Developer account so you can utilize the API key, access and bearer tokens to authenticate with the API. You can sign up for a Twitter Developers account <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">here</a>.

<h3>Modules Used:</h3>
1. tweepy  2. config  3. csv  4. pandas

<h3>Process:</h3>
• First you create a configuration file where you can store your API key, API key secret, access key, access key, access key secret and bearer token.
<br>
<br>
<a href="https://imgur.com/5YJBnrB"><img src="https://i.imgur.com/5YJBnrB.jpg" title="source: imgur.com" /></a><br>
<br>
• Next we will create a new file, import the modules we will be using in this script and define a function for client authentication.<br>
<br>
<a href="https://imgur.com/OItIxs3"><img src="https://i.imgur.com/OItIxs3.jpg" title="source: imgur.com" /></a><br>
<br>
• Our next step is to define a function to parse the user data. We do this by first getting the user ID and then use that ID to pull the user's tweets.
<br>
<br>
<a href="https://imgur.com/EraUK87"><img src="https://i.imgur.com/EraUK87.jpg" title="source: imgur.com" /></a>
<br>
<br>
• We then create a data frame to clean up the data and output it to a CSV file.
<br>
<br>
<a href="https://imgur.com/pBcBGx8"><img src="https://i.imgur.com/pBcBGx8.jpg" title="source: imgur.com" /></a>
<br>
<br>
• For fun I created a with open statement that searches the CSV file for a list of strings. 
<br>
<br>
<a href="https://imgur.com/b5DKHE1"><img src="https://i.imgur.com/b5DKHE1.jpg" title="source: imgur.com" /></a>
<br>
<br>
<h3>Lessons Learned:</h3>
1. When using the Tweepy module, you have to make sure you are using the right parameters per client Method. You can find the <a href="https://docs.tweepy.org/en/stable/client.html> Tweepy documentation here.</a>
<br>
2. When using the standard Twitter developer account you are limited to the amount of data you can parse montly. You can apply for an elevated or academic account which raises that ceiling. 

  
  
  
  
  
  
  
  
  
  
  


