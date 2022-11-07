# TwitterOSINT
Utilizing python and the Twitter API to parse data for OSINT.

This script was written in python while taking advantage of the Twitter API to pull data and output it to a CSV file for reconnaissance purposes when completing a penetration test. You will need to sign up for a Twitter Developer account so you can utilize the API key, access and bearer tokens to authenticate with the API. You can sign up for a Twitter Developers account <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">here</a>.

<h3>Modules Used</h3>
1. tweepy
2. config
3. csv
4. pandas 

<h3>Process</h3>
• First you create a configuration file where you can store your API key, API key secret, access key, access key, access key secret and bearer token.
<br>
<a href="https://imgur.com/5YJBnrB"><img src="https://i.imgur.com/5YJBnrB.jpg" title="source: imgur.com" /></a><br>
<br>
• Next we will create a new file, import the modules we will be using in this script and define a function for client authentication.<br>
<br>
<a href="https://imgur.com/OItIxs3"><img src="https://i.imgur.com/OItIxs3.jpg" title="source: imgur.com" /></a><br>



