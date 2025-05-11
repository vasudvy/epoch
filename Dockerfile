# Use an official Node.js runtime as a parent image
FROM node:16-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies only when needed to avoid rebuilding on every change
COPY package*.json ./

# Install the Codex package and any additional dependencies (if needed)
RUN npm install -g @openai/codex

# Copy the rest of your application code into the container
COPY . .

# Set up a non-root user for running the application (safer for production)
RUN useradd -ms /bin/bash codexuser && chown -R codexuser:codexuser /app
USER codexuser

# Expose port if you are running any server or interacting through ports
EXPOSE 8080

# Set the default command to run Codex
CMD ["codex"]
