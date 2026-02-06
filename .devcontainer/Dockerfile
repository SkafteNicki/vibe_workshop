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

# Install OpenCode and Ralphy globally
RUN npm install -g opencode-ai ralphy-cli

# Install pyright for Python type checking
RUN pip install --no-cache-dir pyright

# Verify installations
RUN opencode --version && ralphy --version && pyright --version
