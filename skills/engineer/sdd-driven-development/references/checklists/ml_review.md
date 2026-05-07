# ML/CV SDD Review Checklist

## Experiment and data
- [ ] Hypothesis and target metric are explicit.
- [ ] Dataset schema and split strategy are explicit.
- [ ] Leakage risks and mitigation are documented.
- [ ] Reproducibility settings (seed/version) are present.

## Model and performance
- [ ] Baseline and promotion threshold are defined.
- [ ] Hyperparameter search space and budget are bounded.
- [ ] Latency/memory constraints are specified.
- [ ] Failure criteria and rollback policy are defined.

## Evaluation and operations
- [ ] Slice analysis or edge-condition testing is defined.
- [ ] Monitoring and drift detection plan is defined.
- [ ] Model registration metadata contract is defined.

## Verification
- [ ] Training validation is reproducible.
- [ ] Inference validation covers worst-case inputs.
- [ ] Promotion decision is traceable to predefined criteria.

