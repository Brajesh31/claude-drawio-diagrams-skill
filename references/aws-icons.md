# AWS Architecture Icon Guidance

Use AWS architecture icons only when the diagram actually represents AWS services or resources.

## Safe usage
- Obtain icon assets from the current official AWS Architecture Icons package or the official draw.io AWS shape library.
- Follow the applicable AWS icon usage guidance and do not modify official artwork in a way that changes its meaning.
- Prefer the current icon set and verify service names against current AWS product documentation.
- Use the icon's official service label nearby when the symbol may not be familiar.
- Keep icon sizes and label placement consistent across the diagram.

## Draw.io styles
Draw.io libraries may expose AWS shapes through style identifiers such as `mxgraph.aws4.*`. These identifiers can change between library versions. Confirm a shape exists in the installed library before relying on it.

## Do not
- Invent a style identifier and assume it renders.
- Use an AWS icon for a generic or non-AWS component.
- Treat an icon as proof that a service supports a particular feature or integration.
- bundle vendor icon artwork into a project unless its license and redistribution terms permit it.

## Validation
After inserting AWS shapes, open the diagram in draw.io and export a preview. A valid XML file can still contain missing or unresolved library shapes.
