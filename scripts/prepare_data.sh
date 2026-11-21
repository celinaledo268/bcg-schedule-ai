mkdir -p data/raw data/processed
python - <<'PY'
from pathlib import Path
Path('data/processed').mkdir(parents=True, exist_ok=True)
PY
