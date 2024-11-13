# pic2pdf

A simple command line tool to convert a folder of images into a single pdf.
### Usage:
```python pic2pdf <insert desired path of output pdf> <insert path to directory of images> <<optional switches>>```

or via wrapper bash script:\
```./pic2pdf <insert desired path of output pdf> <insert path to directory of images> <<optional switches>>```

### Switches:

**-n** (default) order images in pdf by their filename  (descending lexicographical order)\
**-d** order images in pdf by file date (descending file modification time)

### Example Usage:

```python pic2pdf out.pdf ~/Downloads/assignment1\ imgs```\
```./pic2pdf ~/school/assignment1/output.pdf ~/Downloads/imgs/ -d```

