# diagrams-ocr-test
About
evaluating the possibilities of extracting text from image diagrams with complex background

# GPT4

not conclusive, OCR not possible and SVg require custom cleaning
details in [gpt4/readme.md](./gpt4/readme.md)
# Tesseract
* https://github.com/tesseract-ocr/tesseract
* https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html#simplest-invocation-to-ocr-an-image

example command
```bash
tesseract test_slide.png test_slide --psm 11 -l eng pdf
```

help output see [tessteract-help.md](./tesseract-help.md)
