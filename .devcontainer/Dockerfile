FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Node.js LTS
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python and pip (if not already included in base image)
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Python package and tool manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local/bin sh

# Install OpenCode and Pi globally
RUN npm install -g opencode-ai @mariozechner/pi-coding-agent

# Install pyright for Python type checking using pip so the binary is on PATH
RUN python3 -m pip install --break-system-packages pyright

# Copy version check script and make it executable
COPY check-versions.sh /usr/local/bin/check-versions.sh
RUN chmod +x /usr/local/bin/check-versions.sh

# Verify installations using the script
RUN /usr/local/bin/check-versions.sh
