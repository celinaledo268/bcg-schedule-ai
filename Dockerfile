FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
WORKDIR /workspace
COPY requirements.txt pyproject.toml ./
COPY code ./code
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -e .
COPY configs ./configs
COPY scripts ./scripts
COPY dataset_links.txt README.md LICENSE ./
