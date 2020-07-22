# pugmark

Simple output of text formatted in markdown.

---

## Install

```sh
pip install git+https://github.com/holmescharles/pugmark
```

## Usage

Let's say you want to create a markdown file in which to log text while working in python.

```python
import pugmark

mdfile = pugmark.MarkdownFile('output.md')

mdfile.head(level=1, text='This is a heading.')
mdfile.para('This is a body. Here comes some code.')
mdfile.code_block('echo This is some code', language='sh')
mdfile.head(level=2, text='This is a sub-heading.')
mdfile.para('More text!')

mdfile.close()
```

...to produce...

````
# This is a heading.

This is a body. Here comes some code.

```sh
echo This is some code
```

## This is a sub-heading.

More text!
````
