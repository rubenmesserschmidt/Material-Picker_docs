#########
Changelog
#########

*****
1.3.0
*****

New Features
============

* **4.2 Extensions Compatible**
    Material Picker is now compatible with Blender 4.2 extensions.

Bug Fixes
=========

* **Material Picker: Select Material**
   Fixed an issue where when no material was found, an error could occur.

* **(macOS) Material Picker: Linked Materials**
   Fixed an issue where linked materials didn't update when changing the material in the source file on macOS.

*****
1.2.1
*****

Bug Fixes
=========

* **Material Browser: Reload**
   Fixed an issue where an error message occured when there was a non-geometry object in the scene while reloading the browser.

* **Material Picker: Pick Material**
   Fixed an issue where an error message occured when picking from objects with empty material slots.

*****
1.2.0
*****

New Features
============

* **Material Property Popup**
   You can now open a popup with all material properties when holding ``SHIFT`` while picking. Find out more :ref:`here <Material Picker>`.

* **Material Browser**: New filter
   You can now filter materials by objects, collections, and their source. Find out more :ref:`here <Material Browser>`.

* **Material Browser**: Rename menu
   You can now rename materials by replacing specificed characters with new ones. Find out more :ref:`here <Material Browser>`.

Bug Fixes
=========

* **Linked Materials: Show Local**
   Linked materials can now be shown locally every time, no matter how they are attached to the object.

* **Linked Materials: Load File**
   Fixed a rare issue where the workspace automatically switched to 'Shading' when opening a file.

*****
1.1.0
*****

New Features
============

* **Material Browser**
  There is now a material browser available in the Sidebar of the Shader Editor. Find out more :ref:`here <Material Browser>`.


*****
1.0.2
*****

Bug Fixes
=========

* **Load linked File**
   Fixed an issue where the material got not automatically selected on loading a linked file.

* **Library override Objects**
   Material Picker now works with library override objects as expected.


*****
1.0.0
*****

Initial Release


 