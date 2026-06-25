# Figure Spec Schema

Use this schema before generating or editing any non-trivial article image.

The schema turns a vague prompt into a checkable visual brief. It is especially important when the user gives a full article and expects the skill to decide what diagrams are needed.

## Package Spec

```text
package:
  article_title:
  output_language:
  article_thesis:
  package_goal:
  number_of_images:
  package_rhythm:
  shared_metaphor_world:
  shared_visual_tokens:
    colors:
    line_roles:
    label_containers:
    typography_mode:
    font_feeling:
  package_symbol_legend:
    primitive_geometry:
    shape_meanings:
    color_meanings:
    recurring_marks:
    inheritance_rule:
  intentional_variety:
    forms:
    scales:
    reader_paths:
  skipped_sections:
    - source_anchor:
      reason:
```

## Single Figure Spec

```text
figure:
  id:
  placement:
  package_role:
  source_anchor:
  article_job:
  reader_takeaway:
  misunderstanding_prevented:
  selection:
    simplest_sufficient_rung:
    why_not_simpler:
    why_not_more_complex:
    complexity_budget:
      claims:
      stages_or_zones:
      objects:
      labels:
      accent_colors:
      forms:
    accuracy_risk:
  diagram:
    structure:
    family:
    specific_form:
    spatial_mode:
    layout_skeleton:
    three_second_read:
    rejected_forms:
    data_rules:
    causality_rules:
  visual_tokens:
    color_roles:
    line_roles:
    line_patterns:
    shape_roles:
    label_containers:
    emphasis_rule:
    spatial_tokens:
  typography:
    mode: draft_labels | publish_overlay
    font_feeling:
    L1:
    L2:
    L3:
    text_zones:
    text_free_zones:
  human_presence:
    level: H0 | H1 | H2 | H3 | H4 | H5
    charm_level: C0 | C1 | C2 | C3 | C4 | C5
    form: none | human_trace | role_token | abstract_faceless_figure | storybook_actor | explicit_mascot
    what_it_clarifies:
    forbidden_traits:
  action_character:
    use_character: yes | no
    operator: none | Thread Runner | Lens Keeper | Gate Builder | other
    action_verb:
    object_acted_on:
    relation_clarified:
    what_breaks_if_removed:
    scale:
    forbidden_drift:
  visual_harness:
    output_family:
    form_family:
    spatial_mode:
    style_lineage:
    abstraction_level:
    material:
    line_behavior:
    color_system:
    composition_engine:
    human_presence:
    typography_mode:
    why_this_lineage_helps:
    anti_copy_boundary:
  image_quality:
    quality_target:
    material_family:
    grid_and_margins:
    focal_hierarchy:
    palette_discipline:
    typography_overlay_plan:
    texture_depth_rule:
    negative_space_contract:
    anti_default_ai:
    default_generation_smoke_target:
  composition_stability:
    preset:
    fixed_layout:
    max_anchors:
    max_labels:
    focal_module:
    seven_word_reader_path:
    quiet_zones:
    forbidden_drift:
  composition:
    canvas:
    grid:
    reader_path:
    focal_action:
    carrier:
    key_objects:
    whitespace_plan:
    focal_surprise:
  prompt_constraints:
    must_show:
    must_not_show:
    anti_copy_boundary:
  beauty_gate:
    target_score:
    accurate_because:
    understandable_because:
    desirable_because:
    removed_for_simplicity:
    remaining_risk:
```

## Required Fields

Do not generate until these fields are filled:

- source anchor
- reader takeaway
- misunderstanding prevented
- simplest sufficient rung
- exact diagram family and specific form
- complexity budget
- visual token plan
- typography mode
- human presence and charm level
- action character decision: none or one Paper Operator; article domain; operator family; action verb; object acted on; what breaks if removed
- visual harness style lineage and anti-copy boundary
- visual harness output family, form family, spatial mode, material, line behavior, color system, and composition engine
- image quality harness: material family, grid/margins, focal hierarchy, palette discipline, typography/overlay plan, negative space contract, and anti-default-AI constraints
- composition stability preset: exactly one preset, fixed layout, max anchors, max labels, focal module, quiet zones, and forbidden drift
- reader path
- accuracy risk
- must-not-show constraints

## Compact Spec For Fast Work

For short requests, use this compact version:

```text
figure spec:
- source anchor:
- reader takeaway:
- misunderstanding prevented:
- simplest sufficient rung:
- form: family / specific form / spatial mode
- complexity budget: claims / objects / labels / colors
- visual tokens: colors / lines / labels / shapes
- typography: mode / font feeling / L1-L3
- human presence: H level / C level / form / what it clarifies
- action character: none or operator / action verb / object acted on / what breaks if removed
- visual harness: output family / form family / spatial mode / style lineage / abstraction / material / line / color / composition / anti-copy boundary
- image quality: quality target / material family / grid and margins / focal hierarchy / palette / typography overlay plan / negative space / anti-default-AI
- composition stability: preset / max anchors / max labels / focal module / quiet zones / forbidden drift
- reader path:
- focal surprise:
- accuracy risk:
- must not show:
```

## Validation

Before image generation, ask:

- Could a different person read this spec and produce the same kind of image?
- Does the spec forbid the likely wrong image?
- Does the spec say what text should exist and where it belongs?
- Does the spec state when simpler is better?
- Does the spec protect accuracy from metaphor drift?
- Does the image quality section translate taste into visible art direction rather than abstract praise?
- Does the composition stability section prevent the model from inventing a different layout?
- If a character is used, does the spec say what breaks if removed?

If not, repair the spec before prompting.
