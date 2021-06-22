# Hacker101 - Introduction

## What you'll learn

* Required tools
* Thinking like a breaker
* Attacker-defender imbalance
* Lightweight threat assessment and prioritization
* How to write good bug reports
* Reflected XSS (Cross-Site Scripting)

## Welcome

It's a good idea to have a few things that you're familiar as they will be with you from the beginning until the end. These tools are:

* a web request library
    + Python's _requests_ library
    + _postman_
* burp proxy
    + never used this before
    + there is a pro and freeware edition
* Firefox
    + better developer tools than Chrome

You're goal is the break everything, and also be the first one to do so. You will have to stop thinking with a defensive mindset and switch to an offensive, or attackers mindset.

Attackers will always have an advantage over defenders, because defenders are supposed to find every single bug. That isn't always possible and can be especially challenging under time constraints.

Assessing what an attacker actually wants is one of the most important tasks. Once you have some kind of understanding, you can begin to prioritize what is most important to safeguard.

## Reporting

For the purposes of this course, and in general, these are the following bullets needed:

* Title -- E.g. "Reflected Cross-Site Scripting in profiles"
* Severity
* Description -- Brief description of what the vulnerability is
* Reproduction Steps -- brief description of how to reproduce bug; preferably with a small proof of concept
* Impact -- what can be done with the vulnerability?
* Mitigation -- how is it fixed?
* Affected Assets -- Generally a list of affected URLs

### Severity

Severity is subjective and is handled differently everywhere, but here's a loose template:

* Informational
    + Issue has no real impact
* Low
    + The business impact is minimal
* Medium
    + Potential to cause harm to users, but not revealing data
* High
    + Potential to reveal user data or aids in exploitation of other vulnerabilities
* Critical
    + High risk of personal/confidential data exposure, general system compromise, and other severe impacts to business

## First Bug Example

```php
<?php
if(isset($_GET['name'])){
    echo "<h1>Hello {$_GET['name']}!</h1>";
}
?>
<form method="GET">
Enter your name: <input type="input" name="name"><br>
<input type="submit">
```

It seems relatively straight forward and simple, right? Well here's the problem, you can potentially exploit a web URL like this using that same name tag:

> http://vulnerable.example.com/page.php?name=<script>alert(1);</script>

The HTML would be: <h1>Hello<script>alert(1);</script>!</h1>

### Reflected XSS

What you've just seen is an example of reflected cross-site scripting (a.k.a. Reflected XSS or rXSS)

A parameter that an attacker controls is directly reflected back to a user. This could allow injection of raw HTML or Javascript (depending on where the XSS takes place) and allow an attacker to perform actions in the context of another user.

---

[Back to table of content!](../README.md)

[Onward to the web in depth!](./web-in-depth.md)