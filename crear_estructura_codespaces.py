# -*- coding: utf-8 -*-
"""Crear y publicar la estructura de las 49 herramientas desde Codespaces.

Ejecutar dentro del repositorio, en main:
    python3 crear_estructura_codespaces.py

Usa la autenticacion de Git configurada en Codespaces.
"""

from pathlib import Path
import subprocess

GROUPS = {
    "MANUFAI Workbench/Make Weld Trajectories": [
        "Edge Split", "Find Weldable Edges",
        "Weld Creators", "Add Normals",
        "Surface Weld", "Weld Loader",
    ],
    "MANUFAI Workbench/Positions": [
        "Make Positions Groups", "Assign Welds To Robots",
        "SubAssembly", "Assign Positions",
        "Move SubAssembly", "Move Welds",
    ],
    "MANUFAI Workbench/Length": [
        "Weld Length Report",
    ],
    "MANUFAI Workbench/Cycle Time": [
        "Process", "Assign Process",
        "Welding Parameters", "Assign Welding Parameters",
        "Cycle Time",
    ],
    "MANUFAI Workbench/Weight": [
        "Create Materials", "Assign Materials",
        "Weight of Welding and Welded Part",
    ],
    "MANUFAI Workbench/Welding Sequence AI Advisor": [
        "Export STL", "Export As DK Project",
    ],
    "MANUFAI Workbench/Sequence and Process Visualization": [
        "Assign Sequence", "Weld Simulation",
        "Show Weld Sphere", "Visualizer",
    ],
    "3-2-1 Datum Based Alignment & Tools": [
        "Toggle Visibility Recursive", "Create Center Point",
        "Create Sphere at Origin", "Datum A",
        "Datum B", "Datum C",
        "3-2-1 Datum-Based Alignment", "Move Model To Origin",
        "Reset Position", "Show Welding Widget",
        "Launch Find Data Panel", "Focus Object",
        "Move Weld Lines", "Discretize",
    ],
    "C3P - WdCurve Tools": [
        "Line Weld Table", "Show Names",
        "Selection Mode (X-Ray & Filter)",
    ],
    "RoboDK & Process Automation": [
        "Export To .rdk Project", "Export Full",
        "Export Selected", "Glue Manager",
        "Drilling Manager",
    ],
}

SUBFOLDERS = (
    "Resources",
    "Materials/01 Files needed to test",
    "Materials/02 Output",
)


def git(*args):
    return subprocess.run(["git", *args], check=True)


def main():
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], text=True
    ).strip()
    if branch != "main":
        raise SystemExit("Ejecuta este bloque en la rama main.")
    root = Path(subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip())
    git("-C", str(root), "pull", "--ff-only")
    paths = []
    tools = 0
    for group, names in GROUPS.items():
        for name in names:
            tools += 1
            for subfolder in SUBFOLDERS:
                relative = group + "/" + name + "/" + subfolder + "/.gitkeep"
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    with target.open("xb"):
                        pass
                paths.append(relative)
    git("-C", str(root), "add", "--", *paths)
    result = subprocess.run([
        "git", "-C", str(root), "diff", "--cached", "--quiet", "--", *paths
    ])
    if result.returncode == 1:
        git("-C", str(root), "commit", "--quiet", "--only", "-m",
            "Create tool folders with Resources, test files and Output", "--", *paths)
    elif result.returncode != 0:
        raise SystemExit(result.returncode)
    git("-C", str(root), "push", "origin", "main")
    print("Estructura publicada:", tools, "herramientas.")
    print("Cada una contiene Resources y Materials con 01 Files needed to test y 02 Output.")


if __name__ == "__main__":
    main()

