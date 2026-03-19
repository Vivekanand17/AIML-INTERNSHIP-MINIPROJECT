# MLP Sklearn Fix - Classification Support

## Plan Steps:
- [x] **Step 1**: Create/Update TODO.md 
- [ ] **Step 2**: Edit backend/models.py (add MLPClassifier, accuracy_score import)
- [ ] **Step 3**: Edit backend/train.py (classification logic in MLP branch)
- [ ] **Step 4**: Edit backend/utils.py (enhance diagnostics)
- [ ] **Step 5**: Test uvicorn app:app --reload
- [ ] **Step 6**: MLP FIXED SUCCESSFULLY USING SKLEARN

**Details**:
- Detect classification: y.nunique() < 10
- Classifier: MLPClassifier mirror Regressor params
- Metrics: accuracy_score for logs
- Keep regression unchanged
- No API changes

