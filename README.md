<a id="top"></a>

<p align="center">
<img src="./docs/assets/manufai-hero.svg" width="100%" alt="MANUFAI FreeCAD Plugin — Welding engineering and simulation">
</p>

<p align="center">
<a href="https://www.manufai.com/freecad"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/WeldWorkbench.svg" width="18" height="18" alt="MANUFAI Workbench icon"> <strong>Download plugin</strong></a> &nbsp;·&nbsp;
<a href="#installation">Installation</a> &nbsp;·&nbsp;
<a href="#activation">Activation</a> &nbsp;·&nbsp;
<a href="#toolbar-layout">Tool index</a> &nbsp;·&nbsp;
<a href="#repository-resources">Test resources</a>
</p>

<table>
<tr><th>FreeCAD</th><th>Installer</th><th>External workflows</th></tr>
<tr><td><code>1.1.1</code> required</td><td>Windows <code>.exe</code></td><td>RoboDK · C3P · WSO</td></tr>
</table>

<a id="overview"></a>

## Welding engineering & simulation

<p>

 <strong>MANUFAI</strong> is a specialized workbench for FreeCAD, developed to integrate 3D CAD design with the planning, preparation, and simulation of welding processes.   
</p>
<p>
Its main objective is to transform CAD geometry into usable manufacturing information, enabling users to define welding trajectories, tool orientations, process parameters, operation sequences, and the data required for subsequent simulations, all within the same working environment.
</p>
<p>
The plugin is designed to facilitate the transition between digital design and manufacturing process execution, reducing manual tasks and centralizing the information associated with the welding process.
</p>

<details>
<summary><strong>Key capabilities</strong></summary>
<br>

<ul>
  <li>
    <strong>Intelligent Geometry Analysis:</strong>
    Analyzes the 3D model geometry to identify edges and potentially weldable
    regions, including T-joints, 90° joints, and other relevant configurations.
  </li>

  <li>
    <strong>Weld Path Generation:</strong>
    Allows users to generate and configure welding trajectories from the selected
    geometry, including continuous welds, edge offsets, and intermittent welds.
  </li>

  <li>
    <strong>Welding Orientation Definition:</strong>
    Calculates and assigns normal vectors and orientations along the welding
    trajectories, providing the information required to correctly define the
    position and orientation of the welding torch.
  </li>

  <li>
    <strong>Process Parameter Management:</strong>
    Allows technological information and welding process parameters to be assigned,
    such as speeds, materials, preparation data, resources, and other information
    required for subsequent calculations and simulations.
  </li>

  <li>
    <strong>Process Simulation &amp; Sequencing:</strong>
    Facilitates the definition of the welding execution order and allows operations
    performed by robots, human operators, or auxiliary equipment to be organized,
    supporting process analysis and cycle-time calculations.
  </li>

  <li>
    <strong>Robotic Workflow Integration:</strong>
    Prepares welding trajectories and orientation information for use in external
    robotic simulation and programming tools, such as RoboDK.
  </li>

  <li>
    <strong>Manufacturing Data Organization:</strong>
    Structures project information within FreeCAD, facilitating the organization
    of welds, positions, resources, and manufacturing operations.
  </li>

  <li>
    <strong>Engineering Reports:</strong>
    Generates useful information for project documentation and analysis, including
    welding length, operation times, process parameters, and manufacturing-related
    estimates.
  </li>
</ul>

</details>

<details>
<summary><strong>Interoperability: from CAD to manufacturing</strong></summary>
<br>

<p>

 <strong>MANUFAI</strong> is designed to integrate FreeCAD into a broader manufacturing workflow, facilitating the connection between CAD design, process preparation, simulation, and manufacturing programming.  
</p>
<p>
The plugin acts as a bridge between the information generated in FreeCAD and specialized simulation, robotics, and analysis tools, enabling the transfer of welding trajectories, orientations, and process data to external platforms used in industrial environments.
</p>
<ul>
  <li>
    <strong>Integration with Specialized Software:</strong>
    Facilitates connectivity with tools such as RoboDK, C3P, and other simulation and computational environments.
  </li>

  <li>
    <strong>Manufacturing Data Transfer:</strong>
    Enables the export of welding trajectories and process parameters for subsequent stages of simulation, programming, or validation.
  </li>

  <li>
    <strong>Pre-Manufacturing Validation:</strong>
    Helps evaluate aspects such as trajectory, orientation, kinematics, and process behavior before physical implementation.
  </li>

  <li>
    <strong>Digital Workflow Continuity:</strong>
    Maintains a structured connection between the CAD model and the subsequent stages of engineering and manufacturing.
  </li>
</ul>
<p>
In this way, <strong>MANUFAI</strong> allows FreeCAD to function not only as a design tool, but also as a starting point for the planning, simulation, and digital preparation of welding processes.
</p>

</details>

<a id="installation"></a>

## Download & installation

<ol>
<li><strong>Download.</strong> Get the <code>.exe</code> installer from <a href="https://www.manufai.com/freecad">MANUFAI – FreeCAD Plugin</a>.</li>
<li><strong>Install.</strong> Run the executable and follow the setup wizard. If prompted by Windows SmartScreen, click “Run anyway.” The installer automatically locates your FreeCAD <code>Mod</code> directory.</li>
<li><strong>Restart FreeCAD.</strong> The MANUFAI workbench will be available in the workbench selector.</li>
</ol>
<p><strong>Required FreeCAD version:</strong> <code>1.1.1</code>.</p>
<p><a href="https://youtu.be/3LZCjwZW4YY">Watch installation tutorial · Sign up and download FreeCAD Plugin</a></p>

<a id="activation"></a>

## Activation

<table><tr>
<td width="66" align="center"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Acvitator.svg" width="44" height="44" alt="Activator icon"></td>
<td><strong>Activator</strong><br>Select MANUFAI in the FreeCAD workbench selector, then click the Activator button.</td>
</tr></table>
<ol>
<li>Obtain your <strong>Serial Key</strong> and enter it into the corresponding field.</li>
<li>Click <code>+</code> to add the key.</li>
<li>Click <code>Activate</code>.</li>
</ol>
<p><a href="https://youtu.be/MNOla3Mc2aI">Watch activation tutorial · Get your license key and activate MANUFAI FreeCAD plugin</a></p>

<a id="plugin-component-manager"></a>

## Plugin Component Manager

<table><tr>
<td width="66" align="center"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MANUFAI_welding_SVG_V5.svg" width="44" height="44" alt="Modifier icon"></td>
<td><strong>Modifier</strong><br>Open the Plugin Component Manager to choose which toolbars and features are displayed.</td>
</tr></table>
<ol>
<li>Click the <strong>Modifier</strong> button in the MANUFAI toolbar. The Plugin Component Manager setup window opens.</li>
<li>Check or uncheck the components you want to show or hide.</li>
<li>Click <code>Install</code> to save the changes, then restart FreeCAD.</li>
</ol>
<ul>
<li><strong>MANUFAI Workbench</strong> — required; cannot be disabled.</li>
<li>3-2-1 Datum Based Alignment Tools.</li>
<li>C3P – WdCurve Tools.</li>
<li>RoboDK &amp; Process Automation.</li>
</ul>

<a id="repository-resources"></a>

## Repository structure & test resources

<p>
To ensure you can replicate the workflows shown in the demonstrations, <strong>each tool/button has its own dedicated folder</strong> in this repository. Inside each tool's folder, you will find the following organized resources:
</p>
<ul>
  <li>
    <strong>Tool Icon:</strong>
    The image file of the button for easy visual identification.
  </li>
  <li>
    <strong>📂 01 Files needed to test:</strong>
    Contains the exact input files (CAD models, scripts, etc.) required to perform the test shown in the video.
  </li>
 <li>
    <strong>📂 02 Output:</strong>
   Contains the <strong>final result</strong> generated by the tool (exported files, reports, or modified geometry), serving as a reference to verify that the tool executed correctly.
  </li>
</ul>

<a id="toolbar-layout"></a>

## Tool index

Choose a component to browse its tools. Each tool includes its description, demonstration video and test resources.

<details>
<summary><strong>MANUFAI Workbench</strong></summary>
<br>
<p><strong><a href="#make-weld-trajectories">Make Weld Trajectories</a></strong></p>
<ul>
<li><a href="#edge-split"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Extract_edges_20.svg" width="16" height="16" alt=""> Edge Split</a></li>
<li><a href="#find-weldable-edges"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Find_Weld_edges_21.svg" width="16" height="16" alt=""> Find Weldable Edges</a></li>
<li><a href="#weld-creators"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Weld_tree_item.svg" width="16" height="16" alt=""> Weld Creators</a></li>
<li><a href="#add-normals"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Normals.svg" width="16" height="16" alt=""> Add Normals</a></li>
<li><a href="#surface-weld"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/welding-icon.svg" width="16" height="16" alt=""> Surface Weld</a></li>
<li><a href="#weld-loader"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/import1.svg" width="16" height="16" alt=""> Weld Loader</a></li>
</ul>
<p><strong><a href="#positions">Positions</a></strong></p>
<ul>
<li><a href="#make-positions"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Make_position_groups.svg" width="16" height="16" alt=""> Make Positions Groups</a></li>
<li><a href="#assign-welds-to-robots"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/AssignWeldsToRobots.svg" width="16" height="16" alt=""> Assign Welds To Robots</a></li>
<li><a href="#subassembly"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/CreateSA.svg" width="16" height="16" alt=""> SubAssembly</a></li>
<li><a href="#assign-positions"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/AssigSA.svg" width="16" height="16" alt=""> Assign Positions</a></li>
<li><a href="#move-subassembly"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveSA.svg" width="16" height="16" alt=""> Move SubAssembly</a></li>
<li><a href="#move-welds"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveWelds.svg" width="16" height="16" alt=""> Move Welds</a></li>
</ul>
<p><strong><a href="#length">Length</a></strong></p>
<ul>
<li><a href="#weld-length-report"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report1.svg" width="16" height="16" alt=""> Weld Length Report</a></li>
</ul>
<p><strong><a href="#cycle-time-tools">Cycle Time</a></strong></p>
<ul>
<li><a href="#process"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Process_V2.svg" width="16" height="16" alt=""> Process</a></li>
<li><a href="#assign-process"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign%20process.svg" width="16" height="16" alt=""> Assign Process</a></li>
<li><a href="#welding-parameters"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Welding_parameters.svg" width="16" height="16" alt=""> Welding Parameters</a></li>
<li><a href="#assign-welding-parameters"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign%20weld%20parameters_v3.svg" width="16" height="16" alt=""> Assign Welding Parameters</a></li>
<li><a href="#cycle-time"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report3_cycle_time.svg" width="16" height="16" alt=""> Cycle Time</a></li>
</ul>
<p><strong><a href="#weight">Weight</a></strong></p>
<ul>
<li><a href="#create-materials"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Create%20Material.svg" width="16" height="16" alt=""> Create Materials</a></li>
<li><a href="#assign-materials"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign_material_v4.svg" width="16" height="16" alt=""> Assign Materials</a></li>
<li><a href="#weight-of-welding-and-welded-part"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report2.svg" width="16" height="16" alt=""> Weight of Welding and Welded Part</a></li>
</ul>
<p><strong><a href="#wso">Welding Sequence AI Advisor</a></strong></p>
<ul>
<li><a href="#export-stl"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/stl-file-format-icon.svg" width="16" height="16" alt=""> Export STL</a></li>
<li><a href="#export-as-dk-project"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Export_DKproj_v4.svg" width="16" height="16" alt=""> Export As DK Project</a></li>
</ul>
<p><strong><a href="#simulation">Sequence and Process Visualization</a></strong></p>
<ul>
<li><a href="#assign-sequence"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Define%20Sequence.svg" width="16" height="16" alt=""> Assign Sequence</a></li>
<li><a href="#weld-simulation"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Run_simulation3.svg" width="16" height="16" alt=""> Weld Simulation</a></li>
<li><a href="#weld-visualizer"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/weld_sphere.svg" width="16" height="16" alt=""> Show Weld Sphere</a></li>
<li><a href="#visualizer-cmd"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/show.svg" width="16" height="16" alt=""> Visualizer</a></li>
</ul>
</details>

<details>
<summary><strong>3-2-1 Datum Based Alignment &amp; Tools</strong></summary>
<br>
<ul>
<li><a href="#toggle-visibility-recursive"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Toggle_Visibility_Recursive.svg" width="16" height="16" alt=""> Toggle Visibility Recursive</a></li>
<li><a href="#create-center-point"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/CENTRO.svg" width="16" height="16" alt=""> Create Center Point</a></li>
<li><a href="#create-sphere-at-origin"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/ORIGEN.svg" width="16" height="16" alt=""> Create Sphere at Origin</a></li>
<li><a href="#datum-a"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_A.svg" width="16" height="16" alt=""> Datum A</a></li>
<li><a href="#datum-b"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_B.svg" width="16" height="16" alt=""> Datum B</a></li>
<li><a href="#datum-c"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_C.svg" width="16" height="16" alt=""> Datum C</a></li>
<li><a href="#3-2-1-alignment"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/ALINEACION.svg" width="16" height="16" alt=""> 3-2-1 Datum-Based Alignment</a></li>
<li><a href="#move-model-to-origin"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MOVER.svg" width="16" height="16" alt=""> Move Model To Origin</a></li>
<li><a href="#reset-pos"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Part_Box.svg" width="16" height="16" alt=""> Reset Position</a></li>
<li><a href="#show-welding-widget-command"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/welding-image-tool.svg" width="16" height="16" alt=""> Show Welding Widget</a></li>
<li><a href="#launch-find-data-panel"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATA_ICON.svg" width="16" height="16" alt=""> Launch Find Data Panel</a></li>
<li><a href="#focus-object-command"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/focus_icon.svg" width="16" height="16" alt=""> Focus Object</a></li>
<li><a href="#move-weld-lines"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveWeldlines.svg" width="16" height="16" alt=""> Move Weld Lines</a></li>
<li><a href="#discretize"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DIZCRE.svg" width="16" height="16" alt=""> Discretize</a></li>
</ul>
</details>

<details>
<summary><strong>C3P – WdCurve Tools</strong></summary>
<br>
<ul>
<li><a href="#line-weld-table"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/table_icon.svg" width="16" height="16" alt=""> Line Weld Table</a></li>
<li><a href="#show-names"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/names_icon.svg" width="16" height="16" alt=""> Show Names</a></li>
<li><a href="#selection-mode"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/selection_mode.svg" width="16" height="16" alt=""> Selection Mode (X-Ray &amp; Filter)</a></li>
</ul>
</details>

<details>
<summary><strong>RoboDK &amp; Process Automation</strong></summary>
<br>
<ul>
<li><a href="#weld-data-to-robodk"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Robot_2.svg" width="16" height="16" alt=""> Export To .rdk Project</a></li>
<li><a href="#export-full"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/export_icon.svg" width="16" height="16" alt=""> Export Full</a></li>
<li><a href="#export-selected"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/export_single.svg" width="16" height="16" alt=""> Export Selected</a></li>
<li><a href="#glue-manager"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/glue_icon.svg" width="16" height="16" alt=""> Glue Manager</a></li>
<li><a href="#drilling-manager"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Drill.svg" width="16" height="16" alt=""> Drilling Manager</a></li>
</ul>
</details>


<a id="manufai-workbench"></a>

<h2><img src="./docs/assets/manufai-workbench.svg" width="100%" alt="01 · MANUFAI Workbench"></h2>

<a id="make-weld-trajectories"></a>

### Make Weld Trajectories

<a id="edge-split"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Extract_edges_20.svg" width="44" height="44" alt="Edge Split icon"></td>
<td><h4>Edge Split</h4><p>Geometric Extraction &amp; Intersection</p></td>
</tr>
<tr><td colspan="2">
<p>This tool automatically scans the 3D model (or specific selected parts) to extract all solid edges. It brings them into a global coordinate system and splits the intersecting lines based on a user-defined tolerance threshold.</p>
<ul>
<li><strong>Automated Cleanup:</strong> Generates a clean object with the split edges and automatically hides the original solid bodies to keep the workspace clear.</li>
<li><strong>Assembly Aware:</strong> Respects the global position of parts nested inside complex assemblies or linked objects.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Edge_Splitting"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=BuyjTM-gB38"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=BuyjTM-gB38"><img src="https://img.youtube.com/vi/BuyjTM-gB38/hqdefault.jpg" width="480" alt="Welding FreeCAD add-on - Automatic weldable edges recognition Demo"></a><br><a href="https://www.youtube.com/watch?v=BuyjTM-gB38">Welding FreeCAD add-on - Automatic weldable edges recognition Demo</a></p>
</details>
</td></tr>
</table>

<a id="find-weldable-edges"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Find_Weld_edges_21.svg" width="44" height="44" alt="Find Weldable Edges icon"></td>
<td><h4>Find Weldable Edges</h4><p>Weldable Union Recognition &amp; Filtering</p></td>
</tr>
<tr><td colspan="2">
<p>This tool automatically identifies and extracts edges that are viable candidates for welding. It analyzes the faces and bounding boxes of the 3D model to detect structural joints, filtering out unneeded geometry based on user-defined length and distance thresholds.</p>
<ul>
<li><strong>Smart Detection:</strong> Analyzes complex geometry to distinguish between actual structural joints and regular aesthetic CAD edges.</li>
<li><strong>Length Filtering:</strong> Automatically ignores edges that are shorter than your specified minimum length, preventing the processing of insignificant details.</li>
<li><strong>Automated Output:</strong> Generates a clean "Weldedges" object ready for path generation, hiding the original selection to keep your viewport clear.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Find_Weld_Edges"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=BuyjTM-gB38"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=BuyjTM-gB38"><img src="https://img.youtube.com/vi/BuyjTM-gB38/hqdefault.jpg" width="480" alt="Welding FreeCAD add-on - Automatic weldable edges recognition Demo"></a><br><a href="https://www.youtube.com/watch?v=BuyjTM-gB38">Welding FreeCAD add-on - Automatic weldable edges recognition Demo</a></p>
</details>
</td></tr>
</table>

<a id="weld-creators"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Weld_tree_item.svg" width="44" height="44" alt="Weld Creators icon"></td>
<td><h4>Weld Creators</h4><p>Trajectory Generation</p></td>
</tr>
<tr><td colspan="2">
<p>This core module transforms extracted edges into processable welding trajectories. Beyond just creating paths, it calculates the <strong>Normal Vectors</strong> (torch orientation angles) required for accurate process simulation in both FreeCAD and RoboDK.</p>
<p>Weld creation modes:</p>
<ul>
<li><strong>Make Weld:</strong> Manual mode. You directly select the specific edges where the weld beads should be placed.</li>
<li><strong>Make Weld with All Edges:</strong> Automated mode. Instantly generates welds on all the viable edges detected in the previous filtering step.</li>
<li><strong>Make Weld with Specific Length:</strong> Trims the weld bead by defining offset distances from the start or end (useful for avoiding corners).</li>
<li><strong>Make Weld with Chosen Points:</strong> High precision mode. Graphically define the exact Start and End points of the trajectory.</li>
<li><strong>Make Weld with Multiple Specific Lengths:</strong> Segmented mode. Allows you to create stitch or intermittent welds along a single edge.</li>
<li><strong>By Bead Quantity:</strong> Specify the exact number of weld segments you need, and the system automatically calculates the required gap and length to fit the edge perfectly.</li>
<li><strong>By Bead Length:</strong> Define the exact length of each weld bead, and let the algorithm determine how many segments fit and the correct pitch between them.</li>
<li><strong>By Bead Pitch:</strong> Set the specific center-to-center distance between each weld bead to strictly comply with engineering blueprints.</li>
</ul>
<p><strong>Smart Vector Control:</strong> Automatically calculates bisector angles between faces and allows manual overrides (angle offsets) or individual normal corrections to avoid robot torch collisions.
</p>
<p><a href="./MANUFAI_Workbench/Weld_Trajectory_Generation"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/QdZxZB9vzDA"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://youtu.be/QdZxZB9vzDA"><img src="https://img.youtube.com/vi/QdZxZB9vzDA/hqdefault.jpg" width="480" alt="FreeCAD - Welding plugin - Define Welds Demo"></a><br><a href="https://youtu.be/QdZxZB9vzDA">FreeCAD - Welding plugin - Define Welds Demo</a></p>
</details>
</td></tr>
</table>

<a id="add-normals"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Normals.svg" width="44" height="44" alt="Add Normals icon"></td>
<td><h4>Add Normals</h4><p>Create and define orientation normals along the welding path</p></td>
</tr>
<tr><td colspan="2">
<p>Generates normal vectors along the selected weld trajectory in FreeCAD, allowing the user to define the orientation required for later robotic welding simulation and offline programming in RoboDK.</p>
<ul>
<li><strong>Normal Generation:</strong> Creates normal vectors along the weld path based on the selected geometry.</li>
<li><strong>Tool Orientation:</strong> Defines the approach direction and orientation that the welding torch should follow.</li>
<li><strong>Trajectory Preparation:</strong> Prepares the weld path with the orientation information required for robotic simulation.</li>
<li><strong>RoboDK Integration:</strong> Provides the directional data needed to correctly transfer and simulate the welding trajectory in RoboDK.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Weld_Trajectory_Generation"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/QdZxZB9vzDA"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://youtu.be/QdZxZB9vzDA"><img src="https://img.youtube.com/vi/QdZxZB9vzDA/hqdefault.jpg" width="480" alt="FreeCAD - Welding plugin - Define Welds Demo"></a><br><a href="https://youtu.be/QdZxZB9vzDA">FreeCAD - Welding plugin - Define Welds Demo</a></p>
</details>
</td></tr>
</table>

<a id="surface-weld"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/welding-icon.svg" width="44" height="44" alt="Surface Weld icon"></td>
<td><h4>Surface Weld</h4><p>Volumetric modeling and physical joint representation</p></td>
</tr>
<tr><td colspan="2">
<p>Designed for visual validation and mechanical documentation. Unlike trajectory modules that generate invisible paths for robots, this tool generates the <strong>actual solid geometry</strong> representing Fillet, Butt, and Complex Curve welds. This is essential for collision detection, mass calculation, and rendering.</p>
<ul>
<li><strong>Edge Weld (Auto-Detect):</strong> Automatically detects the geometric type of the edge (Straight, Arc, BSpline, etc.) and generates a solid weld bead between two intersecting faces. It uses an advanced parallel transport algorithm to prevent the 3D shape from twisting along complex curves.</li>
<li><strong>Butt Weld (Angular):</strong> Generates an extruded arc shape to accurately represent V-groove and butt welding joints between two planar faces.</li>
<li><strong>WeldLine Constructor:</strong> A built-in freehand polyline tool to manually draw 3D weld.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Surface_Weld_Generator"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="weld-loader"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/import1.svg" width="44" height="44" alt="Weld Loader icon"></td>
<td><h4>Weld Loader</h4><p>Advanced Welding Data Importer &amp; Interoperability</p></td>
</tr>
<tr><td colspan="2">
<p>A robust synchronization tool designed to bridge external welding design software with FreeCAD. It specializes in parsing industry-standard trajectory files while preserving critical manufacturing parameters.</p>
<ul>
<li><strong>Multi-Format Support:</strong> Native parsing of <code>.WDCurve</code> and <code>.cwsf</code> (CastWorks) files, including global heat source parameters like Voltage (U) and Current (I).</li>
<li><strong>WSO:</strong> Accepts <code>.dkproj</code> files containing the sequence created by WSO.</li>
<li><strong>Smart Geometry Reconstruction:</strong> Automatically cleans duplicate coordinate points, detects closed curves, and reconstructs valid 3D wires for simulation.</li>
<li><strong>Manufacturing Metadata:</strong> Imports and assigns complete process metadata including sequence numbers, layer organization, welding speed, efficiency, and automated lead time calculations.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="positions"></a>

### Positions

<a id="make-positions"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Make_position_groups.svg" width="44" height="44" alt="Make Positions Groups icon"></td>
<td><h4>Make Positions Groups</h4><p>Create and organize workstation position groups.</p></td>
</tr>
<tr><td colspan="2">
<p>
Adds a new Positions Group to the FreeCAD tree, allowing the user to define specific workstations (Positions) 
with their own kinematic constraints, such as linear or rotational axes, positioning speeds, and constant rotation times.
</p>
<ul>
<li>
<strong>Tree Organization:</strong>
Creates a dedicated Positions Group in the FreeCAD project tree.
</li>
<li>
<strong>Workstation Structure:</strong>
Helps organize the different positions used during the welding process.
</li>
<li>
<strong>Process Planning:</strong>
Provides a structured hierarchy for later robot and weld assignments.
</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="assign-welds-to-robots"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/AssignWeldsToRobots.svg" width="44" height="44" alt="Assign Welds To Robots icon"></td>
<td><h4>Assign Welds To Robots</h4><p>Define workstations and assign welds to specific robots</p></td>
</tr>
<tr><td colspan="2">
<p>Allows the user to organize and distribute welds among the robots assigned to each workstation. This helps define which robot is responsible for executing each welding trajectory during the manufacturing process.</p>
<ul>
<li><strong>Robot Assignment:</strong> Assigns individual welds to a specific robot within a Position Group.</li>
<li><strong>Workload Organization:</strong>Helps distribute welding operations between multiple robots in the same workstation.</li>
<li><strong>Process Planning:</strong> Creates a structured relationship between positions, robots, and weld trajectories for later simulation and process execution.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Robot_Assignment"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=TU_ENLACE"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=TU_ENLACE"><img src="https://img.youtube.com/vi/TU_ENLACE/hqdefault.jpg" width="480" alt="Robotic Cell &amp; Assignment Manager - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=TU_ENLACE">Robotic Cell &amp; Assignment Manager - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="subassembly"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/CreateSA.svg" width="44" height="44" alt="SubAssembly icon"></td>
<td><h4>SubAssembly</h4><p>Create and organize manufacturing SubAssemblies.</p></td>
</tr>
<tr><td colspan="2">
<p>
Allows the user to divide complex CAD assemblies into logical
manufacturing SubAssemblies, providing a structured organization
of the components involved in the welding process.
</p>
<ul>
<li>
<strong>Visual Part Grouping:</strong>
Organizes CAD parts into logical manufacturing SubAssemblies.
</li>
<li>
<strong>Tree Organization:</strong>
Creates a clear manufacturing hierarchy inside the FreeCAD tree.
</li>
<li>
<strong>CAD Preservation:</strong>
Organizes the parts without modifying the original CAD constraints.
</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="assign-positions"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/AssigSA.svg" width="44" height="44" alt="Assign Positions icon"></td>
<td><h4>Assign Positions</h4><p>Assign manufacturing positions to SubAssemblies</p></td>
</tr>
<tr><td colspan="2">
<p> Links each manufacturing SubAssembly with the physical welding
workstation or Position where its welding operations will be performed.</p>
<ul>
<li>
<strong>Workstation Mapping:</strong>
Assigns welding Positions to specific SubAssemblies.
</li>
<li>
<strong>Drag &amp; Drop Assignment:</strong>
Provides an intuitive interface for connecting SubAssemblies
with their corresponding manufacturing Positions.
</li>
<li>
<strong>Automatic Data Inheritance:</strong>
Propagates manufacturing information through the hierarchy:
<em>SubAssembly → Position → Robot → Weld</em>.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/SubAssembly_Manager"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=TU_ENLACE"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=TU_ENLACE"><img src="https://img.youtube.com/vi/TU_ENLACE/hqdefault.jpg" width="480" alt="SubAssembly &amp; Position Manager - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=TU_ENLACE">SubAssembly &amp; Position Manager - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="move-subassembly"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveSA.svg" width="44" height="44" alt="Move SubAssembly icon"></td>
<td><h4>Move SubAssembly</h4><p>Move CAD parts between SubAssemblies using drag and drop.</p></td>
</tr>
<tr><td colspan="2">
<p>Allows the user to reorganize the manufacturing structure by dragging
CAD parts from one SubAssembly to another directly within the FreeCAD
tree view.</p>
<ul>
<li>
<strong>Drag &amp; Drop Reorganization:</strong>
Move parts between different SubAssemblies using the tree interface.
</li>
<li>
<strong>SubAssembly Assignment:</strong>
Changes the manufacturing group to which a CAD part belongs.
</li>
<li>
<strong>Hierarchy Organization:</strong>
Keeps the project structure organized after parts are reassigned.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Hierarchy_Organizers"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=TU_ENLACE"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=TU_ENLACE"><img src="https://img.youtube.com/vi/TU_ENLACE/hqdefault.jpg" width="480" alt="Smart Hierarchy Organizers - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=TU_ENLACE">Smart Hierarchy Organizers - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="move-welds"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveWelds.svg" width="44" height="44" alt="Move Welds icon"></td>
<td><h4>Move Welds</h4><p>Reassign weld trajectories between robots using drag and drop.</p></td>
</tr>
<tr><td colspan="2">
<p>
Allows the user to move weld trajectories from one robot to another
directly within the manufacturing hierarchy, simplifying robot assignment
and welding sequence organization.
</p>
<ul>
<li>
<strong>Drag &amp; Drop Reassignment:</strong>
Move welds between robots using an intuitive tree-based interface.
</li>
<li>
<strong>Robot Assignment:</strong>
Quickly change which robot is responsible for executing a specific weld.
</li>
<li>
<strong>Hierarchy Update:</strong>
Updates the weld position inside the manufacturing structure after reassignment.
</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="length"></a>

### Length

<a id="weld-length-report"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report1.svg" width="44" height="44" alt="Weld Length Report icon"></td>
<td><h4>Weld Length Report</h4><p>Production Reports &amp; Quotations</p></td>
</tr>
<tr><td colspan="2">
<p>Automatically extracts the total linear distance of all weld beads within the active document. This tool is essential for estimating filler metal consumption, wire usage, and overall project costs.</p>
<ul>
<li><strong>Smart Grouping:</strong> Organizes the exported data hierarchically by SubAssembly, Position, and specific Robot.</li>
<li><strong>Unit Conversion:</strong> Allows on-the-fly conversion between metric and imperial units (mm, cm, m, in, ft, etc.).</li> 
<li><strong>Direct Excel Export:</strong> Generates a clean, formatted <code>.xlsx</code> workbook ready for your purchasing and planning departments.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Reports"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=hXmbLb0A_RI"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=hXmbLb0A_RI"><img src="https://img.youtube.com/vi/hXmbLb0A_RI/hqdefault.jpg" width="480" alt="FreeCAD - Plugin - Total welding distance Demo"></a><br><a href="https://www.youtube.com/watch?v=hXmbLb0A_RI">FreeCAD - Plugin - Total welding distance Demo</a></p>
</details>
</td></tr>
</table>

<a id="cycle-time-tools"></a>

### Cycle Time

<a id="process"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Process_V2.svg" width="44" height="44" alt="Process icon"></td>
<td><h4>Process</h4><p>Define the welding process parameters.</p></td>
</tr>
<tr><td colspan="2">
<p>
Allows the user to define the main process parameters required
for the welding operation and subsequent cycle-time calculation.
</p>
<ul>
<li><strong>Resource Configuration:</strong> Assigns process data to a positioner, robot, or human operator.</li>
<li><strong>Execution Parameters:</strong>Defines the information required for how the selected resource participates in the welding operation.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="assign-process"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign%20process.svg" width="44" height="44" alt="Assign Process icon"></td>
<td><h4>Assign Process</h4><p>Assign process information to welding trajectories.</p></td>
</tr>
<tr><td colspan="2">
<p>
Links the previously defined process parameters to the
corresponding weld lines before the welding sequence is analyzed.
</p>
<ul>
<li><strong>Process Data Linking:</strong> Connects previously created process parameters with the selected welding trajectories.</li>
<li><strong>Project Data:</strong> Ensures that each weld contains the necessary process information for later cycle-time calculations, simulation, or report generation.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="welding-parameters"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Welding_parameters.svg" width="44" height="44" alt="Welding Parameters icon"></td>
<td><h4>Welding Parameters</h4><p>Define the heat source used by the welding process.</p></td>
</tr>
<tr><td colspan="2">
<p>
Creates the heat-source information required to characterize
the thermal input associated with each welding operation.
</p>
<ul>
<li><strong>Parameter Configuration:</strong> Defines the welding parameters associated with the operation.</li>
<li><strong>Welding Speed Setup:</strong> Sets the travel speed used during the welding process.</li>
<li><strong>Process Preparation:</strong> Prepares the necessary welding data for later assignment to weld trajectories.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="assign-welding-parameters"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign%20weld%20parameters_v3.svg" width="44" height="44" alt="Assign Welding Parameters icon"></td>
<td><h4>Assign Welding Parameters</h4><p>Assign heat-source data to individual weld lines.</p></td>
</tr>
<tr><td colspan="2">
<p>
Associates the appropriate heat-source configuration with each
welding trajectory so that the project contains all required
process information.
</p>
<ul>
<li><strong>Parameter Assignment:</strong> Applies the selected welding parameters to one or more weld trajectories.</li>
<li><strong>Weld Data Validation:</strong> Ensures that the welds contain the required information for later cycle-time calculations, simulation, and report generation.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="cycle-time"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report3_cycle_time.svg" width="44" height="44" alt="Cycle Time icon"></td>
<td><h4>Cycle Time</h4><p>Sequence Verification &amp; Process Timing</p></td>
</tr>
<tr><td colspan="2">
<p>Calculates the total execution time for the welding process, whether performed by a human operator or an automated robot, based on actual trajectory length and assigned travel speeds.</p>
<ul>
<li><strong>Parameter Validation:</strong> Strictly verifies that every weld line has proper Heat Source and Process parameters assigned before allowing the export.</li>
<li><strong>Drag &amp; Drop Sequencer:</strong> Includes an interactive table interface to visually reorder and organize the welding sequence prior to generating the report.</li>
<li><strong>Detailed Analytics:</strong> Exports a hierarchical Excel report breaking down the time spent per subassembly, position, and robotic cell.</li>
</ul>
<p><a href="./MANUFAI_Workbench/Find_Weld_Edges"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Giv5xZ7Uw44"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=Giv5xZ7Uw44"><img src="https://img.youtube.com/vi/Giv5xZ7Uw44/hqdefault.jpg" width="480" alt="FreeCAD Plugin - Cycle time report - Robot or Manual welding Demo"></a><br><a href="https://www.youtube.com/watch?v=Giv5xZ7Uw44">FreeCAD Plugin - Cycle time report - Robot or Manual welding Demo</a></p>
</details>
</td></tr>
</table>

<a id="weight"></a>

### Weight

<a id="create-materials"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Create%20Material.svg" width="44" height="44" alt="Create Materials icon"></td>
<td><h4>Create Materials</h4><p>Create custom materials for weight calculations.</p></td>
</tr>
<tr><td colspan="2">
<p>
Allows the user to create and define materials by specifying
the properties required for subsequent weight calculations.
</p>
<ul>
<li>
<strong>Material Definition:</strong>Creates new materials with their corresponding density.
</li>
<li>
<strong>Custom Database:</strong>Allows project-specific materials to be added for later use.
</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="assign-materials"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Assign_material_v4.svg" width="44" height="44" alt="Assign Materials icon"></td>
<td><h4>Assign Materials</h4><p>Assign materials to CAD components.</p></td>
</tr>
<tr><td colspan="2">
<p>
Allows the user to assign a previously defined material
to each component of the CAD assembly.
</p>
<ul>
<li>
<strong>Component Assignment:</strong> Links each CAD part with its corresponding material.
</li>
<li>
<strong>Density Information:</strong>Provides the material density required for weight calculations.
</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Weld_Loader_Pro"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk"><img src="https://img.youtube.com/vi/5uwMWgmB7Lk/hqdefault.jpg" width="480" alt="Surface Weld Generator - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=5uwMWgmB7Lk">Surface Weld Generator - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="weight-of-welding-and-welded-part"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Report2.svg" width="44" height="44" alt="Weight of Welding and Welded Part icon"></td>
<td><h4>Weight of Welding and Welded Part</h4><p>Calculate the weight of weld metal and the complete welded assembly</p></td>
</tr>
<tr><td colspan="2">
<p> Calculates the mass of the deposited weld metal and the total weight
of the welded part based on the geometry and assigned material densities.</p>
<ul>
<li>
<strong>Weld Metal Weight:</strong>
Estimates the mass contributed by the deposited welding material.
</li>
<li>
<strong>Welded Part Weight:</strong>
Calculates the total mass of the final welded assembly.
</li>
<li>
<strong>Material-Based Calculation:</strong>
Uses the assigned material densities to determine the corresponding weight.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Weight_Report"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="wso"></a>

### Welding Sequence AI Advisor

<a id="export-stl"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/stl-file-format-icon.svg" width="44" height="44" alt="Export STL icon"></td>
<td><h4>Export STL</h4><p>Export selected objects or the complete part to STL format.</p></td>
</tr>
<tr><td colspan="2">
<p> Converts selected CAD objects or the complete model into an
<code>.stl</code> file for use in other applications.</p>
<ul>
<li>
<strong>Selected Object Export:</strong>
Allows specific CAD objects to be exported individually.
</li>
<li>
<strong>Complete Part Export:</strong>
Exports the entire part when a full model transfer is required.
</li>
<li>
<strong>STL Geometry:</strong>
Converts the external geometry into a triangulated surface representation.
</li>
<li>
<strong>Software Compatibility:</strong>
Facilitates geometry transfer for visualization, meshing,
simulation, or other STL-compatible workflows.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Weight_Report"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="export-as-dk-project"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Export_DKproj_v4.svg" width="44" height="44" alt="Export As DK Project icon"></td>
<td><h4>Export As DK Project</h4><p>Create a new DK project file from the current project.</p></td>
</tr>
<tr><td colspan="2">
<p> Generates a new <code>.dkproject</code> file containing the project
information required for the corresponding DK workflow.</p>
<ul>
<li>
<strong>Project File Generation:</strong>
Creates a new <code>.dkproject</code> file.
</li>
<li>
<strong>Project Transfer:</strong>
Packages the required project information into the DK project format.
</li>
<li>
<strong>Workflow Preparation:</strong>
Provides the project file required for subsequent DK processing.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Sequence_AI_Advisor"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/48nRLUuxqVA"><strong>Watch demo 1</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/bhIbrSHBmeU"><strong>Watch demo 2</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://youtu.be/48nRLUuxqVA"><img src="https://img.youtube.com/vi/48nRLUuxqVA/hqdefault.jpg" width="480" alt="WSO with DK Algorithm Demo"></a><br><a href="https://youtu.be/48nRLUuxqVA">WSO with DK Algorithm Demo</a></p>
<p><a href="https://youtu.be/bhIbrSHBmeU"><img src="https://img.youtube.com/vi/bhIbrSHBmeU/hqdefault.jpg" width="480" alt="Sequence Visualizer [Output] Demo"></a><br><a href="https://youtu.be/bhIbrSHBmeU">Sequence Visualizer [Output] Demo</a></p>
</details>
</td></tr>
</table>

<a id="simulation"></a>

### Sequence and Process Visualization

<a id="assign-sequence"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Define%20Sequence.svg" width="44" height="44" alt="Assign Sequence icon"></td>
<td><h4>Assign Sequence</h4><p>Define the execution order of the welding process.</p></td>
</tr>
<tr><td colspan="2">
<p>Allows the user to organize workstations, robots, and weld trajectories
into a logical execution sequence before running the welding simulation.</p>
<ul>
<li>
<strong>Execution Order:</strong>
Defines the order in which the welding operations will be performed.
</li>
<li>
<strong>Process Organization:</strong>
Structures Positions, Robots, and Welds according to the manufacturing plan.
</li>
<li>
<strong>Simulation Preparation:</strong>
Creates the sequence required before the robotic welding simulation is executed.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Weight_Report"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="weld-simulation"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Run_simulation3.svg" width="44" height="44" alt="Weld Simulation icon"></td>
<td><h4>Weld Simulation</h4><p>Validate torch accessibility, motion, and welding trajectories.</p></td>
</tr>
<tr><td colspan="2">
<p>Simulates the welding gun along the previously defined weld sequence,
allowing the user to visually verify torch motion and identify potential
accessibility or collision issues.</p>
<ul>
<li>
<strong>Trajectory Visualization:</strong>
Displays the welding gun moving along the defined weld paths.
</li>
<li>
<strong>Accessibility Verification:</strong>
Helps identify areas that may be difficult for the welding torch to reach.
</li>
<li>
<strong>Collision Review:</strong>
Provides a visual method for evaluating possible interference during motion.
</li>
<li>
<strong>Process Demonstration:</strong>
Can be used for technical reviews, presentations, and manufacturing planning.
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Welding_Gun_Simulation"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=kuIgRGPw8nU"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=kuIgRGPw8nU"><img src="https://img.youtube.com/vi/kuIgRGPw8nU/hqdefault.jpg" width="480" alt="FreeCAD Plugin - Simulate welding gun on a trajectory Demo"></a><br><a href="https://www.youtube.com/watch?v=kuIgRGPw8nU">FreeCAD Plugin - Simulate welding gun on a trajectory Demo</a></p>
</details>
</td></tr>
</table>

<a id="weld-visualizer"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/weld_sphere.svg" width="44" height="44" alt="Show Weld Sphere icon"></td>
<td><h4>Show Weld Sphere</h4><p>Lightweight 3D visual verification and playback sequence control.</p></td>
</tr>
<tr><td colspan="2">
<p>Designed for rapid visual verification of welds without the computational overhead of generating complex geometric solids.</p>
<p>It utilizes direct scene graph rendering to project a customizable "cloud" of spheres along the trajectory, providing an immediate visual representation of weld coverage while maintaining a lightweight model size and fluid viewport navigation. It includes an integrated sequence table and playback controls to inspect your production flow row by row.</p>
<p><a href="./MANUFAI_Workbench/Weld_Visualizer"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Ccb7qmT_r68"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=Ccb7qmT_r68"><img src="https://img.youtube.com/vi/Ccb7qmT_r68/hqdefault.jpg" width="480" alt="Weld Visualizer (Sphere Mode) - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=Ccb7qmT_r68">Weld Visualizer (Sphere Mode) - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="visualizer-cmd"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/show.svg" width="44" height="44" alt="Visualizer icon"></td>
<td><h4>Visualizer</h4><p>Interactive 3D visibility control and rapid weld inspection.</p></td>
</tr>
<tr><td colspan="2">
<p>Designed to easily isolate and audit complex multi-robot manufacturing cells.</p>
<p>It provides a structured tree-based interface to selectively toggle the visibility of SubAssemblies, Workstation Positions, and individual Robots. Combined with an integrated lightweight sphere rendering mode, it allows engineers to inspect weld coverage and cell accessibility instantly without performance lag.</p>
<p><a href="./MANUFAI_Workbench/Assembly_Visualizer"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=TU_ENLACE"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=TU_ENLACE"><img src="https://img.youtube.com/vi/TU_ENLACE/hqdefault.jpg" width="480" alt="Assembly Visualizer - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=TU_ENLACE">Assembly Visualizer - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<p align="right"><a href="#toolbar-layout">Tool index ↑</a> &nbsp;·&nbsp; <a href="#top">Back to top ↑</a></p>

<a id="datum-alignment-tools"></a>

<h2><img src="./docs/assets/datum-alignment-tools.svg" width="100%" alt="02 · 3-2-1 Datum Based Alignment &amp; Tools"></h2>

<a id="toggle-visibility-recursive"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Toggle_Visibility_Recursive.svg" width="44" height="44" alt="Toggle Visibility Recursive icon"></td>
<td><h4>Toggle Visibility Recursive</h4><p>Instantly restore visual control over complex assemblies.</p></td>
</tr>
<tr><td colspan="2">
<p>The <strong>Recursive Visibility</strong> tool solves UX friction when working with complex hierarchies. It traverses the entire dependency tree of a selected object to toggle visibility for the parent and all descendants recursively.</p>
<p><a href="./Datum_321_Alignment/Recursive_Visibility"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=360sB3FVUp4"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=360sB3FVUp4"><img src="https://img.youtube.com/vi/360sB3FVUp4/hqdefault.jpg" width="480" alt="Recursive Visibility Toggle for Complex Assemblies - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=360sB3FVUp4">Recursive Visibility Toggle for Complex Assemblies - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="create-center-point"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/CENTRO.svg" width="44" height="44" alt="Create Center Point icon"></td>
<td><h4>Create Center Point</h4><p>Calculates geometric centers for quick referencing.</p></td>
</tr>
<tr><td colspan="2">
<p>It computes and marks the center point based on the current selection.</p>
<ul>
<li><strong>Single Object:</strong> Marks the center of mass/geometry.</li>
<li><strong>Two Objects:</strong> Calculates the exact midpoint between them.</li>
</ul>
<p>Useful for establishing auxiliary reference points on complex geometry without creating full datums.</p>
<p><a href="./Datum_321_Alignment/Center_Point"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=AsVGiXEPmd4"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=AsVGiXEPmd4"><img src="https://img.youtube.com/vi/AsVGiXEPmd4/hqdefault.jpg" width="480" alt="Center Point - MANUFAI FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=AsVGiXEPmd4">Center Point - MANUFAI FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="create-sphere-at-origin"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/ORIGEN.svg" width="44" height="44" alt="Create Sphere at Origin icon"></td>
<td><h4>Create Sphere at Origin</h4><p>Generates a visual reference at the Global Origin (0,0,0).</p></td>
</tr>
<tr><td colspan="2">
<p>It places a reference sphere at the absolute zero of the workspace. This provides an immediate visual check to determine the offset distance of imported models relative to the workspace center before starting any alignment procedures.</p>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="datum-a"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_A.svg" width="44" height="44" alt="Datum A icon"></td>
<td><h4>Datum A</h4><p>Define the primary reference for the alignment system.</p></td>
</tr>
<tr><td colspan="2">
<p>
Establishes the main reference plane or axis used to begin the
3-2-1 alignment process.
</p>
<ul>
<li>
<strong>Primary Constraint:</strong>
Locks 3 degrees of freedom.
</li>
<li>
<strong>Reference Selection:</strong>
Can use flat face normals, hole centerlines, or edge pairs.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="datum-b"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_B.svg" width="44" height="44" alt="Datum B icon"></td>
<td><h4>Datum B</h4><p>Define the secondary direction of the coordinate system.</p></td>
</tr>
<tr><td colspan="2">
<p>
Establishes the directional reference used after Datum A to further
constrain and orient the model.
</p>
<ul>
<li>
<strong>Secondary Constraint:</strong>
Locks 2 additional degrees of freedom.
</li>
<li>
<strong>Directional Definition:</strong>
Can use edges, faces, or calculated theoretical midplanes.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="datum-c"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATUM_C.svg" width="44" height="44" alt="Datum C icon"></td>
<td><h4>Datum C</h4><p>Define the final reference required for positioning.</p></td>
</tr>
<tr><td colspan="2">
<p>
Establishes the final reference point of the 3-2-1 system and
completes the constraint of the model.
</p>
<ul>
<li>
<strong>Final Constraint:</strong>
Locks the last remaining degree of freedom.
</li>
<li>
<strong>Zero Point Definition:</strong>
Can use vertices, sphere centers, or edge midpoints.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="3-2-1-alignment"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/ALINEACION.svg" width="44" height="44" alt="3-2-1 Datum-Based Alignment icon"></td>
<td><h4>3-2-1 Datum-Based Alignment</h4><p>This suite provides a step-by-step workflow to establish a definitive coordinate system (CSYS) using standard 3-2-1 alignment logic. It guides you from reference identification to assembly-safe model repositioning</p></td>
</tr>
<tr><td colspan="2">
<p>
Uses Datum A, Datum B, and Datum C to establish a definitive
coordinate system based on standard 3-2-1 alignment principles.
</p>
<ul>
<li>
<strong>Reference Combination:</strong>
Combines the three selected datum references.
</li>
<li>
<strong>Coordinate System Definition:</strong>
Determines the orientation and origin required to correctly
reposition the model.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="move-model-to-origin"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MOVER.svg" width="44" height="44" alt="Move Model To Origin icon"></td>
<td><h4>Move Model To Origin</h4><p>Reposition the model using the calculated 3-2-1 alignment.</p></td>
</tr>
<tr><td colspan="2">
<p>
Applies the calculated transformation to move the model into the
established coordinate system while preserving the internal CAD
assembly structure.
</p>
<ul>
<li>
<strong>Model Repositioning:</strong>
Moves the aligned model toward the defined global reference.
</li>
<li>
<strong>Assembly-Safe Transformation:</strong>
Preserves document hierarchies and internal assembly relationships.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=hPKx3S9DQLc"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=hPKx3S9DQLc"><img src="https://img.youtube.com/vi/hPKx3S9DQLc/hqdefault.jpg" width="480" alt="3-2-1 Datum Based Alignment - MANUFAI FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=hPKx3S9DQLc">3-2-1 Datum Based Alignment - MANUFAI FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="reset-pos"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Part_Box.svg" width="44" height="44" alt="Reset Position icon"></td>
<td><h4>Reset Position</h4><p>Toggle transformation reset and coordinate zeroing</p></td>
</tr>
<tr><td colspan="2">
<p>A professional utility command designed to quickly clear or restore the transformation matrix (Placement) of selected CAD objects with native "Undo" support.</p>
<ul>
<li><strong>Smart Toggle Logic:</strong>
<ul>
<li>If the object is currently placed away from the workspace, clicking the button saves its current position to a hidden property and instantly resets its placement to the absolute origin <code>(0,0,0)</code>.</li>
<li>If the object is already at the origin, clicking it again automatically restores its previous saved position.</li>
</ul>
</li>
</ul>
<p><a href="./MANUFAI_Workbench/Reset_Position"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=TU_ENLACE"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=TU_ENLACE"><img src="https://img.youtube.com/vi/TU_ENLACE/hqdefault.jpg" width="480" alt="Reset Position - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=TU_ENLACE">Reset Position - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="show-welding-widget-command"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/welding-image-tool.svg" width="44" height="44" alt="Show Welding Widget icon"></td>
<td><h4>Show Welding Widget</h4><p>2D Blueprint to 3D Model Synchronization.</p></td>
</tr>
<tr><td colspan="2">
<p>The <strong>Welding Reference Tool</strong> allows engineers to work with blueprints, technical images, or diagrams directly within the 3D environment, eliminating the need to keep a PDF open on a second monitor.</p>
<p>It enables the import of 2D documentation to place digital markers and logically link them with real 3D objects in the document.</p>
<p>Key Capabilities:</p>
<ul>
<li><strong>Interactive Mapping:</strong> Load any image (PNG, JPG) and place "weld points" simply by clicking on the drawing.</li>
<li><strong>Digital Linkage:</strong> Associate each 2D mark with an existing weld bead in the 3D model for full traceability.</li>
</ul>
<p><a href="./Datum_321_Alignment/Welding_Reference"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Yp307CxQaUM"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=Yp307CxQaUM"><img src="https://img.youtube.com/vi/Yp307CxQaUM/hqdefault.jpg" width="480" alt="Welding Reference Tool - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=Yp307CxQaUM">Welding Reference Tool - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="launch-find-data-panel"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DATA_ICON.svg" width="44" height="44" alt="Launch Find Data Panel icon"></td>
<td><h4>Launch Find Data Panel</h4><p>Centralized control for weld tracking and interoperability.</p></td>
</tr>
<tr><td colspan="2">
<p>This tool opens a dedicated side panel that automatically scans the active document to identify and list all generated <strong>Weld Objects</strong>. It serves as the bridge between FreeCAD and external collaborators.</p>
<p>Key Features:</p>
<ul>
<li><strong>Instant Detection:</strong> Click to locate and highlight specific weld beads in the 3D view immediately.</li>
<li><strong>Flexible Data Export:</strong> Generates a <code>.txt</code> report of the selected welds. It offers two modes:
</li><li><strong>Simple Report:</strong> Exports essential identification, coordinates, and basic geometry data.</li>
<li><strong>Detailed Dump:</strong> Exports <strong>every single internal property</strong>. Ideal for deep debugging or external solvers needing raw parametric data.</li>
</ul>
<p><a href="./Datum_321_Alignment/Find_Data_Panel"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=AJxwoL3yqto"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=AJxwoL3yqto"><img src="https://img.youtube.com/vi/AJxwoL3yqto/hqdefault.jpg" width="480" alt="How to see all the weld data? - MANUFAI FreeCAD plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=AJxwoL3yqto">How to see all the weld data? - MANUFAI FreeCAD plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="focus-object-command"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/focus_icon.svg" width="44" height="44" alt="Focus Object icon"></td>
<td><h4>Focus Object</h4><p>Instant Navigation.</p></td>
</tr>
<tr><td colspan="2">
<p>A productivity shortcut that instantly zooms and centers the camera on the object currently selected in the tree or list. Essential for locating small weld segments in large-scale environments.</p>
<p><a href="./Datum_321_Alignment/Focus_on_Object"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=vnDtbglly2k"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=vnDtbglly2k"><img src="https://img.youtube.com/vi/vnDtbglly2k/hqdefault.jpg" width="480" alt="Focus on Object - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=vnDtbglly2k">Focus on Object - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="move-weld-lines"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/MoveWeldlines.svg" width="44" height="44" alt="Move Weld Lines icon"></td>
<td><h4>Move Weld Lines</h4><p>Precision Trajectory Re-positioning.</p></td>
</tr>
<tr><td colspan="2">
<p>A multi-modal suite designed to reposition welding paths without losing their internal manufacturing data. It provides three specialized workflows to handle any alignment scenario:</p>
<ul>
<li><strong>Smart Projection:</strong> Aligns the entire weld line to a target edge by calculating the shortest distance to the path's center, ensuring perfect surface contact while preserving the original shape.</li>
<li><strong>Circular Alignment:</strong> Specialized for pipes and bosses. It detects circular/arc edges and snaps one or multiple weld lines to them using the first point as a precise anchor.</li>
<li><strong>Manual Transformer:</strong> A real-time editing panel for fine-tuning. Rotate and translate paths using precision spinboxes (<code>X, Y, Z, Rx, Ry, Rz</code>) with automatic recalculation of lead times and distances.</li>
</ul>
<p><a href="./Datum_321_Alignment/Smart_Discretize"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="discretize"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/DIZCRE.svg" width="44" height="44" alt="Discretize icon"></td>
<td><h4>Discretize</h4><p>Geometry-Aware Path Projection.</p></td>
</tr>
<tr><td colspan="2">
<p>A high-precision tool that refines welding trajectories by projecting existing data onto target CAD edges. It eliminates the "floating path" issue by snapping the simulation points directly to the physical geometry.</p>
<ul>
<li><strong>Adaptive Point Density:</strong> Unlike standard discretization, this tool distinguishes between geometries:
<ul>
<li><i>Curved Edges:</i> Applies the user-defined <b>Curve Density</b> for smooth robotic motion.</li>
<li><i>Straight Edges:</i> Automatically optimizes to just <b>2 points</b> (Start/End), reducing redundant controller data and OLP complexity.</li>
</ul>
</li>
<li><strong>Multi-Edge Selection:</strong> Capable of projecting a single weld trajectory across multiple disparate edges (Compound support).</li>
<li><strong>Real-Time Optimization:</strong> Includes a "Corner Detection" logic that preserves points only where direction changes significantly ($cos(	heta) &lt; 0.9999$).</li>
<li><strong>Automatic Sync:</strong> Updates all internal MANUFAI metrics (Distance, Pts, and LeadTime) immediately after projection.</li>
</ul>
<p><a href="./Datum_321_Alignment/Smart_Discretize"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<p align="right"><a href="#toolbar-layout">Tool index ↑</a> &nbsp;·&nbsp; <a href="#top">Back to top ↑</a></p>

<a id="c3p-wdcurve-tools"></a>

<h2><img src="./docs/assets/c3p-wdcurve-tools.svg" width="100%" alt="03 · C3P – WdCurve Tools"></h2>

<a id="line-weld-table"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/table_icon.svg" width="44" height="44" alt="Line Weld Table icon"></td>
<td><h4>Line Weld Table</h4><p>Parameter Editor &amp; WDCurve Exporter</p></td>
</tr>
<tr><td colspan="2">
<p>Provides a comprehensive tabular interface to audit and refine technical data for all weld lines within the document. This is the <strong>final stage</strong> of the workflow.</p>
<ul>
<li><strong>Bulk Editing:</strong> Batch modify Voltage (U), Current (I), Speed (V), and Sequence parameters.</li>
<li><strong>Sequence Management:</strong> Reorder the welding sequence via drag-and-drop.</li>
<li><strong>Parallel Operations:</strong> Define simultaneous tasks for multi-robot synchronization.</li>
<li><strong>Final Export:</strong> Generates the <code>.WDCurve</code> file, exporting only active layers for external processing.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Line_Weld_Table"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=wSOsoFvLScI"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=wSOsoFvLScI"><img src="https://img.youtube.com/vi/wSOsoFvLScI/hqdefault.jpg" width="480" alt="Line Weld Table &amp; WDCurve Export - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=wSOsoFvLScI">Line Weld Table &amp; WDCurve Export - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="show-names"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/names_icon.svg" width="44" height="44" alt="Show Names icon"></td>
<td><h4>Show Names</h4><p>Orientation &amp; ID HUD.</p></td>
</tr>
<tr><td colspan="2">
<p>Toggles a "Head-Up Display" in the 3D view for all weld lines.</p>
<ul>
<li><strong>ID Labels:</strong> Shows the name/number of the weld floating above it.</li>
<li><strong>Direction Markers:</strong> Clearly marks the <strong>Start (O)</strong> and <strong>End (X)</strong> of the path to verify torch direction visually.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Show_Names"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=uVRiyf8H4nk"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=uVRiyf8H4nk"><img src="https://img.youtube.com/vi/uVRiyf8H4nk/hqdefault.jpg" width="480" alt="Weld Path Name &amp; Direction Display - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=uVRiyf8H4nk">Weld Path Name &amp; Direction Display - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="selection-mode"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/selection_mode.svg" width="44" height="44" alt="Selection Mode (X-Ray &amp; Filter) icon"></td>
<td><h4>Selection Mode (X-Ray &amp; Filter)</h4><p>Visual isolation and Selection Lock.</p></td>
</tr>
<tr><td colspan="2">
<p>A specialized view mode designed for working in complex assemblies.</p>
<ul>
<li><strong>X-Ray Vision:</strong> Makes the 3D geometry transparent while keeping weld lines solid and visible.</li>
<li><strong>Click-Through Blocker:</strong> <strong>Selection Filter.</strong> Strictly blocks the selection of 3D geometry (faces/bodies), ensuring that clicks <strong>only register on weld lines</strong>. This prevents accidental selection of the background model.</li>
</ul>
<p><a href="./C3P_WdCurve_Tools/Selection_Mode"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Y3D3PVF0ubI"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=Y3D3PVF0ubI"><img src="https://img.youtube.com/vi/Y3D3PVF0ubI/hqdefault.jpg" width="480" alt="X-Ray Weld Selection Mode - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=Y3D3PVF0ubI">X-Ray Weld Selection Mode - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<p align="right"><a href="#toolbar-layout">Tool index ↑</a> &nbsp;·&nbsp; <a href="#top">Back to top ↑</a></p>

<a id="robodk-process-automation"></a>

<h2><img src="./docs/assets/robodk-process-automation.svg" width="100%" alt="04 · RoboDK &amp; Process Automation"></h2>

<a id="weld-data-to-robodk"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Robot_2.svg" width="44" height="44" alt="Export To .rdk Project icon"></td>
<td><h4>Export To .rdk Project</h4><p>Automated Welding Path &amp; Program Generation.</p></td>
</tr>
<tr><td colspan="2">
<p>A powerful FreeCAD add-on designed specifically for <strong>Robotic Welding</strong> applications. It eliminates manual coordinate entry by synchronizing design geometry with robot logic:</p>
<ul>
<li><strong>Path Modeling:</strong> Design complex welding trajectories directly within the FreeCAD environment.</li>
<li><strong>Automatic Program Creation:</strong> The plugin extracts path data and generates ready-to-use robot programs in RoboDK instantly.</li>
<li><strong>Data Synchronization:</strong> Ensures that every vertex and edge of the weld seam is accurately translated into robot targets.</li>
</ul>
<p><a href="./RoboDK_Process_Automation/Weld_Data_to_RoboDK"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/bNV_s38_P9E"><strong>Watch demo 1</strong></a> &nbsp;·&nbsp; <a href="https://youtu.be/PpmaKM3XEzY"><strong>Watch demo 2</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=_DmwPQABFhU"><strong>Watch demo 3</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://youtu.be/bNV_s38_P9E"><img src="https://img.youtube.com/vi/bNV_s38_P9E/hqdefault.jpg" width="480" alt="FreeCAD Plugin - Robotic Cell Modeling for automatic transfer of weld data"></a><br><a href="https://youtu.be/bNV_s38_P9E">FreeCAD Plugin - Robotic Cell Modeling for automatic transfer of weld data</a></p>
<p><a href="https://youtu.be/PpmaKM3XEzY"><img src="https://img.youtube.com/vi/PpmaKM3XEzY/hqdefault.jpg" width="480" alt="FreeCAD to RoboDK welding Modeling and Simulation"></a><br><a href="https://youtu.be/PpmaKM3XEzY">FreeCAD to RoboDK welding Modeling and Simulation</a></p>
<p><a href="https://www.youtube.com/watch?v=_DmwPQABFhU"><img src="https://img.youtube.com/vi/_DmwPQABFhU/hqdefault.jpg" width="480" alt="Weld Path to Robot Program - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=_DmwPQABFhU">Weld Path to Robot Program - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="export-full"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/export_icon.svg" width="44" height="44" alt="Export Full icon"></td>
<td><h4>Export Full</h4><p>Transfer the complete visible CAD assembly to RoboDK</p></td>
</tr>
<tr><td colspan="2">
<p>
Exports the entire visible FreeCAD assembly directly to RoboDK,
allowing the complete model to be transferred to the robotic
simulation environment in a single operation.
</p>
<ul>
<li>
<strong>Complete Assembly Export:</strong>
Transfers all visible components of the current CAD assembly.
</li>
<li>
<strong>RoboDK Integration:</strong>
Sends the geometry directly to the RoboDK simulation environment.
</li>
<li>
<strong>Coordinate Alignment:</strong>
Uses the CAD reference coordinate system to maintain proper
alignment between the FreeCAD model and the RoboDK station.
</li>
</ul>
<p><a href="./Datum_321_Alignment/Create_Sphere_Origin"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8"><img src="https://img.youtube.com/vi/HbsH8DEtrP8/hqdefault.jpg" width="480" alt="FreeCAD plugin welded part weight report Demo"></a><br><a href="https://www.youtube.com/watch?v=HbsH8DEtrP8">FreeCAD plugin welded part weight report Demo</a></p>
</details>
</td></tr>
</table>

<a id="export-selected"></a>
<a id="export-selected-parts"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/export_single.svg" width="44" height="44" alt="Export Selected icon"></td>
<td><h4>Export Selected</h4><p>Transfer only selected CAD components to RoboDK.</p></td>
</tr>
<tr><td colspan="2">
<p> Exports only the parts selected by the user in FreeCAD,
allowing specific components to be transferred to RoboDK
without exporting the complete assembly.</p>
<ul>
<li>
<strong>Selective Export:</strong>
Transfers only the components selected in the FreeCAD model.
</li>
<li>
<strong>Partial Updates:</strong>
Useful when only specific parts need to be added or updated
in the RoboDK station.
</li>
<li>
<strong>Isolated Testing:</strong>
Allows individual components or groups of parts to be evaluated
without transferring the complete assembly.
</li>
</ul>
<p><a href="./RoboDK_Process_Automation/RoboDK_Export_Tools"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=RDRtrwVmNSQ"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=RDRtrwVmNSQ"><img src="https://img.youtube.com/vi/RDRtrwVmNSQ/hqdefault.jpg" width="480" alt="CAD to Robot Export - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=RDRtrwVmNSQ">CAD to Robot Export - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="glue-manager"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/glue_icon.svg" width="44" height="44" alt="Glue Manager icon"></td>
<td><h4>Glue Manager</h4><p>Weld-to-Dispensing Path Conversion.</p></td>
</tr>
<tr><td colspan="2">
<p>This tool repurposes existing MANUFAI weld paths (<code>Pts</code> data) to create precise adhesive dispensing trajectories.</p>
<ul>
<li><strong>Non-Destructive Transformation:</strong> Includes a dedicated panel to Scale, Translate, and Rotate the path locally without altering the original CAD geometry.</li>
<li><strong>Smart Export:</strong> Automatically calculates surface normals for correct gun orientation and exports the transformed data to RoboDK as a "Curve Follow Project".</li>
</ul>
<p><a href="./RoboDK_Process_Automation/Glue_Manager"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=iWT9zPO1s58"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=iWT9zPO1s58"><img src="https://img.youtube.com/vi/iWT9zPO1s58/hqdefault.jpg" width="480" alt="Dispensing operations with RoboDK - MANUFAI FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=iWT9zPO1s58">Dispensing operations with RoboDK - MANUFAI FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<a id="drilling-manager"></a>
<table>
<tr>
<td width="66" align="center" valign="middle"><img src="https://raw.githubusercontent.com/jr23mx/MANUFAI_freecad_plugin/main/Resources/Drill.svg" width="44" height="44" alt="Drilling Manager icon"></td>
<td><h4>Drilling Manager</h4><p>Automated Hole &amp; Rivet Processing.</p></td>
</tr>
<tr><td colspan="2">
<p>A complete suite for automating drilling or riveting operations. It detects circular edges on the 3D model to extract centers and normal vectors automatically.</p>
<ul>
<li><strong>Operation Modes:</strong>
<ul>
<li><strong>Manual:</strong> Step-by-step definition (Start/End points) for visual depth control.</li>
<li><strong>Precision:</strong> Apply specific numeric depth values to single holes.</li>
<li><strong>Batch Processing:</strong> The <strong>"Crown Jewel"</strong> feature—select dozens of holes and apply global drilling parameters to all of them instantly.</li>
</ul>
</li>
<li><strong>Full Simulation:</strong> Generates complete Approach, Drill, and Retract targets within RoboDK automatically.</li>
</ul>
<p><a href="./RoboDK_Process_Automation/Drilling_Manager"><strong>Test files &amp; output</strong></a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Aw_dtBkk4sY"><strong>Watch demo</strong></a></p>
<details>
<summary>Video previews</summary>
<br>
<p><a href="https://www.youtube.com/watch?v=Aw_dtBkk4sY"><img src="https://img.youtube.com/vi/Aw_dtBkk4sY/hqdefault.jpg" width="480" alt="Automated Drilling - FreeCAD Plugin Demo"></a><br><a href="https://www.youtube.com/watch?v=Aw_dtBkk4sY">Automated Drilling - FreeCAD Plugin Demo</a></p>
</details>
</td></tr>
</table>

<p align="right"><a href="#toolbar-layout">Tool index ↑</a> &nbsp;·&nbsp; <a href="#top">Back to top ↑</a></p>

