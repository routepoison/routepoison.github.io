# The Web in Depth

* HTTP basics
* Cookie security
* HTML parsing
* MIME sniffing
* Encoding sniffing
* Same-Origin Policy
* CSRF (Cross-Site Request Forgery)

## Requests

![Example Web Request](../../img/web-request.png)

If you haven't seen a web request before, then that's OK. You will become very familiar with their structure and contents soon. The basic format is as follows:

VERB /resource/locator HTTP/1.1
Header1: Value1
Header2: Value2
...
<Body of request>

### Request Headers

* Hots: indicates the desired host handling the request
* Accept: indicates the MIME type(s) are accepted by the client; often used to specify JSON or XML output for web-services
* Cookie: passes cookie data to the server
* referer: page leading to this request (note: this not passed to other servers when using HTTPS on the origin)
* Authorization: Used for 'basic auth' pages (mainly). Takes the for "Basic <base64'd username:password>"

### Cookies

Cookies are key-value pairs of data that are sent from the server and reside on the client for a fixed period of time.

Each cookie has a domain pattern that it applies to and they're passed with each request the client makes to matching hosts.

#### Cookie Security

* Cookies added for .example.com can be read by any subdomain of example.com
* cookies added for a subdomain can only be read in that subdomain and its subdomains
* a subdomain can set cookies for its own subdomains and parent, but it can't set cookies for sibling domains
    + e.g. test.example.com can't set cookies on test2.example.com, but can set them on example.com and foo.test.example.com

There are two important flags to know for cookies:

* Secure: the cookie will only be accessible to HTTPS pages
* HTTPOnly: the cookie cannot be read by javascript

The server indicates these flags in the set-cookie header that passed them in the first place.

###

## HTML

### Parsing

HTML should be parsed according to the relevant spec, generally HTML5 now. But when you're talking about security, it's often not just parsed by your browser, but also Web-Application Firewalls and other filters. Wherever there's a discrepancy in how these two items parse things, there's probably a vulerability.

##### Canonical Example

You go to http://example.com/vulnerable?name=<script/xss%20src=http://evilsite.com/my.js> and it generates:

```html
<!doctype HTML>
<html>
<head>
    <title>
    Vulerable page named <script /xss src=http://evilsite.com/my.js>
    </title>
</head>
<html>
```
A bad XSS filter on the web application may not see that as a script tag due to it being a 'script/xss' tag. But Firefox's HTML parser, for instance, will treat the slash as whitespace, enabling the attack!

Now what would this do? Absolutely nothing on a browser, you'll have a blank XSS tag. However, a WAF would have let this straight through. Any discrepency will generally be able to pass through.

### Legacy Parsing

Due to decades of bad HTML, browsers are quite excellent at cleaning up after authors, and these conditions are often exploitable.

* a <script> tag on its own will automatically be closed at the end of the page
* a tag missing its closing angle bracket will automatically be closed by the angle bracked of the next tag on the page

## Content Sniffing

### MIME Sniffing

> MIME: Multipurpose Internet Mail Extensions

The broswer will often not just look at Content-Type header that the server is passing, but also the contents of the page. if it looks enough like HTML, it'll be parsed as HTML

This led to IE 6/7-era bugs where image and text files containing HTML tags would execute as HTML.

Imagine a site with a file upload function for profile pictures. If that file contains enough HTML to trigger the sniffing hueristics, an attacker could upload a picture and then link it to victims.

This is one reason why Facebook and other sites use a separate domain to host such content.

### Encoding Sniffing

Similarly, the encoding used on a document will be sniffed by (mainly older) browsers.

If you don't specify an encoding for an HTML document, the browser will apply hueristics to determine it. If you are able to control the way the browser decodes text, you may be able to alter the parsing.

A good example is putting UTF-7 (7-bit Unicode with Base-64'd blocks denoted by +...-) text into XSS payloads.

Consider the payload:

> +ADw-script+AD4-alert(1);+ADw-/script+ADr-

This will go cleanly through HTML encoding, as there are no 'unsafe' characters.

IE8 and below, along with a host of other older browsers, will see this in a page as UTF-7 and switch parsing over, enabling the attack to succed.

## Same-Origin Policy

What is SOP? Same-Origin Policy (SOP) is how the browser restricts a number of security-critical features:

* What domains you can contact via XMLHttpRequest
* Access to the DOM across separate frames/windows

### Origin Matching

The way origin matching for SOP works is much more strict than cookies:

* Protocol must match -- no crossing HTTP/HTTPS boundaries
* Port numbers must match
* Domain names must be an exact match - no wildcarding or subdomain walking

### SOP Loosening

Its possible for developers to loosen the grip that SOP has on their communications, by changing document.domain, posting messages between windows, and by using CORS (Cross-origin resource sharing).

All of these open up interesting avenues for attack. Anyone can call postMessage into IFrame - how many pages validate messages properly?

## CORS

CORS is still very new, but enables some very risky situations. In essence, you're allowed to make XMLHttpRequests to domains outside of your origin, but they have special headers to signify where the request originates, what custom headers are added, etc.

It's possible to even have it pass the receiving domain's cookies, allowing attackers to potentially compromise logged-in users. The securitty prospects here are still largely unexplored.

## Cross-Site Request Forgery

Usually if you find one in an app, you're going to find many, it's systemic.

### What is CSRF?

Cross-site Request Forgery is when an attacker tricks a victim into going to a page controlled by the attacker, which then submits data to the target site as the victim.

It is one of the most common vulnerabilities today, and enables a whole host of others, namely rXSS.

The canonical example is a bank transfer site. Here we have a form that allows a user to transfer money from their account to a destination account.

```html
<form action=/levels/0/" method="POST">
    <h2>Transfer Funds</h2>
    Destination Account: <input type="input" name="to" value""><br>
    Amount: <input type="input" name="amount" value="">
    <br>
    <br>
    <input type="submit" value="Transfer">
</form>
```

When the server gets such a transfer request from the client, how can it tell that it actually came from the real site? Referer headers are unreliable at best.

Here we can see an automatic exploit that will transfer money if the user is logged in.

```html
<body onload="document.forms[0].submit()">
    <form action="https://victim.vulnerable/levels/0/" method="POST">
    <input type="hidden" name="amount" value="1000000">
    <input type="hidden" name="to" value="1625">
    </form>
</body>
```

### Mitigation

Clearly, we need a way for the server to know for sure that the request has originated on its own page.

The best way to mitigate this bug is through the use of CSRF tokens. These are random tokens tied to user's session, which you embed in each for that you generate.

Here you can see a form containg a safe, random CSRF token. In this case, it's 32 nibbles of hex - plenty of randomness to prevent guessing it.

```html
<form action="post" method="POST">
    What's on your mind?<br>
    <textarea cols="40">
    <input type="hidden" name="csrf" value="8dbdb545d29dfc070911212d55cb871d">
    <input type="submit">
</form>
```

When the server gets a POST request, it should check to see that the CSRF token is present and matches the token associated with the user's session.

Note that this will not help you with GET requests typically, but applications _should not_ be changing state with GET requests anyway.

#### How not to mitigate

I've seen a number of sites implement "dynamic CSRF-proof forms". They had a csrf.js file that sends back code rougly equivalent to: $csrf = 'session CSRF token';

On each page, they had <script src="/csrf.js"> and then baked the CSRF token into the forms from there.

So all I had to do was include that same tag in my own exploit.

###

## Review

* Cookie domain scoping is often a source of trouble
* Same-origin Policy is strict, but complex enough to be a frequent source of headaches for defenders and attackers alike
* Cross-Site Request forgery is when an attacker tricks a victim into going to a page that triggers requests on other sites 
    + Use CSRF Tokens!

---

[Back to main repository!](../../README.md)

[Back to intro!](./intro.md)

[Onward to writing good reports!](./writing-good-reports.md)