#!/bin/sh
# Create project tree
./scripts/make_tree.sh

# Copy static assets
./scripts/copy_static.sh

# Export index and pages
./scripts/export_index.sh
./scripts/export_pages.sh

# Export posts
./scripts/export_posts.sh

# Export talks
./scripts/export_talks.sh
