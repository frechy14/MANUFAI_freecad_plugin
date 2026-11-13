# -*- coding: utf-8 -*-
"""Elimina los 99 SVG de la raiz incluidos en la lista proporcionada.

Ver la lista, sin modificar el repositorio:
    py borrar_svg_sueltos.py

Borrarlos en GitHub mediante un commit en main:
    py borrar_svg_sueltos.py --borrar

Requiere Python, sin paquetes adicionales. Para borrar pide un token
con Contents: Read and write para frechy14/MANUFAI_freecad_plugin.
El token se introduce oculto y no se guarda.
"""

import argparse
import base64
import getpass
import html
import json
import posixpath
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

REPOSITORY = "frechy14/MANUFAI_freecad_plugin"
BRANCH = "main"
TARGET_FILES = [
    "activation.svg",
    "back-index.svg",
    "back-top.svg",
    "category-cycle-time-tools.svg",
    "category-length.svg",
    "category-make-weld-trajectories.svg",
    "category-positions.svg",
    "category-simulation.svg",
    "category-weight.svg",
    "category-wso.svg",
    "component-manager.svg",
    "index-c3p-wdcurve-tools.svg",
    "index-cycle-time-tools.svg",
    "index-datum-alignment-tools.svg",
    "index-length.svg",
    "index-make-weld-trajectories.svg",
    "index-manufai-workbench.svg",
    "index-positions.svg",
    "index-robodk-process-automation.svg",
    "index-simulation.svg",
    "index-weight.svg",
    "index-wso.svg",
    "installation-tutorial.svg",
    "installation.svg",
    "interoperability.svg",
    "key-capabilities.svg",
    "manufai-hero.svg",
    "nav-3-2-1-alignment.svg",
    "nav-activation.svg",
    "nav-add-normals.svg",
    "nav-assign-materials.svg",
    "nav-assign-positions.svg",
    "nav-assign-process.svg",
    "nav-assign-sequence.svg",
    "nav-assign-welding-parameters.svg",
    "nav-assign-welds-to-robots.svg",
    "nav-create-center-point.svg",
    "nav-create-materials.svg",
    "nav-create-sphere-at-origin.svg",
    "nav-cycle-time.svg",
    "nav-datum-a.svg",
    "nav-datum-b.svg",
    "nav-datum-c.svg",
    "nav-discretize.svg",
    "nav-download.svg",
    "nav-drilling-manager.svg",
    "nav-edge-split.svg",
    "nav-export-as-dk-project.svg",
    "nav-export-full.svg",
    "nav-export-selected.svg",
    "nav-export-stl.svg",
    "nav-find-weldable-edges.svg",
    "nav-focus-object-command.svg",
    "nav-glue-manager.svg",
    "nav-index.svg",
    "nav-installation.svg",
    "nav-launch-find-data-panel.svg",
    "nav-line-weld-table.svg",
    "nav-make-positions.svg",
    "nav-move-model-to-origin.svg",
    "nav-move-subassembly.svg",
    "nav-move-weld-lines.svg",
    "nav-move-welds.svg",
    "nav-process.svg",
    "nav-reset-pos.svg",
    "nav-resources.svg",
    "nav-selection-mode.svg",
    "nav-show-names.svg",
    "nav-show-welding-widget-command.svg",
    "nav-subassembly.svg",
    "nav-surface-weld.svg",
    "nav-toggle-visibility-recursive.svg",
    "nav-visualizer-cmd.svg",
    "nav-weight-of-welding-and-welded-part.svg",
    "nav-weld-creators.svg",
    "nav-weld-data-to-robodk.svg",
    "nav-weld-length-report.svg",
    "nav-weld-loader.svg",
    "nav-weld-simulation.svg",
    "nav-weld-visualizer.svg",
    "nav-welding-parameters.svg",
    "open-download.svg",
    "open-materials.svg",
    "overview.svg",
    "repository-resources.svg",
    "requirements.svg",
    "section-c3p-wdcurve-tools.svg",
    "section-datum-alignment-tools.svg",
    "section-manufai-workbench.svg",
    "section-robodk-process-automation.svg",
    "tool-3-2-1-alignment.svg",
    "tool-add-normals.svg",
    "tool-assign-materials.svg",
    "tool-assign-positions.svg",
    "tool-assign-process.svg",
    "tool-assign-sequence.svg",
    "tool-assign-welding-parameters.svg",
    "tool-assign-welds-to-robots.svg",
    "tool-create-center-point.svg"
]


def github_api(token, method, endpoint, payload=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "MANUFAI-root-svg-cleanup",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(
        "https://api.github.com/repos/" + REPOSITORY + "/" + endpoint,
        data=None if payload is None else json.dumps(payload).encode("utf-8"),
        headers=headers,
        method=method,
    )
    try:
        with urlopen(request, timeout=60) as response:
            return json.load(response)
    except HTTPError as exc:
        try:
            detail = json.loads(exc.read().decode("utf-8")).get("message", exc.reason)
        except (ValueError, UnicodeDecodeError):
            detail = str(exc.reason)
        hint = ""
        if exc.code in (401, 403):
            hint = " Revisa el acceso al repositorio y el permiso Contents: Read and write."
        raise RuntimeError("HTTP " + str(exc.code) + ": " + str(detail) + hint) from None
    except URLError as exc:
        raise RuntimeError("No se pudo conectar con GitHub: " + str(exc.reason)) from None


def root_references(text, document, targets):
    references = re.findall(
        r"""(?:src|href|xlink:href)\s*=\s*["']([^"']+)["']""",
        text, flags=re.IGNORECASE,
    )
    references += re.findall(r"\]\(\s*<?([^\s)>]+)", text)
    matches = set()
    for reference in references:
        parts = urlsplit(html.unescape(reference))
        path = unquote(parts.path)
        if parts.netloc:
            host = parts.netloc.lower()
            if host == "github.com":
                prefixes = ["/" + REPOSITORY + "/blob/" + BRANCH + "/",
                            "/" + REPOSITORY + "/raw/" + BRANCH + "/"]
            elif host == "raw.githubusercontent.com":
                prefixes = ["/" + REPOSITORY + "/" + BRANCH + "/"]
            else:
                continue
            prefix = next((prefix for prefix in prefixes if path.startswith(prefix)), None)
            if prefix is None:
                continue
            resolved = posixpath.normpath(path[len(prefix):])
        elif parts.scheme:
            continue
        else:
            resolved = posixpath.normpath(
                path.lstrip("/") if path.startswith("/") else
                posixpath.join(posixpath.dirname(document), path)
            )
        if resolved in targets:
            matches.add(resolved)
    return matches


def clean_root(api, execute=False):
    old_head = api("GET", "git/ref/heads/" + BRANCH)["object"]["sha"]
    base_tree = api("GET", "git/commits/" + old_head)["tree"]["sha"]
    snapshot = api("GET", "git/trees/" + base_tree + "?recursive=1")
    if snapshot.get("truncated"):
        raise RuntimeError("GitHub devolvio un arbol incompleto. Se detuvo el proceso.")
    existing = {entry["path"]: entry for entry in snapshot["tree"]}
    candidates = sorted(
        name for name in TARGET_FILES
        if "/" not in name and name.endswith(".svg")
        and name in existing and existing[name]["type"] == "blob"
    )
    if not candidates:
        print("Los SVG de la lista ya no estan en la raiz.")
        return None

    # Comprobar los enlaces de los documentos actuales antes de publicar.
    blocked = []
    target_set = set(candidates)
    for entry in snapshot["tree"]:
        if entry["type"] != "blob" or not entry["path"].lower().endswith((".md", ".html", ".htm")):
            continue
        blob = api("GET", "git/blobs/" + entry["sha"])
        if blob.get("encoding") != "base64":
            raise RuntimeError("No se pudo leer el documento: " + entry["path"])
        text = base64.b64decode(blob["content"]).decode("utf-8-sig")
        for name in sorted(root_references(text, entry["path"], target_set)):
            blocked.append(entry["path"] + " -> " + name)
    if blocked:
        raise RuntimeError(
            "Hay documentos que aun usan estos SVG de la raiz. Corrige sus enlaces primero:\n"
            + "\n".join(blocked)
        )

    print("Repositorio:", REPOSITORY)
    print("SVG de la lista presentes en la raiz:", len(candidates))
    for name in candidates:
        print("  " + name)
    if not execute:
        print("\nVista previa. No se ha borrado nada.")
        print("Para borrarlos: py borrar_svg_sueltos.py --borrar")
        return candidates

    deletion_entries = [
        {"path": name, "mode": existing[name]["mode"], "type": "blob", "sha": None}
        for name in candidates
    ]
    tree_sha = api("POST", "git/trees", {
        "base_tree": base_tree,
        "tree": deletion_entries,
    })["sha"]
    updated = api("GET", "git/trees/" + tree_sha + "?recursive=1")
    if updated.get("truncated"):
        raise RuntimeError("No se pudo comprobar el nuevo arbol. La rama no se actualizo.")

    def entries_map(entries):
        return {
            entry["path"]: (entry["mode"], entry["type"], entry["sha"])
            for entry in entries
        }

    expected = entries_map([
        entry for entry in snapshot["tree"] if entry["path"] not in target_set
    ])
    if entries_map(updated["tree"]) != expected:
        raise RuntimeError("El nuevo arbol contiene cambios inesperados. La rama no se actualizo.")

    commit_sha = api("POST", "git/commits", {
        "message": "Remove unused SVG files from repository root",
        "tree": tree_sha,
        "parents": [old_head],
    })["sha"]
    if api("GET", "git/ref/heads/" + BRANCH)["object"]["sha"] != old_head:
        raise RuntimeError("La rama main cambio. Vuelve a ejecutar el script.")
    result = api("PATCH", "git/refs/heads/" + BRANCH, {
        "sha": commit_sha,
        "force": False,
    })
    if result["object"]["sha"] != commit_sha:
        raise RuntimeError("No se pudo verificar el commit publicado.")
    print("\nSVG borrados:", len(candidates))
    print("https://github.com/" + REPOSITORY + "/commit/" + commit_sha)
    return commit_sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--borrar", action="store_true",
                        help="Eliminar los SVG de la lista en un commit en main.")
    args = parser.parse_args()
    token = None
    if args.borrar:
        token = getpass.getpass("Token de GitHub (no se mostrara): ").strip()
        if not token:
            raise RuntimeError("No se introdujo un token.")
    clean_root(
        lambda method, endpoint, payload=None: github_api(token, method, endpoint, payload),
        execute=args.borrar,
    )


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        print("\nProceso interrumpido.", file=sys.stderr)
        sys.exit(1)

