# Firefox Customizations

Firefox customizations I use because the defaults are so bad

## What does it do?

- Enables `userChrome.css` (warning: may slow down initial startup)
- Removes the "List all tabs" chevron
- Disables all Pocket (extension) related functionality

## Setup

There is a handy Python script that does the manual steps outlined below for you. Simply run with `./install.py`! If you are a masochist, keep reading :)

### Manual steps

- Open your profile folder. You can find this by going to about:profiles. Click on "Show in Finder" or "Show in Explorer" in the "Root Directory" row of the currently active profile.
- Make a new folder named `chrome`
- Copy the `userChrome.css` file inside
- Back at the root of the profile folder, copy the `user.js` file inside.

