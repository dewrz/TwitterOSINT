# TwitterOSINT
Utilizing python and the Twitter API to parse data for OSINT.

This script was written in python while taking advantage of the Twitter API to pull data and output it to a CSV file for reconnaissance purposes when completing a penetration test. You will need to sign up for a Twitter Developer account so you can utilize the API key, access and bearer tokens to authenticate with the API. You can sign up for a Twitter Developers account <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">here</a>.

<h3>Modules Used:</h3>
1. tweepy  2. config  3. csv  4. pandas
<br>
<br>
<h3>Lessons Learned:</h3>
1. When using the Tweepy module, you have to make sure you are using the right parameters per client Method. You can find the <a href="https://docs.tweepy.org/en/stable/client.html> Tweepy documentation here.</a>
<br>
2. When using the standard Twitter developer account you are limited to the amount of data you can parse montly. You can apply for an elevated or academic account which raises that ceiling. 
