The [babel-sublime plugin](https://github.com/babel/babel-sublime) has this comment style built in and is most likely what you want, but if you for some reason only want the commenting style, feel free to use this plugin.

JSX Comment plugin for Sublime Text
===================================
This very very simple plugin adds JSX comment functionality for Sublime Text through a custom keyboard shortcut.


Installation
------------
The plugin must be installed into the User folder.

On OS X this can be done with:

    cd ~/"Library/Application Support/Sublime Text 3/Packages"
    git clone https://github.com/Briix/JSXComment-Sublime-Plugin.git JSXComment


and on Windows with:

    cd "%APPDATA%\Sublime Text 3\Packages"
    git clone https://github.com/Briix/JSXComment-Sublime-Plugin.git JSXComment


Keyboard Shortcut
-----------------
This plugin features, as of now, a single shortcut that will wrap a block or line with `{/* */}`

|Feature    | Shortcut    |
|-----------|-------------|
|Comment    | `^ Shift C` |

