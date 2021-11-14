# PhishAR Interview Assignment

Preview the application [here](http://arcane-shore-01572.herokuapp.com).

## Thought process

First thing that came to mind was to use an OCR on a web page screenshot and
look for some known words and phrases for each known hostname. For that sake I
used a [Tesseract](https://github.com/tesseract-ocr/tesseract) OCR. While it
worked on some examples, there were some problems. For example, the CNN web page
contains only the CNN logo which is very hard to read with OCR. Also, there
would be a problem if one page has an article about the other, as the article's
title would probably contain the words or phrases of that page.

The second idea was to save known logos of each of the known hosts and look for
that logo on every queried screenshot. The problem with that is in matching the
logos, as a deep learning model would be needed and I didn't have the time and
resources. The non-deep-learning solutions include the matching that requires
the same dimensions of the known logo and the logo on a screenshot, which is
not at all robust. There is also a problem of one page referencing the other as
the logo of the other page might be in the article's image.

I then started researching the image similarity measures. That way I would save
the screenshot of each known host and then compare that screenshot to the
queried image. First thing that came to mind was to learn the image
feature-vectors by running the known images through a CNN, but again, I didn't
have enough time nor resources.

## Solution

Next thing on my mind was the computation of image hashes. Similar images would
have similar image hashes. While maybe that would be a better solution, in the
middle of implementing different image hashes, I suddenly remembered the SIFT,
SURF and FAST feature detection algorithms. While again reading about them I
decided to go with the ORB algorithm, as it was free and efficient.

I precompute the features for all known host screenshots and save them to a
dictionary. When a new query arrives, the features for the new image are
computed. I limited the number of features to 500. Now I loop through all the
precomputed image features and for each one match the corresponding features.
Matching is performed using the hamming distance. The 10 best matches are taken,
their average hamming distance computed and that measure is used as a score for
the corresponding web host. Now, the web host with the smallest distance is
taken. If that distance is less then the given threshold of 15, it is a match!
Otherwise, the image is of an unknown host.

The proposed solution should also work on some photographs of screens, if the
screen is not too warped. It is highly configurable and it is also easy to
implement the new feature exraction algorithms. Honestly, I didn't dedicate much
time for parameter tweaking, as my time was limited.

**Note:** all the mentioned constants are configurable.
