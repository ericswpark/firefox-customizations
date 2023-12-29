# Firefox Customizations

Firefox customizations I use because the defaults are so bad

## What does it do?

- Enables `userChrome.css` (warning: may slow down initial startup)
- Removes the "List all tabs" chevron
- Disables all Pocket (extension) related functionality

## Setup

If you are on Windows or macOS, there is a handy Python script that does the manual steps outlined below for you. Simply run with `./install.py`! If you prefer to do it on your own or if you are on another platform, keep reading :)

- Open your profile folder. You can find this by going to about:profiles. Click on "Show in Finder" or "Show in Explorer" in the "Root Directory" row of the currently active profile.
- Make a new folder named `chrome`
- Copy the `userChrome.css` file inside
- Back at the root of the profile folder, copy the `user.js` file inside.

[about:profiles]: about:profiles
