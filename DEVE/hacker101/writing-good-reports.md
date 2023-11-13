# Writing Good Reports

What makes a good bug report and how can you become a more successful bug hunter.

## Why Write Reports?

If your'e a bug bounty hunter and you're finding great bugs, why does it matter whether or not you write a good report?

At the end of the day, is there anything more important than the techincal quality of your work?

Your goal with a report should be to give the most useful information possible to the product team. This means they can traige and confirm your bugs faster; this gets the money into your pocket even sooner.

It also leads to fewer questions from the team, making everyone's lives easier.

## What is a good report?

* Clear description of the bug
* Real-world impact
* Concise reproduction steps
* Working examples
    + Proof of concept links/payloads
    + screenshots
    + source code snippets

## Description - Bad

"When submitting feedback, the title tage value isn't escaped, allowing XSS attacks."

Problems:

* Where does the title come from?
* What privileges are required to execute this attack?
* Which page(s) are actually affected?

## Description - Good

"Within the administration panel of the site, administrators are able to set the default value for the '<title>' tag, to which page names are prepended. On the "Submit Feedback" page (https://example.com/portal/feedback), this value is not escaped properly. This means that an attacker with administrative privileges can inject arbitrary HTML into a page, thus effecting a cross-site scripting attack."

1. Login to the application as an adminstrator
2. Go to https://example.com/admin/settings
3. Set the page title field to:

> '</title><script>alert(document.cookie);</script>'

4. Go to https://example.com/portal/feedback
5. Note the alert dialog that occurs

## Impact - Bad

"Attackers can add any HTML to a page, which is cross-site scripting."

Problems:

* What can an attacker accomplish with this?
* Does "a page" mean a specific page? If so, which?
* What does the attack flow look like in practice?

## Impact - Good

"An attacker is able to execute JavaScript in the context of the "Submit Feedback" page. This code is able to perform any action that the victim could ordinarily perform, e.g. making posts and sending messages. As this page is accesssible to all users and is clicked commonly, this may allow an attacker to compromis a large number of users without any new interaction being forced."

## Screenshots - Bad

![Bad Bug Report Screenshot](../../img/bad-bug-report-screencap.png)

This doesn't tell you anything about:

* The affected page
* parameters/fields affected

## Screenshots - Good

![Bad Bug Report Screenshot](../../img/good-bug-report-screencap.png)


This shows the URL, affected parameter, and the cookies readable from the browser.

## Determining Impact

WHen it comes to determining the impact of a vulnerabilty, the key thing is thining like an attacker.

What things are important to the business behind the application? If you can figure out what's important to the business, you can figure out what an attacker would be targeting and thus how your vulnerability can be used for that.

When you're talking about the impact of a bug, talking about the techincal details misses the point. Businesses don't care about SQL injection, they care about the user information being access or destroyed. They don't care about cross-site scripting, they care about fraudulent orders.

## Soft Skills

Once you've started findng bugs, the single biggest thing you can do to increase bounty payouts is to work on your soft skills. Do you have issues with spelling or grammar? There are plenty of resources online to work on those. Have your reports ben closed N/A when you think they shouldn't be? Maybe you're not presenting it to the team in a useful and actionable way,

## Read! 

On HackerOne you can find thousands of reports from real hackers. These hackers range from absolute beginners to the best in the business, but you can learn from every one of them. If you read a lot of reports, you'll notice things that make them particularly good or bad. Use those to make your own reports better.

That's all for introductory information folks!

---

[Back to main repository!](./README.md)

[Back to the web in depth!](./web-in-depth.md)
