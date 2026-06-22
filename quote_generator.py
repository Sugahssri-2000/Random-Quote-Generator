import random
from IPython.display import display, Markdown

quotes = [
    "Never stop learning.",
    "Success starts with consistency.",
    "Small progress is still progress.",
    "Believe in yourself.",
    "Every day is a new opportunity."
]

quote_of_the_day = random.choice(quotes)

markdown_output = f"""
# 💡 Quote of the Day:

> **{quote_of_the_day}**
"""

display(Markdown(markdown_output))