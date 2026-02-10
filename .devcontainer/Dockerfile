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
ENV PATH="/root/.local/bin:${PATH}"

# Install OpenCode and Ralphy globally
RUN npm install -g opencode-ai ralphy-cli

# Install get-shit-done-cc for OpenCode
RUN npx get-shit-done-cc --opencode --global

# Install pyright for Python type checking using uv
RUN uv tool install pyright

# Install specify-cli from GitHub spec-kit
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Copy version check script and make it executable
COPY check-versions.sh /usr/local/bin/check-versions.sh
RUN chmod +x /usr/local/bin/check-versions.sh

# Verify installations using the script
RUN /usr/local/bin/check-versions.sh
