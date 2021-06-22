# Burp Suite - 101

## Getting Started

Learn how to use key features of the most popular bug hunting tool. Burp proxy is a MITM proxy, it is allowed to intercept Web Requests.

You can download the community edition of burp here:

> https://portswigger.net/

The commmunity edition does lack some advanced and nice to have features. Use the installer as it will simplify a lot of things insteaed of the .jar file.

Only temporary projects are supported in the commmunity edition. For now we will use default, but for the future you can use saved configuration and keep your configured profile setups. Lets start by setting up Firefox to connect onto burp.

Go to Proxy > Options and you should see under _Proxy Listeners_ your loopback address with socket 8080. If you notice the __Running__ checkbox unchecked, then there could likely be another web instance or service running on that port and you can simply select a new one.

In Firefox you can go to _Preferences_ > _General_ and then at the bottom where there is _Network Settings_ you can select _Settings_ and then configure your __Configure Proxy Access to the Internet__ with a manual proxy configuration set to localhost:8080 and select all protocols if applicable.

![Burp Config](../../img/burp101(0).png)

Once you refresh your page you will notice that it should work, but Firefox will not allow you to proceed because the website will have an invalid SSL certificate, so we cannot override that. And that this is the reason why firefox is the defacto testing browser, it has its own proxy settings. Other browsers will require you to configure system wide making Firefox the clear winner.

To get around this we will need the certificate authority for our own Burp proxy. With our preferences current setting, proceed to navigate to the following URL to download the needed cert:

> http://burp

![Burp Cert](../../img/burp-cert.png)

Once the download is complete you can navigate back to __Privacy & Security__ under your preferences and under the __Certificates__ section click _View Certificates..._. Here you can import the cert you had just downloaded.


