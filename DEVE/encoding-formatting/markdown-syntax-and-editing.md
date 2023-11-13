

I believe that all the previously proposed solutions (apart from those that require specific implementations) result in the comments being included in the output HTML, even if they are not displayed.

If you want a comment that is strictly for yourself (readers of the converted document should not be able to see it, even with "view source") you could (ab)use the link labels (for use with reference style links) that are available in the core Markdown specification:

http://daringfireball.net/projects/markdown/syntax#link

That is:

```
[comment]: <> (This is a comment, it will not be included)
[comment]: <> (in  the output file unless you use it in)
[comment]: <> (a reference style link.)
```

Or you could go further:

> [//]: <> (This is also a comment.)

To improve platform compatibility (and to save one keystroke) it is also possible to use # (which is a legitimate hyperlink target) instead of <>:

> [//]: # (This may be the most platform independent comment)

For maximum portability it is important to insert a blank line before and after this type of comments, because some Markdown parsers do not work correctly when definitions brush up against regular text. The most recent research with Babelmark shows that blank lines before and after are both important. Some parsers will output the comment if there is no blank line before, and some parsers will exclude the following line if there is no blank line after.

In general, this approach should work with most Markdown parsers, since it's part of the core specification. (even if the behavior when multiple links are defined, or when a link is defined but never used, is not strictly specified).
