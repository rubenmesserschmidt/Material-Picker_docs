Changelog
#########

|
1.2.0
*****

New Features
^^^^^^^^^

* **Material Property Popup**
   You can now open a popup with all material properties when holding ``SHIFT`` while picking. Find out more :ref:`here <Material Picker>`.

* **Material Browser**: New filter
   You can now filter materials by objects, collections, and their source. Find out more :ref:`here <Material Browser>`.

* **Material Browser**: Rename menu
   You can now rename materials by replacing specificed characters with new ones. Find out more :ref:`here <Material Browser>`.

Bug Fixes
^^^^^^^^^

* **Linked Materials: Show Local**
   Linked materials can now be shown locally every time, no matter how they're attached to the object.

* **Linked Materials: Load File**
   Fixed a rare issue where the workspace automatically switched to 'Shading' when opening a file.

|
1.1.0
*****

New Features
^^^^^^^^^

* **Material Browser**
   There is now a material browser available in the Sidebar of the Shader Editor. Find out more :ref:`here <Material Browser>`.


|
1.0.2
*****

Bug Fixes
^^^^^^^^^

* **Load linked File**
   Fixed an issue where the material got not automatically selected on loading a linked file.

* **Library override Objects**
   Material Picker now works with library override objects as expected.


|
1.0.0
*****

Initial Release


.. |
.. 1.1.0
.. *****

.. New Features
.. ^^^^^^^^^^^^

.. * **Expanded Preferences**: Added more default settings.
..    :Default Material: :ref:`See here <Settings>`.
..    :Default Empty Size: :ref:`See here <Settings>`.
.. |

.. * **Export Object**: Added the option to export cross sections as object for use inside blender.
.. |

.. * **Export DXF Settings**: Added more export settings.
..    :Clean Mesh: :ref:`See here <Plane Settings>`.
.. |

.. * **Hide Render**: Added the option to hide the sections in renders only.
.. |

.. * **Loading Indicator**: Loading is now indicated by the mouse cursor when using performance heavy features on more complex objects, to make clear when a operation is finished.
.. |

.. * **Merge Panels**: Added the option to merge all panels of my addons into a single panel called *Ruben's Addons*. You'll find the option under the addon preferences (*Edit>Preferences>Add-Ons>Material Picker*).
.. |


.. Bug Fixes
.. ^^^^^^^^^

.. * **Geometry Nodes**:
..   Fixed not working sections when using instances that are not realized.
..   Fixed an issue when having a 'Set Material' node with a empty material property in the node tree.
.. |

.. * **Non-Geometry Objects**: Fixed an issue when creating a Material Picker while having non-geometry objects selected.
.. |


 