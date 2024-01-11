#!/bin/bash


echo "Deploy"

# Define front-end deployment flow
cd frontend && ./deploy.sh
cd ..
# Define back-end deployment flow
cd backend && ./deploy.sh

echo "Done."
