FROM astral/uv:python3.11-trixie

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync

CMD ["/bin/bash"]