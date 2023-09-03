########
Features
########

.. _Material Picker Feature:

***************
Material Picker
***************

:Area: 3D Viewport
:Menu: Context Menu ‣ Material Picker
:Hotkey: ``Alt + M`` (Changable in the :ref:`Preferences`)

Hover over any material in the viewport and then press `Leftclick` to select it.
For showing the material the following cases are considered:

1. The material is assigned to a material slot of the object

   * The object will be selected and the according material slot will be made active.

2. The material is otherwise assigned to the object (e.g. Geometry Nodes 'Set Material Node')   

   * A new hidden object will be created and the material will be assigned to it.
   * Then **1** will be applied.

3. The material is part of an object that is instanced (e.g. Collection Instance)

   * The original object will be searched.
   * Then **1** or **2** will be applied.

4. The material is part of an object that is linked from another *.blend* file

   * A popup window will appear asking if you want to load the linked file or show the material locally

     * **Load File**: The linked file will be loaded in a new blender instance. Then **1** or **2** will be applied and the *Shading* workspace will be activated.

        :Auto Reload: If the material in the linked file is changed, the material will be updated automatically. Needs to be enabled in the :ref:`Preferences`.
    
     * **Show Local**: **1** or **2** will be applied but the material is not editable, since it remains linked.

During picking you can enable the following features by holding the according key:

* ``SHIFT``: Edit the picked material in a popup window.
* ``ALT``: Pick all materials laying under your mouse cursor resulting in a list of materials to choose from (just like when holding alt when selecting objects in the viewport).
* ``CTRL``: Take also objects into consideration which are displayed as wire, else they are ignored.

You can change the modifier keys to hold for these features in the :ref:`Preferences`.


****************
Material Browser
****************

:Area: Shader Editor
:Menu: Sidebar ‣ Material Browser

| Browse through all materials in your blend file.
| Select one to show it's node tree immediately. For showing the material node tree the same cases as for the Material Picker are considered.

.. attention:: 
   Use the reload button below the list to keep the material browser up to date. This is necessary after adding or removing materials in your blend file.

The following features are available:

* **Select**: Select an existing material and show it's node tree.
* **Add**: Add a new material to the blend file.
* **Remove**: Remove the selected material from the blend file.
* **Rename Menu**: Rename material names by replacing specified characters with new ones.

   :Find: The characters to be replaced.
   :Replace: The characters to replace the found ones with.
   :Case Sensitive: If enabled, the search will be case sensitive.
   :Regex: If enabled, the search will be treated as a regular expression.
   :Replace: Replaces the first material name with matching characters.
   :Replace All: Replaces all material names with matching characters.


The following filter options are available:

* **Source**: Show either all materials of the blend file or only the ones in the current scene.
* **Search**: Search for materials by name. Use ``*`` as wildcard.
* **Favorites**: Show only materials marked as favorite.
* **Object**: Show only materials assigned to a specific object.
* **Collection**: Show only materials assigned to a specific collection.

The following sorting options are available:

* **Name**: Order by name alphabetically.


***************
Material Search
***************

:Area: Shader Editor
:Menu: Context Menu ‣ Material Browser
:Hotkey: ``Alt + M`` (Changable in the :ref:`Preferences`)

Fast search for materials by name. The chosen material will also be selected in the Material Browser.
