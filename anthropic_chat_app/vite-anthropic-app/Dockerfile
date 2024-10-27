# Stage 1: Build Stage
FROM node:22-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of your application code to the working directory
COPY . .

# Build the application for production
RUN npm run build

# Stage 2: Production Stage
FROM nginx:alpine

# Copy built files from builder stage to NGINX html folder
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 for NGINX
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]