---
name: drawio-diagrams
description: Creates, edits, validates, and exports draw.io diagrams using native .drawio XML, consistent layouts, clear visual hierarchy, and reviewable architecture conventions.
---

# Draw.io Diagram Skill

Use this skill when creating or maintaining diagrams in draw.io / diagrams.net, especially editable `.drawio` XML files, architecture diagrams, process flows, data flows, sequence diagrams, and infrastructure diagrams.

## Core rules
- Treat `.drawio` XML as the editable source of truth.
- Do not edit exported PNG files as if they were source diagrams.
- Preserve existing page structure, IDs, and user-authored content unless a change requires otherwise.
- Keep diagrams accurate before making them visually attractive.
- Use official vendor icon libraries when the diagram represents a real vendor service. Never invent a vendor icon or imply an unsupported service capability.
- Keep labels concise, relationships explicit, and connectors behind nodes where practical.
- Use a consistent font, text scale, line weight, spacing, and color system.
- Use color and shape together to communicate meaning. Do not rely on color alone.
- For complex systems, split context, container, component, deployment, data-flow, and sequence views rather than forcing everything onto one canvas.

## Editing workflow
1. Inspect the existing `.drawio` XML and identify pages, cells, IDs, styles, and geometry.
2. Confirm the diagram's audience, purpose, scope, and expected level of detail.
3. Plan the hierarchy and flow before changing coordinates.
4. Make focused XML edits. Keep cell IDs unique and preserve valid parent/source/target references.
5. Validate XML structure with `scripts/validate_drawio.py`.
6. Export a preview with `scripts/convert-drawio-to-png.sh` when the draw.io desktop/CLI executable is installed.
7. Visually inspect the exported image for clipped labels, crossing connectors, overlaps, bad margins, and unreadable text.
8. Report what changed and identify anything that could not be visually verified.

## Layout guidance
- Use a clear reading direction, usually left-to-right or top-to-bottom.
- Align related nodes and distribute spacing consistently.
- Leave enough padding inside containers and around page edges.
- Keep connectors from crossing labels and unrelated nodes.
- Place connectors behind shapes where possible.
- Use orthogonal connectors for architecture and process diagrams unless another route is clearer.
- Label non-obvious relationships and add a legend for custom notation.
- Use multiple diagrams when a single diagram becomes crowded.

See:
- `references/layout-guidelines.md`
- `references/aws-icons.md`
- `templates/architecture.drawio`
- `scripts/validate_drawio.py`
- `scripts/convert-drawio-to-png.sh`

## Export
Use the conversion script for PNG previews. It requires a local draw.io / diagrams.net command-line executable named `drawio` or an explicit executable path via `DRAWIO_BIN`. Never claim an export succeeded unless the command completed and the output file exists.

## Completion checklist
- [ ] Editable source remains a valid `.drawio` file
- [ ] Cell IDs are unique
- [ ] All connectors point to valid cells or valid explicit points
- [ ] Labels are readable and not clipped
- [ ] Nodes are aligned and consistently spaced
- [ ] Connectors do not obscure labels or important shapes
- [ ] Containers have adequate internal margins
- [ ] Color contrast is sufficient
- [ ] Legend and metadata are included when useful
- [ ] Exported preview was visually inspected, or the limitation is disclosed
