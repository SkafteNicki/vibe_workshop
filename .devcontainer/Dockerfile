FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Node.js LTS
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python and pip (if not already included in base image)
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Python package and tool manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install OpenCode and Ralphy globally
RUN npm install -g opencode-ai ralphy-cli

# Install pyright for Python type checking
RUN pip install --no-cache-dir pyright

# Install specify-cli from GitHub spec-kit
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify installations
RUN opencode --version && ralphy --version && pyright --version && specify --version
