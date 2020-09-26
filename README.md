With this Microbit python project you can send messages to another Microbit
through a radio signal.

How to use this program?
When you start the Microbit the top left led will be turned on.
If you press button A, the cursor(i.e. the led) will cycle throug all
the led's. Every led contains a letter. The first one being A, the secon B etc. (There is no Z, use an S)

When you press B the letter that you're currently on will be added to your message.
If your done 'typing' press A and B at the same time. Your message wil be displayed.
Press A to send your message to everyone on the same radio group.
Press B to cancel sending your message. Your message won't be deleted.

To..
Delete your message > Put the face of the microbit downwards
Reset the cursor > Cycle through the alplabet OR shake te microbit.

If you receive a message that's longer than 30 charachters an X is displayed. 
You can turn this off by deleting the followwing lines: 52, 54, 55, 56, 57



> Open this page at [https://reinder-github.github.io/texting/](https://reinder-github.github.io/texting/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/reinder-github/texting** and import

## Edit this project ![Build status badge](https://github.com/reinder-github/texting/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/reinder-github/texting** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/reinder-github/texting/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
