FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Node.js LTS
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCode and Ralphy globally
RUN npm install -g opencode-ai ralphy-cli

# Verify installations
RUN opencode --version && ralphy --version
