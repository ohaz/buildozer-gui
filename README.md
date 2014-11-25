buildozer-gui
=============

A gui for buildozer (https://github.com/kivy/buildozer)

First basic usage works. It's still beta, so if you want to use it on an existing project
make a backup of your buildozer.spec first! No warranty for broken / lost files!

Requirements
------------

* kivy>=1.8.0
* buildozer
* python 2.7

Instructions
------------

* cd to the directory of your application
* run buildozer-gui (currently done with python PATH/TO/BUILDOZER-GUI/main.py)
* create a new project / edit an existing project and follow the UI instructions

Example Screenshot
------------
![Screenshot 1](http://i.imgur.com/coatl6m.png)

TODO
------------

* Editing iOS Codesign does not work. Needs some regex love :)
* Give some options a better way of changing them. (e.g. Paths could get a file option dialog)
* Add ways to set a specific option to the default value specified in https://github.com/kivy/buildozer/blob/master/buildozer/default.spec
* Change current working directory
* Add ways to set a specific option to a user-defined default value (e.g. android sdk/ndk path!)
* Better error-handling